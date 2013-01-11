#!/usr/bin/env python

import unittest

def bin2hex(bins):
    return (''.join( [ "%02X" % ord( x ) for x in bins ] ).strip())


def hex2bin(hexStr):
    bytes = []
    hexStr = ''.join(hexStr.split(" "))
    for i in xrange(0, len(hexStr), 2):
        bytes.append(chr(int(hexStr[i:i+2], 16)))
    return ''.join(bytes)

class TestDES(unittest.TestCase):
    def test_des_encrypt(self):
        import pyDes
        key = '_abcdef_'
        ivec = key
        sinput = 'testtes'

        k = pyDes.des(key, pyDes.CBC, ivec, pad=None, padmode=pyDes.PAD_PKCS5)
        expected = bin2hex(k.encrypt(sinput))

        from ctypes_des import des_encrypt
        real = des_encrypt(sinput, key, ivec)

        self.assertEqual(real, expected)
        
    def test_des_decrypt(self):
        import pyDes
        key = '_abcdef_'
        ivec = key
        sinput = 'testtes'

        k = pyDes.des(key, pyDes.CBC, ivec, pad=None, padmode=pyDes.PAD_PKCS5)
        hexs = bin2hex(k.encrypt(sinput))
        expected = k.decrypt(hex2bin(hexs))

        from ctypes_des import des_decrypt
        real = des_decrypt(hex2bin(hexs), key, ivec)

        self.assertEqual(real, expected)

    


if __name__ == '__main__':
    unittest.main()
