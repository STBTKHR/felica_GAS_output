import nfc
import binascii

def conncted(tag):
    idm = binascii.hexlify(tag.idm)
    print(idm)
    return False

clf = nfc.ContactlessFrontend('usb')
tag = clf.connect(rdwr = {'on-connect': conncted})
clf.close()