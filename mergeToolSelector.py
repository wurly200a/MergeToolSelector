import sys,subprocess,re
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication

class MergeToolSelector(QMainWindow):
    base    = ""
    theirs  = ""
    mine    = ""
    merged  = ""
    bname   = ""
    tname   = ""
    yname   = ""
    mname   = ""

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.displayArgv()

        btn1 = QPushButton('P4Merge', self)
        btn1.move(30, 120)

        btn2 = QPushButton('Emacs', self)
        btn2.move(150, 120)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusbar = self.statusBar()
        self.resize(320, 240)
        self.setWindowTitle('MergeToolSelector')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

        if sender.text() == 'P4Merge':
            string = 'C:\Program Files\Perforce\p4merge.exe ' + '-nb "' + self.bname + '" -nl "' + self.tname + '" -nr "' + self.yname + '" -nm "' + self.mname + '" "' + self.base + '" "' + self.theirs + '" "' + self.mine + '" "' + self.merged + '"'
        elif sender.text() == 'Emacs':
            regex = re.compile(r'\\')
            self.base   = regex.sub('\\\\\\\\',self.base  )
            self.theirs = regex.sub('\\\\\\\\',self.theirs)
            self.mine   = regex.sub('\\\\\\\\',self.mine  )
            self.merged = regex.sub('\\\\\\\\',self.merged)
            self.bname  = regex.sub('\\\\\\\\',self.bname )
            self.tname  = regex.sub('\\\\\\\\',self.tname )
            self.yname  = regex.sub('\\\\\\\\',self.yname )
            self.mname  = regex.sub('\\\\\\\\',self.mname )

            string = 'C:\\usr\\emacs\\bin\\runemacs '
#            string += '-q --load %HOME%\.emacs '
            string += '--eval "(setq my-merge-mode t)" --eval "(require \'ediff)" --eval "(setq ediff-window-setup-function \'ediff-setup-windows-plain)" '
            string += '--eval "(ediff-merge-with-ancestor ' + '\\"' + self.mine + '\\" \\"' + self.theirs + '\\" \\"' + self.base + '\\" ' + 'nil' + ' \\"' + self.merged + '\\")"'

        print(string)
        subprocess.Popen(string)

    def displayArgv(self):
        self.base   = sys.argv[1]
        self.theirs = sys.argv[2]
        self.mine   = sys.argv[3]
        self.merged = sys.argv[4]
        self.bname  = sys.argv[5]
        self.tname  = sys.argv[6]
        self.yname  = sys.argv[7]
        self.mname  = sys.argv[8]

        y = 0
        y += 10
        lbl1 = QLabel("base    : " + self.base, self)
        lbl1.move(15, y)
        lbl1.adjustSize()

        y += 10
        lbl1 = QLabel("theirs  : " + self.theirs, self)
        lbl1.move(15, y)
        lbl1.adjustSize()

        y += 10
        lbl1 = QLabel("mine    : " + self.mine  , self)
        lbl1.move(15, y)
        lbl1.adjustSize()

        y += 10
        lbl1 = QLabel("merged  : " + self.merged, self)
        lbl1.move(15, y)
        lbl1.adjustSize()

        y += 10
        lbl1 = QLabel("bname   : " + self.bname , self)
        lbl1.move(15, y)
        lbl1.adjustSize()

        y += 10
        lbl1 = QLabel("tname   : " + self.tname , self)
        lbl1.move(15, y)
        lbl1.adjustSize()

        y += 10
        lbl1 = QLabel("yname   : " + self.yname , self)
        lbl1.move(15, y)
        lbl1.adjustSize()

        y += 10
        lbl1 = QLabel("mname   : " + self.mname , self)
        lbl1.move(15, y)
        lbl1.adjustSize()

def main():

    app = QApplication(sys.argv)
    mw = MergeToolSelector()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

