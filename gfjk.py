import sys
from PyQt4.QtGui import *

uyg=QApplication(sys.argv)
pencere=QWidget()
pencere.setWindowTitle("Yakıt Hesapla")

etiket=QLabel('<font color="blue" size="+2">Gideceğiniz Yol </font>')
etiket1=QLabel('<font color="blue" size="+2">Yakıtın Litre Fiyatı</font>')
etiket2=QLabel('<font color="blue" size="+2">100 kmde Tük.Yakıt</font>')
etiket3=QLabel('<font color="blue" size="+2">Toplam Tutar</font>')
buton=QPushButton("Hesapla")
textbox = QLineEdit()
textbox1 = QLineEdit()
textbox2 = QLineEdit()
textbox3 = QLineEdit()

yatayKutu=QGridLayout()
yatayKutu.addWidget(etiket,0,0)
yatayKutu.addWidget(etiket1,1,0)
yatayKutu.addWidget(etiket2,2,0)
yatayKutu.addWidget(etiket3,3,0)
yatayKutu.addWidget(buton,5,0,2,0)
yatayKutu.addWidget(textbox,0,1)
yatayKutu.addWidget(textbox1,1,1)
yatayKutu.addWidget(textbox2,2,1)
yatayKutu.addWidget(textbox3,3,1)
pencere.setLayout(yatayKutu)
pencere.resize(250,250)


pencere.show()
uyg.exec_
