import binascii
import nfc
import signal

class FelicaCardReader(object):

    def on_connect(self, tag):
        self.idm = binascii.hexlify(tag.idm)
        return True

    def read_idm(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr = {'on-connect':self.on_connect})
        finally:
            clf.close()

def spreadsheet_output(idm):
    import requests
    import os

    url = os.environ['FELICA_GOOGLE_SPREADSHEET_URL']
    requests.get(url + '?data1=' + idm)
    return True

if __name__ == '__main__':
    read_card = FelicaCardReader()
    while True:
        print('カードをタッチしてください')
        read_card.read_idm()
        print("カードのID: ",end='')
        idm = str(read_card.idm)[1:18]
        print(idm[1:17])
        if spreadsheet_output(idm):
            print('スプレッドシートに書き込みました')
        else:
            print('書き込みに失敗しました')

        signal.signal(signal.SIGINT,signal.SIG_DFL)
