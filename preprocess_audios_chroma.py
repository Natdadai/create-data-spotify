import multiprocessing
import numpy as np
from functools import partial
from tqdm import tqdm
import librosa

def load_chroma_features(audio_file,sr,offset,duration,n_fft,n_chroma,hop_length,max_length):
    # Load audio file
    y, sr = librosa.load(audio_file, sr=sr,mono=True,offset=offset, duration=duration)

    # Extract chroma features
    chroma = librosa.feature.chroma_stft(y=y, sr=sr, n_fft=n_fft, n_chroma=n_chroma, hop_length=hop_length)

    if max_length > 0:
        if chroma.shape[1] < max_length:
            chroma = np.pad(chroma, pad_width=((0, 0), (0, max_length - chroma.shape[1])), mode='constant')
        else:
            chroma = chroma[:, :max_length]

    return chroma

def preprocess_audios_chroma(audio_files,num_processes,sr,offset,duration,n_fft,n_chroma,hop_length,max_length):
    pool = multiprocessing.Pool(num_processes)
    func = partial(load_chroma_features,sr=sr,offset=offset,duration=duration,
                                  n_fft = n_fft, n_chroma=n_chroma, hop_length = hop_length,
                                  max_length=max_length)
    
    features = []
    with tqdm(total=len(audio_files)) as pbar:
        for chroma in pool.imap(func, audio_files):
            features.append(chroma)
            pbar.update(1)
            
    pool.close()
    pool.join()
    return features