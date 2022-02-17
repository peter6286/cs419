import sqlite3
import auth

conn = sqlite3.connect('cs419.db')

def create():
    auth.createtable()


def adduser():
    auth.adduser('peter', '1234')
    auth.adduser('muggle', '1234')
    auth.adduser('jack', '1234')
    auth.adduser('alex', '5678')
    auth.adduser('bob', 'dsaf')
    auth.adduser('li', 'asd')

def secur():
    print(auth.authenticate('peter', '1234'))
    print(auth.authenticate('muggle', '1234'))
    print(auth.authenticate('mu', '1234'))
    print(auth.authenticate('bob', 'dfef'))
    print(auth.authenticate('li', 'asd'))

def setdomain():
    auth.setDomain('muggle', 'fucker')
    auth.setDomain('muggle', 'lover')
    auth.setDomain('peter', 'fucker')
    #main.select('muggle','peter')
    #main.setDomain('fingal','dwq')
    #main.setDomain('alex','lover')
    auth.setDomain('bob', 'lover')
    auth.setDomain('bob', 'lover')

def doinfo():
    print(auth.DomainInfo('fucker'))
    print(auth.DomainInfo('lover'))
    print(auth.DomainInfo('as'))

def settype():
    auth.SetType('pornhub', 'video')
    auth.SetType('wo.txt', 'document')
    auth.SetType('cs419', 'document')
    auth.SetType('cs352', 'document')
    auth.SetType('movei', 'video')
    auth.SetType('hhh', 'funny')
    auth.SetType('cs520', 'document')
    auth.SetType('football', 'sport')

def tyinfo():
    print(auth.Typeinfo('video'))
    print(auth.Typeinfo('document'))

def setaccess():
    auth.addaccess('read', 'fucker', 'document')
    auth.addaccess('watch', 'fucker', 'video')
    auth.addaccess('doing', 'fucker', 'sport')
    auth.addaccess('read', 'lover', 'document')

def checkaccess():
    print(auth.canaccess('watch', 'peter', 'pornhub'))
    print(auth.canaccess('doing', 'muggle', 'football'))



#adduser()
print("-----------")
#secur()
print("-----------")
#setdomain()
print("-----------")
#doinfo()
print("-----------")
#print(main.canaccess('rival', 'france', 'usa'))
#settype()
print("-----------")
#tyinfo()
#setaccess()
#conn.close()