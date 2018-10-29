from PyQt4.QtCore import *
from PyQt4.QtGui import *

class devirHizi(QDialog):
    def __init__(self,ebeveyn=None):
        super(devirHizi,self).__init__(ebeveyn)
        grid=QGridLayout()

        grid.addWidget(QLabel("İşten ayrılan personel:"),0,0)
        self.ayrilanPer=QLineEdit()
        grid.addWidget(self.ayrilanPer,0,1)

        grid.addWidget(QLabel("Aylık çalışan:"),1,0)
        self.aylikCal=QLineEdit()
        grid.addWidget(self.aylikCal,1,1)
        
        grid.addWidget(QLabel("Hesaplanacak ay:"),2,0)
        self.ay=QLineEdit()
        grid.addWidget(self.ay,2,1)

        grid.addWidget(QLabel("Sonuç:"),3,0)
        self.sonuc=QLabel("")
        grid.addWidget(self.sonuc,3,1)

        hesaplaDugme=QPushButton("Hesapla")
        grid.addWidget(hesaplaDugme,5,1)
        self.connect(hesaplaDugme,SIGNAL('pressed()'),self.hesapla)

        self.setLayout(grid)

        self.setWindowTitle("Personel Devir Hızı")
        self.resize(250,150)


        
    def hesapla(self):
        ap=int(self.ayrilanPer.text())
        aylik=int(self.aylikCal.text())
        hesAy=int(self.ay.text())
        son=(ap/(aylik/hesAy))*100
        
        self.sonuc.setText('<font color="purple"><b>%0.1f</b></font>'%son)

        

uygulama=QApplication([])
pencere=devirHizi()
pencere.show()
uygulama.exec_

