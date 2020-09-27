import nfc
import binascii
import requests


def conncted(tag):
    url = 'https://script.google.com/macros/s/AKfycbxDF8RfY1wELzum7kjy-W1qBL98jAxen59CGQk92-bw_YPka9E/exec?data1='
    idm = binascii.hexlify(tag.idm)
    print(idm)
    requests.get(url + str(idm)[2:18])
    return False

clf = nfc.ContactlessFrontend('usb')
while True:
    tag = clf.connect(rdwr = {'on-connect': conncted})
    if input() == 'exit':
        break
clf.close()