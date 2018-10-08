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
textbox = QLineEdit(etiket)
textbox.move(0,225)
textbox1 = QLineEdit(etiket1)
textbox1.move(0,225)
textbox2 = QLineEdit(etiket2)
textbox2.move(0,225)
textbox3 = QLineEdit(etiket3)
textbox3.move(0,225)
yatayKutu=QHBoxLayout()
yatayKutu.addWidget(etiket)
yatayKutu.addWidget(etiket1)
yatayKutu.addWidget(etiket2)
yatayKutu.addWidget(etiket3)
yatayKutu.addWidget(buton)
pencere.setLayout(yatayKutu)
pencere.resize(800,300)


pencere.show()
uyg.exec_
