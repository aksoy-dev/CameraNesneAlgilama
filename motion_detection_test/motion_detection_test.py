import cv2
from datetime import datetime


def farkImaj(t0, t1, t2):  # 3 zaman karşılaştırması
    fark1 = cv2.absdiff(t2, t1)  # mutlak olarak ikisinin farkı
    fark2 = cv2.absdiff(t1, t0)  #
    return cv2.bitwise_and(fark1,
                           fark2)  # bitsel olarak 3 zaman aralığındaki resmin and: 1,1 olması durumunda 1 döner piksel farklarına gore


esik_deger = 140000  # guvenlik kamerasının oranına gore x3 diye hesap yapabiliriz ,web cam yakında oldugu için
# daha dikkatli goruntu almak için ufak değişimler yapılabilir
kamera = cv2.VideoCapture(0)

pencereIsmi = "Hareket Algilayici"
cv2.namedWindow(pencereIsmi)

t_eksi = cv2.cvtColor(kamera.read()[1], cv2.COLOR_BGR2GRAY)  # resimlerin farkını gri tonlama ile yapacağız
t = cv2.cvtColor(kamera.read()[1], cv2.COLOR_BGR2GRAY)  # ilk resimlerinin başlangıç hallerini gri tonla alıyoruz
t_arti = cv2.cvtColor(kamera.read()[1], cv2.COLOR_BGR2GRAY)

zamanKontrol = datetime.now().strftime(
    '%Ss') 
# her saniye max bir fotograf alsın
while True:
    cv2.imshow(pencereIsmi, kamera.read()[1])  # surekli pencereyi goster
    if cv2.countNonZero(farkImaj(t_eksi, t, t_arti)) > esik_deger and zamanKontrol != datetime.now().strftime('%Ss'):
                              # 3 resmin farkı sıfır değilse işlem yap
        fark_resim = kamera.read()[1]  # zaman kontrol eşit değilse aynı saniyede birden fazla fotograf çekmeyi önler
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', fark_resim) #su anki bilgiyi alıyoruz string formatta yıl ,ay,gün,saat,dakika ve saniye bilgisini alıyoruz
    zamanKontrol = datetime.now().strftime('%Ss')  #saniye olarak
    t_eksi = t
    t = t_arti
    t_arti = cv2.cvtColor(kamera.read()[1], cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(10)
    if key == 27:  #esc tuşu ile çıkış yap
        cv2.destroyWindow(pencereIsmi)
        break


"""import cv2
from datetime import datetime


def farkImaj(t0,t1,t2):
    fark1=cv2.absdiff(t2,t1)
    fark2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(fark1,fark2)
esik_deger=140000
kamera=cv2.VideoCapture(0)

pencereIsmi="Hareket Algilayici"
cv2.namedWindow(pencereIsmi)

t_eksi=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)

zamanKontrol=datetime.now().strftime('%Ss')

while True:
    cv2.imshow(pencereIsmi,kamera.read()[1])
    if cv2.countNonZero(farkImaj(t_eksi,t,t_arti))>esik_deger and zamanKontrol !=datetime.now().strftime('%Ss'):
        fark_resim=kamera.read()[1]
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f')+'.jpg',fark_resim)
    zamanKontrol = datetime.now().strftime('%Ss')
    t_eksi=t
    t=t_arti
    t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(10)
    if key==27:
        cv2.destroyWindow(pencereIsmi)
        break"""