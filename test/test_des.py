#!/usr/bin/env python

import unittest

def bin2hex(bins):
    return (''.join( [ "%02X" % ord( x ) for x in bins ] ).strip())

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
        

if __name__ == '__main__':
    unittest.main()
