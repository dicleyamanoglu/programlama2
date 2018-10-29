from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys
 
def tablo():  
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    tableItem 	= QTableWidgetItem()
 
    # initiate table
    table.setWindowTitle("Kişi Listesi")
    table.resize(350,150)
    table.setRowCount(3)
    table.setColumnCount(3)
 
    # set label
    table.setHorizontalHeaderLabels(("Adı;Soyadı;Bölüm;").split(";"))
    table.setVerticalHeaderLabels(("1;2;3;").split(";"))
 
    # set data
    table.setItem(0,0, QTableWidgetItem("Can"))
    table.setItem(0,1, QTableWidgetItem("Aydın"))
    table.setItem(0,2, QTableWidgetItem("Ybs"))
    table.setItem(1,0, QTableWidgetItem("Semih"))
    table.setItem(1,1, QTableWidgetItem("Yarar"))
    table.setItem(1,2, QTableWidgetItem("Ybs"))
    table.setItem(2,0, QTableWidgetItem("Büşra"))
    table.setItem(2,1, QTableWidgetItem("Demirgüreşçi"))
    table.setItem(2,2, QTableWidgetItem("İktisat"))
    
 
    # show table
    table.show()
    return app.exec_()
 
if __name__ == '__main__':
    tablo()
