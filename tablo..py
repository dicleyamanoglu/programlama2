import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
data = {'Adı':['Can','Semih','Büşra'],'Soyadı':['Aydın','Yarar','Demirgüreşçi'],'bölümü':['Ybs','Ybs','İktisat']}
 
class tablo(QTableWidget):
    
    def __init__(self,data,*args):
        super(tablo, self).__init__()
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
    def setmydata(self):
 
        header = []
        for n, key in enumerate(sorted(self.data.keys())):
            header.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(header)
        self.setWindowTitle("Tablo Örneği")
          
def main(args):
    app = QApplication(args)
    table = tablo(data, 3, 3)
    table.show()
    sys.exit(app.exec_())
 
if __name__=="__main__":
    main(sys.argv)
