import os
import sqlite3
import sys


conn = sqlite3.connect('cs419.db')

def createtable():
    c0 = conn.cursor()
    c1 = conn.cursor()
    c2 = conn.cursor()


    c0.execute('''CREATE TABLE IF NOT EXISTS USER
    (USER_NAME    TEXT  PRIMARY KEY   NOT NULL,
    password      TEXT     NOT NULL,
    domain        CHAR(50));''')

    c1.execute('''CREATE TABLE IF NOT EXISTS OBJECTS
        (objectname  TEXT NOT NULL,
        type         TEXT NOT NULL  );''')

    c2.execute('''CREATE TABLE IF NOT EXISTS ACCESS
           (operationname  TEXT NOT NULL,
            domainname  TEXT NOT NULL ,
            typename    TEXT NOT NULL);''')

    conn.commit()

def adduser(user,password):
    c = conn.cursor()
    list1 = [user,password,'NULL']
    try:
        c.execute("INSERT INTO USER (USER_NAME,password,domain) \
                        VALUES (?,?,?)",list1)
    except sqlite3.IntegrityError as err:
          exit ("user name already exist")

    conn.commit()
    return ("Success in adding user")


def authenticate(user,password):
    c = conn.cursor()
    c1 = conn.cursor()
    cursor = c.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [user])
    cursor1 = c1.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [user])
    if len(list(cursor1)) == 0:
        exit("Error: No such user")
    for row in cursor:
        if row[0] == user:
            if row[1] != password:
                exit("Error: Bad password")
            else:
                conn.commit()
                return("Success in authenticate")

def setDomain(name,domain):
    c = conn.cursor()
    c1 = conn.cursor()
    cursor1 = c1.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [name])
    cursor = c.execute("SELECT distinct USER_NAME, password, domain from USER where USER_NAME = ?;", [name])

    if len(list(cursor1)) == 0:
        exit("Error: No such user")

    for row in cursor:
        if row[2] == 'NULL':
            c.execute("UPDATE USER set domain = ? where USER_NAME = ?", [domain, name])
        else:
            c.execute("UPDATE USER set domain = domain || ? where USER_NAME = ?", ["," + domain, name])

    conn.commit()
    return ("Success in setting the domain")


def select(name1,name2):
    c = conn.cursor()
    cursor = c.execute("SELECT USER_NAME ,password,domain from USER where USER_NAME = ? or USER_NAME = ? ;",[name1,name2] )
    for row in cursor:
        print("USER_NAME = ", row[0])
        print("password = ", row[1])
        print("domian = ",row[2])

        #print("数据操作成功")
        conn.commit()

def DomainInfo(domain):
    c = conn.cursor()
    dict = {}
    if domain == '':
        return 'Error: missing domain'
    cursor = c.execute("SELECT distinct domain,USER_NAME from USER ")
    for row in cursor:
        temp = str(row[0])      #domain
        domainlist = (temp.split(",")) #domain
        userlist = str(row[1])     # user name

        for item in domainlist:
            if item not in dict:
                dict[item] = [userlist]
            else:
                if userlist not in dict[item]:
                    dict[item].append(userlist)

    conn.commit()
    if domain not in dict:
        exit("NO such domain name")
    else:
        return (dict[domain])

def SetType(objectname,type):
    c = conn.cursor()
    if objectname == '' or type == '':
        exit ("Arguemnt missing")
    c.execute("INSERT INTO OBJECTS (objectname,type) \
             VALUES (?,?)",[objectname,type])
    conn.commit()
    return ("Success in setting type")

def Typeinfo(country):
    res = []
    c = conn.cursor()
    c1 = conn.cursor()
    cursor=c.execute("SELECT distinct objectname from OBJECTS where type = ?;",[country])
    cursor1 = c1.execute("SELECT objectname from OBJECTS where type = ?;", [country])
    if len(list(cursor1)) == 0:
        exit("Error: No such object name")

    for row in cursor:
        res.append(row[0])
    conn.commit()

    return res


def addaccess(operation,Dname,Tname):
    c = conn.cursor()
    c.execute("INSERT INTO ACCESS (operationname,domainname,typename) \
                 VALUES (?,?,?)", [operation, Dname,Tname])
    conn.commit()
    return ("Success in setting the access")


def canaccess(op,un,on):
    c0 = conn.cursor()
    c1 = conn.cursor()
    c2 = conn.cursor()

    cursor0 = c0.execute("select distinct domainname,typename from ACCESS where operationname = ? ;",[op])
    cursor1 = c1.execute("select domain from USER where USER_NAME = ? ;",[un])
    cursor2 = c2.execute("select distinct type from OBJECTS where objectname = ? ;", [on])
    #print(cursor1[0][0])
    for row in cursor1:
        temp = str(row[0])  # domain
    domianlist = (temp.split(","))  # domain
    #print(list1)

    typelist = []
    for row in cursor2:
        #print("type = ", row[0])
        typelist.append(row[0])

    #print(domianlist)
    #print(typelist)
    for row in cursor0:
        #print("domainname = ", str(row[0]))
        #print("typename = ", str(row[1]))
        t1 = row[0]
        t2 = row[1]
        if (t1 in domianlist)&(t2 in typelist):
                conn.commit()
                return ("can access")
    conn.commit()
    return ("can not access")


def execute(args):

    args_passed = len(args)
    if args_passed < 2:
        return ("please look up the command info")

    else:
        base_cmd = args[1].lower()

        if base_cmd == 'adduser':
            if args_passed != 4:
                return ' Input argument adduser user password'

            return adduser(args[2], args[3])

        elif base_cmd == 'authenticate':
            if args_passed != 4:
                return 'Input argument Authenticate user password'

            return authenticate(args[2], args[3])

        elif base_cmd == 'setdomain':
            if args_passed != 4:
                return 'Input argument SetDomain user domain'

            return setDomain(args[2], args[3])

        elif base_cmd == 'domainfo':
            if args_passed != 3:
                return 'Input argument DomainInfo domain'
            ans = DomainInfo(args[2])
            for item in ans:
                print(item)

        #return DomainInfo(args[2])

        elif base_cmd == 'settype':
            if args_passed != 4:
                return 'Input argument SetType object type'

            return SetType(args[2], args[3])

        elif base_cmd == 'typeinfo':
            if args_passed != 3:
                return 'Input argument TypeInfo type'

            ans = Typeinfo(args[2])
            for item in ans:
                print(item)

        #return Typeinfo(args[2])

        elif base_cmd == 'addaccess':
            if args_passed != 5:
                return 'Input argument operation domain type'

            return addaccess(args[2], args[3], args[4])

        elif base_cmd == 'canaccess':
            if args_passed != 5:
                return 'Input argument CanAccess operation user object'

            return canaccess(args[2], args[3], args[4])

        else:
            return "make sure the command is correct"


def main():
    if sys.version_info < (3, 0):
        print('Please make sure you are using Python 3.')
        return
    createtable()
    print(execute(sys.argv))


if __name__ == '__main__':  # pragma: no cover
    main()

#conn.close()