from musion import SaveConfig
import cProfile
import itertools
import os
from multiprocessing import set_start_method

from tqdm import tqdm

from musion import Struct
from musion.dev_tools import timer

@timer
def test_continous_running_sequential(audio_list, times=10):
    audio_itr = itertools.cycle(audio_list)

    struct = Struct()
    for _ in range(times):
        struct(audio_path=next(audio_itr))

def convert():
    tg_dir = '/mnt/nas_hanyu/Project/Tag_music/data/七层段落标注6837首'
    tgt_dir =  '/mnt/nas1/users/tianwei.zhao/dataset/ai1/skymusic_6000/struct'
    for r,d,files in tqdm(os.walk(tg_dir)):
        for file in files:
            if file.endswith('.TextGrid'):
                intervals, labels = textgrid2struct(os.path.join(r, file))
                with open(os.path.join(tgt_dir, file.replace('.TextGrid', '.struct')), 'w') as f:
                    for interval, label in zip(intervals, labels):
                        f.write(f'{interval[0]} {interval[1]} {label}\n')

def test_struct():
    # audio_path = '/mnt/nas_tianwei/music/Time after time ～花舞う街で～（theater version）.mp3'
    audio_path = '/mnt/nas_tianwei/music/irr_sig/'
    struct = Struct()
    save_cfg = SaveConfig('./test_data/struct')
    res = struct(audio_path=audio_path, 
           save_cfg=save_cfg,
           overwrite=True,
           num_workers=3)
    # print(res)

if __name__ == '__main__':
    set_start_method('spawn')
    audio_dir = '/mnt/nas1/users/tianwei.zhao/music'

    test_struct()
