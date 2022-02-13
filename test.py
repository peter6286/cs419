import sqlite3
import main

conn = sqlite3.connect('wo.db')

def create():
    main.createtable()


def adduser():
    main.insert('peter','1234')
    main.insert('muggle','1234')
    main.insert('jack','1234')
    main.insert('alex','5678')
    main.insert('bob','dsaf')
    main.insert('li','asd')

def secur():
    print(main.authenticate('peter','1234'))
    print(main.authenticate('muggle','1234'))
    print(main.authenticate('mu','1234'))
    print(main.authenticate('bob','dfef'))
    print(main.authenticate('li','asd'))

def setdomain():
    main.setDomain('muggle','fucker')
    main.setDomain('muggle','lover')
    main.setDomain('peter','fucker')
    #main.select('muggle','peter')
    #main.setDomain('fingal','dwq')
    #main.setDomain('alex','lover')
    main.setDomain('bob','lover')
    main.setDomain('bob','lover')

def doinfo():
    print(main.DomainInfo('fucker'))
    print(main.DomainInfo('lover'))
    print(main.DomainInfo('as'))

def settype():
    main.SetType('pornhub','video')
    main.SetType('wo.txt','document')
    main.SetType('cs419','document')
    main.SetType('cs352','document')
    main.SetType('movei','video')
    main.SetType('hhh','funny')
    main.SetType('cs520','document')
    main.SetType('football','sport')

def tyinfo():
    print(main.Typeinfo('video'))
    print(main.Typeinfo('document'))

def setaccess():
    main.addaccess('read','fucker','document')
    main.addaccess('watch','fucker','video')
    main.addaccess('doing','fucker','sport')
    main.addaccess('read','lover','document')

def checkaccess():
    main.canaccess('watch','peter','pornhub')


#create()
print("-----------")
#adduser()
print("-----------")
#secur()
print("-----------")
#setdomain()
print("-----------")
#doinfo()
print("-----------")
#print(main.canaccess('rival', 'france', 'usa'))
settype()
print("-----------")
tyinfo()
setaccess()
conn.close()