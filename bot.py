from PyQt5.QtWidgets import QApplication, QWidget
from mailchecker.MailChecker import MailChecker
import sys
from gui.App import App
from database.db import Dbase

if __name__ == "__main__":
    # app=QApplication(sys.argv)
    # ex=App()
    # sys.exit(app.exec_())
    vt= Dbase()
    mc=MailChecker()
    # print(vt.getValues("nonavaible"))
    # print(vt.getValues("avaible"))
    mc.check("ozgurkrcm")