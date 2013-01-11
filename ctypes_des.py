#!/usr/bin/env python

from ctypes import *
import ctypes
import ctypes.util
import os


path_ossl = ctypes.util.find_library('ssl')
libssl = cdll.LoadLibrary(path_ossl)

    
class _union_keys(Union):
    _fields_ = [
        ("cblock", c_char * 8),
        ("deslong", c_long * 2),
    ]

class DES_key_schedule(Structure):
    _fields_ = [
        ("ks", _union_keys * 16)
    ]


libssl.DES_set_key.argtypes = [c_char_p, c_void_p]
libssl.DES_set_key.restype = c_int

libssl.DES_ncbc_encrypt.argtypes = [c_char_p, c_char_p, c_int, c_void_p, c_char_p, c_int]
libssl.DES_ncbc_encrypt.restype = None

DES_DECRYPT = 0
DES_ENCRYPT = 1

def set_key(key):
    keys = DES_key_schedule()
    assert len(key) == 8
    ptr_key = create_string_buffer(key)

    libssl.DES_set_key(ptr_key, addressof(keys))
    return keys

    

def _des_encrypt(input, keys, ivec):

    ptr_output = create_string_buffer(4096)
    ptr_ivec = create_string_buffer(ivec)

    pad_len = 8 - (len(input) % 8)
    input += pad_len * chr(pad_len)

    libssl.DES_ncbc_encrypt(input, ptr_output, len(input), addressof(keys), ptr_ivec, DES_ENCRYPT)
    output = ptr_output.raw
    hexoutput = (''.join( [ "%02X" % ord( x ) for x in output if ord(x) != 0 ] ).strip())
    
    return hexoutput

def _des_decrypt(input, keys, ivec):
    ptr_output = create_string_buffer(4096)
    ptr_ivec = create_string_buffer(ivec)

    libssl.DES_ncbc_encrypt(input, ptr_output, len(input), addressof(keys), ptr_ivec, DES_DECRYPT)
    output = ptr_output.value

    pad_len = ord(output[-1])
    output = output[:len(output) - pad_len]
    
    return output


GLOBAL_KEYS = None
GLOBAL_KEY = None

def des_encrypt(input, key, ivec):
    global GLOBAL_KEY, GLOBAL_KEYS
    if key != GLOBAL_KEY:
        GLOBAL_KEY = key
        GLOBAL_KEYS = set_key(key)

    return _des_encrypt(input, GLOBAL_KEYS, ivec)

def des_decrypt(input, key, ivec):
    global GLOBAL_KEY, GLOBAL_KEYS
    if key != GLOBAL_KEY:
        GLOBAL_KEY = key
        GLOBAL_KEYS = set_key(key)

    return _des_decrypt(input, GLOBAL_KEYS, ivec)



def main():
    print des_encrypt('testtes', '_abcdef_', '_abcdef_')
    print des_encrypt('testtes', '_abcdef_', '_abcdef_')

    pass

if __name__ == '__main__':
    main()
