import cProfile
import itertools
# logging.basicConfig(level=logging.DEBUG)
import csv

import torch.multiprocessing as tmp

from musion.dev_tools import timer
from musion import Separate, SaveConfig

import demucs.separate

@timer
def test_continous_running_sequential(audio_list, times=10):
    audio_itr = itertools.cycle(audio_list)

    sep = Separate()
    for _ in range(times):
        sep(audio_path=next(audio_itr), save_cfg=SaveConfig('./test'))

@timer
def test_continous_running_parallel(audio_list, times=10):
    audio_itr = itertools.cycle(audio_list)
    full_audio_list = []
    for _ in range(times):
        full_audio_list.append(next(audio_itr))

    sep = Separate()
    sep(audio_path=full_audio_list, num_threads = 10)

@timer
def test_continous_running_sequential_demucs(audio_list, times=10):
    audio_itr = itertools.cycle(audio_list)
    full_audio_list = []
    for _ in range(times):
        full_audio_list.append(next(audio_itr))
    demucs_infer(full_audio_list)

def demucs_infer(audio_list):
    demucs.separate.main(audio_list)

def gen_list_from_csv(num=10):
    csv_path = '/mnt/nas2/users/tong.feng/kuwo/20240130/manifest/dataloader_info.csv'
    song_list = []
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)    # skip the header
        for i in range(num):
            path = next(reader)[1]
            if '242275546' in path:
                continue
            song_list.append(path)
    return song_list

if __name__ == '__main__':
    # mp.set_start_method('spawn') # This is important and MUST be inside the name==main block.
    tmp.set_start_method('spawn')

    # audio_list = ['/mnt/nas1/users/tianwei.zhao/music/4.Time after time ～花舞う街で～（theater version）.mp3']
    # audio_list = get_file_list('/mnt/workspace/spotify/audio')
    # audio_list = get_file_list('/mnt/workspace/users/tianwei.zhao/music')
    # profile.run('test_continous_running_sequential(audio_list, 5)')
    # test_continous_running_sequential(audio_list, 10)
    # test_continous_running_parallel(audio_list)

    num_files_to_process = 10
    # audio_list = gen_list_from_csv(num_files_to_process)

    # test_spotify(audio_list)
    # test_continous_running_sequential(audio_list, num_files_to_process)
    # cProfile.run("test_spotify(audio_list)", "profile_res.prof")
    # test_continous_running_sequential_demucs(audio_list, num_files_to_process)

