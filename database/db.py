import sqlite3 as sql

class Dbase:
    def __init__(self):
        self.vt=sql.connect("mails.sqlite")
        self.im=self.vt.cursor()
        self.im.execute("CREATE TABLE IF NOT EXISTS avaible ('mail')")
        self.im.execute("CREATE TABLE IF NOT EXISTS nonavaible ('mail')")
    def addAvaible(self,val):
        self.im.execute("INSERT INTO avaible VALUES ('%s')" %val)
    def addNonAvaible(self,val):
        self.im.execute("INSERT INTO nonavaible VALUES ('%s')" %val)
    def getValues(self,choise="avaible"):
        self.im.execute('SELECT * FROM %s' %choise)