""" Probables Hashing library """

import typing
from functools import wraps
from hashlib import md5, sha256
from struct import unpack

from .constants import UINT64_T_MAX

KeyT = typing.Union[str, bytes]
SimpleHashT = typing.Callable[[KeyT, int], int]
HashResultsT = typing.List[int]
HashFuncT = typing.Callable[[KeyT, int], HashResultsT]
HashFuncBytesT = typing.Callable[[KeyT, int], bytes]


def hash_with_depth_bytes(func: HashFuncBytesT) -> HashFuncT:
    """Decorator to turns a function taking a single key and hashes it to
    bytes. Wraps functions to be used in Bloom filters and Count-Min sketch
    data structures.

    Args:
        key (str): The element to be hashed
        depth (int): The number of hash permutations to compute
    Returns:
        list(int): 64-bit hashed representation of key
    Note:
        Arguments shown are as it will be after decorated"""

    @wraps(func)
    def hashing_func(key, depth=1):
        """wrapper function"""
        res = list()
        tmp = key
        if isinstance(key, str):
            tmp = key.encode("utf-8")
        for idx in range(depth):
            tmp = func(tmp, idx)
            res.append(unpack("Q", tmp[:8])[0])  # turn into 64 bit number
        return res

    return hashing_func


def hash_with_depth_int(func: HashFuncT) -> HashFuncT:
    """Decorator to turn a function that takes a single key and hashes it to
    an int. Wraps functions to be used in Bloom filters and Count-Min
    sketch data structures.

    Args:
        key (str): The element to be hashed
        depth (int): The number of hash permutations to compute
    Returns:
        list(int): 64-bit hashed representation of key
    Note:
        Arguments shown are as it will be after decorated"""

    @wraps(func)
    def hashing_func(key, depth=1):
        """wrapper function"""
        res = list()
        tmp = func(key, 0)
        res.append(tmp)
        for idx in range(1, depth):
            tmp = func("{0:x}".format(tmp), idx)
            res.append(tmp)
        return res

    return hashing_func


def default_fnv_1a(key: KeyT, depth: int = 1) -> typing.List[int]:
    """The default fnv-1a hashing routine

    Args:
        key (str): The element to be hashed
        depth (int): The number of hash permutations to compute
    Returns:
        list(int): List of size depth hashes"""

    res = list()
    for idx in range(depth):
        res.append(fnv_1a(key, idx))
    return res


def fnv_1a(key: KeyT, seed: int = 0) -> int:
    """Pure python implementation of the 64 bit fnv-1a hash

    Args:
        key (str): The element to be hashed
        seed (int): Add a seed to the initial starting point (0 means no seed)
    Returns:
        int: 64-bit hashed representation of key
    Note:
        Uses the lower 64 bits when overflows occur"""
    max64mod = UINT64_T_MAX + 1
    hval = (14695981039346656037 + (31 * seed)) % max64mod
    fnv_64_prime = 1099511628211
    if isinstance(key, str):
        tmp = list(map(ord, key))
    else:
        tmp = list(key)
    for t_str in tmp:
        hval ^= t_str
        hval *= fnv_64_prime
        hval %= max64mod
    return hval


@hash_with_depth_bytes
def default_md5(key: KeyT, seed: int = 0) -> bytes:
    """The default md5 hashing routine

    Args:
        key (str): The element to be hashed
        depth (int): The number of hash permutations to compute
    Returns:
        list(int): List of 64-bit hashed representation of key hashes
    Note:
        Returns the upper-most 64 bits"""
    if isinstance(key, str):
        return md5(key.encode()).digest()
    return md5(key).digest()


@hash_with_depth_bytes
def default_sha256(key: KeyT, seed: int = 0) -> bytes:
    """The default sha256 hashing routine

    Args:
        key (str): The element to be hashed
        depth (int): The number of hash permutations to compute
    Returns:
        list(int): List of 64-bit hashed representation of key hashes
    Note:
        Returns the upper-most 64 bits"""
    if isinstance(key, str):
        return sha256(key.encode()).digest()
    return sha256(key).digest()
