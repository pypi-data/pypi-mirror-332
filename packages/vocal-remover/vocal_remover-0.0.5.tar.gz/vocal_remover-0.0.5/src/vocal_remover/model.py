import numpy as np
import torch
from tqdm import tqdm

from vocal_remover import dataset
from vocal_remover import nets
from vocal_remover import spec_utils
import os
import librosa
import soundfile as sf
from huggingface_hub import hf_hub_download

n_fft = 2048
hop_length = 1024
sr = 44100
batchsize = 4
cropsize = 256
postprocess = False
# output_dir = "output"
tta = False

class Separator(object):

    def __init__(self, device=None, batchsize=4, cropsize=256, postprocess=False):
        self.model = self.load_vr_model()
        self.offset = self.model.offset
        self.device = device
        self.batchsize = batchsize
        self.cropsize = cropsize
        self.postprocess = postprocess
        
        

    def _postprocess(self, X_spec, mask):
        if self.postprocess:
            mask_mag = np.abs(mask)
            mask_mag = spec_utils.merge_artifacts(mask_mag)
            mask = mask_mag * np.exp(1.j * np.angle(mask))

        X_mag = np.abs(X_spec)
        X_phase = np.angle(X_spec)

        y_spec = mask * X_mag * np.exp(1.j * X_phase)
        v_spec = (1 - mask) * X_mag * np.exp(1.j * X_phase)
        # y_spec = X_spec * mask
        # v_spec = X_spec - y_spec

        return y_spec, v_spec

    def _separate(self, X_spec_pad, roi_size):
        X_dataset = []
        patches = (X_spec_pad.shape[2] - 2 * self.offset) // roi_size
        for i in range(patches):
            start = i * roi_size
            X_spec_crop = X_spec_pad[:, :, start:start + self.cropsize]
            X_dataset.append(X_spec_crop)

        X_dataset = np.asarray(X_dataset)

        self.model.eval()
        with torch.no_grad():
            mask_list = []
            # To reduce the overhead, dataloader is not used.
            for i in tqdm(range(0, patches, self.batchsize)):
                X_batch = X_dataset[i: i + self.batchsize]
                X_batch = torch.from_numpy(X_batch).to(self.device)

                mask = self.model.predict_mask(torch.abs(X_batch))

                mask = mask.detach().cpu().numpy()
                mask = np.concatenate(mask, axis=2)
                mask_list.append(mask)

            mask = np.concatenate(mask_list, axis=2)

        return mask

    def separate(self, X_spec):
        n_frame = X_spec.shape[2]
        pad_l, pad_r, roi_size = dataset.make_padding(n_frame, self.cropsize, self.offset)
        X_spec_pad = np.pad(X_spec, ((0, 0), (0, 0), (pad_l, pad_r)), mode='constant')
        X_spec_pad /= np.abs(X_spec).max()

        mask = self._separate(X_spec_pad, roi_size)
        mask = mask[:, :, :n_frame]

        y_spec, v_spec = self._postprocess(X_spec, mask)

        return y_spec, v_spec

    def separate_tta(self, X_spec):
        n_frame = X_spec.shape[2]
        pad_l, pad_r, roi_size = dataset.make_padding(n_frame, self.cropsize, self.offset)
        X_spec_pad = np.pad(X_spec, ((0, 0), (0, 0), (pad_l, pad_r)), mode='constant')
        X_spec_pad /= X_spec_pad.max()

        mask = self._separate(X_spec_pad, roi_size)

        pad_l += roi_size // 2
        pad_r += roi_size // 2
        X_spec_pad = np.pad(X_spec, ((0, 0), (0, 0), (pad_l, pad_r)), mode='constant')
        X_spec_pad /= X_spec_pad.max()

        mask_tta = self._separate(X_spec_pad, roi_size)
        mask_tta = mask_tta[:, :, roi_size // 2:]
        mask = (mask[:, :, :n_frame] + mask_tta[:, :, :n_frame]) * 0.5

        y_spec, v_spec = self._postprocess(X_spec, mask)

        return y_spec, v_spec

    def split(self, input, output_dir):
        sr = 44100
        print('loading wave source...', end=' ')
        X, sr = librosa.load(
            input, sr=sr, mono=False, dtype=np.float32, res_type='kaiser_fast'
        )
        basename = os.path.splitext(os.path.basename(input))[0]
        print('done')

        if X.ndim == 1:
            # mono to stereo
            X = np.asarray([X, X])

        X_spec = spec_utils.wave_to_spectrogram(X, hop_length, n_fft)

        if tta:
            y_spec, v_spec = self.separate_tta(X_spec)
        else:
            y_spec, v_spec = self.separate(X_spec)

        output_dir = output_dir
        if output_dir != "":  # modifies output_dir if theres an arg specified
            output_dir = output_dir.rstrip('/') + '/'
            os.makedirs(output_dir, exist_ok=True)

        wave = spec_utils.spectrogram_to_wave(y_spec, hop_length=hop_length)
        sf.write('{}accompaniment.wav'.format(output_dir), wave.T, sr)

        print('inverse stft of vocals...', end=' ')
        wave = spec_utils.spectrogram_to_wave(v_spec, hop_length=hop_length)
        print('done')
        sf.write('{}vocals.wav'.format(output_dir), wave.T, sr)

    def load_vr_model(self):

        print('loading model...', end=' ')
        model_ckpt_path = hf_hub_download(repo_id="hoseinshr1055/vocal_remover", filename="baseline.pth")
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        model = nets.CascadedNet(n_fft, hop_length, 32, 128)
        model.load_state_dict(torch.load(model_ckpt_path, map_location='cpu'))
        model.to(device)
        print('done')
        return model


