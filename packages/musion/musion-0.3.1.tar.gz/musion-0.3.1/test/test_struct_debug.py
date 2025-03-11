import numpy as np
import librosa

from musion import Separate, SaveConfig

def show_close(pred, label):
    print(pred.shape, label.shape, pred.size)
    res = np.isclose(pred, label, atol=0.001)
    num_pos = np.sum(res)
    print(num_pos, num_pos / pred.size)

def test_all_close(data_pair):
    for gt_path, pred_path in data_pair:
        demucs_res, _ = librosa.load(gt_path, sr=None)
        pred, _ = librosa.load(pred_path, sr=None)
        print(max(pred), max(demucs_res))

        show_close(pred, demucs_res[:-1])

def tes_close_from_audio(audio_path):
    sep = Separate()
    sep(audio_path=audio_path, save_cfg=SaveConfig('./'))

    # demucs.separate.main([audio_path])

    # pred = np.load('./pred.npy')
    # label = np.load('./label.npy')
    # show_close(pred, label)

if __name__ == '__main__':
    data_pair = [('./separated/htdemucs/4.Time after time ～花舞う街で～（theater version）/vocals.wav',
                 './4.Time after time ～花舞う街で～（theater version）.vocals.wav')
                ]
    
    tes_close_from_audio('/mnt/nas1/users/tianwei.zhao/music/4.Time after time ～花舞う街で～（theater version）.mp3')
    test_all_close(data_pair)