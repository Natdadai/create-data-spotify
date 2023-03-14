import multiprocessing
import numpy as np
from functools import partial
from tqdm import tqdm
import librosa

def preprocess_audio_mfcc(audio_file,sr,offset,duration,n_mfcc,n_fft,hop_length,max_length):
    # Load audio file
    audio, sr = librosa.load(audio_file, sr=sr,mono=True,offset=offset, duration=duration)
    
    # Convert audio to MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc,n_fft=n_fft,hop_length=hop_length)
    
    # Pad or truncate MFCC to a fixed length
    if max_length > 0:
        if mfcc.shape[1] < max_length:
            mfcc = np.pad(mfcc, pad_width=((0, 0), (0, max_length - mfcc.shape[1])), mode='constant')
        else:
            mfcc = mfcc[:, :max_length]

    return mfcc

def preprocess_audios_mfcc(audio_files,num_processes,sr,offset,duration,n_mfcc,n_fft,hop_length,max_length):
    pool = multiprocessing.Pool(num_processes)
    func = partial(preprocess_audio_mfcc,sr=sr,offset=offset,duration=duration,n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length,max_length=max_length)
    
    mfccs = []
    with tqdm(total=len(audio_files)) as pbar:
        for mfcc in pool.imap(func, audio_files):
            mfccs.append(mfcc)
            pbar.update(1)
            
    pool.close()
    pool.join()
    return mfccs