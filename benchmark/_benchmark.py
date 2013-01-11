#!/usr/bin/env python

import sys

def bin2hex(bins):
    return (''.join( [ "%02X" % ord( x ) for x in bins ] ).strip())

class Tester():
    def __init__(self):
        self._test_txt = 'test_phone.txt'
        self._key = '_abcdef_'
        self._ivec = self._key
        with open(self._test_txt) as f:
            for line in f:
                pass

    def _get_phones(self):
        with open(self._test_txt) as f:
            for line in f:
                phone = line.strip()
                yield phone

    def test_openssl_des(self):
        import ctypes_des
        #keys = des.set_key(self._key)

        for phone in self._get_phones():
            print ctypes_des.des_encrypt(phone, self._key, self._ivec)

    def test_openssl_des_fast(self):
        import ctypes_des
        keys = ctypes_des.set_key(self._key)

        for phone in self._get_phones():
            print ctypes_des._des_encrypt(phone, keys, self._ivec)


    def test_my_des(self):
        import mydes
        for phone in self._get_phones():
            print mydes.my_des_encrypt(phone, self._key, self._ivec)

    def test_pydes(self):
        import pyDes
        k = pyDes.des(self._key, pyDes.CBC, self._ivec, pad=None, padmode=pyDes.PAD_PKCS5)
        for phone in self._get_phones():
            print bin2hex(k.encrypt(phone))

        
        

def main():

    tester = Tester()
    name = sys.argv[1]

    funcname = 'test_%s' % (name)
    func = getattr(tester, funcname)

    func()
    


if __name__ == '__main__':
    main()
