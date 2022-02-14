import sqlite3
import sys

db = 'wo.db'

CMD_INFO = """Usage:
        portal AddUser <user> <password>
        portal Authenticate <user> <password>
        portal SetDomain <user> <domain>
        portal DomainInfo <domain>
        portal SetType <object> <type>
        portal TypeInfo <type>
        portal AddAccess <operation> <domain> <type>
        portal CanAccess <operation> <user> <object>
        portal Reset
        portal Help
        """
'''
def opendb(db):
    try:
        conn = sqlite3.connect('wo.db')
    except:

        conn = sqlite3.connect('wo.db')
conn = sqlite3.connect('wo.db')
print ("数据库打开成功")
'''

conn = sqlite3.connect('wo.db')
def createtable():
    # print()
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

    print("数据表创建成功")
    conn.commit()

def insert(user,password):
    c = conn.cursor()
    list1 = [user,password,'NULL']
    c.execute("INSERT INTO USER (USER_NAME,password,domain) \
             VALUES (?,?,?)",list1)

    conn.commit()
    print("数据插入成功")




def authenticate(user,password):
    c = conn.cursor()
    c1 = conn.cursor()
    cursor = c.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [user])
    cursor1 = c1.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [user])
    if len(list(cursor1)) == 0:
        return("Error: No such user")
    for row in cursor:
        if row[0] == user:
            if row[1] != password:
                return("Error: Bad password")
            else:
                conn.commit()
                return("Success")

def setDomain(name,domain):
    c = conn.cursor()
    c1 = conn.cursor()
    #c = conn.cursor()
    cursor1 = c1.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [name])
    cursor = c.execute("SELECT distinct USER_NAME, password, domain from USER where USER_NAME = ?;", [name])
    #cursor1 = c.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [name])
    if domain == '':
        exit("Error: missing domain")

    if len(list(cursor1)) == 0:
        exit("Error: No such user")

    for row in cursor:
        if row[2] == 'NULL':
            c.execute("UPDATE USER set domain = ? where USER_NAME = ?", [domain, name])
        else:
            c.execute("UPDATE USER set domain = domain || ? where USER_NAME = ?", ["," + domain, name])

    conn.commit()
    return ("Success")


    #if domain == 'NULL':
    #    c.execute("UPDATE USER set domain = ? where USER_NAME = ?", [domain, name])
    #if domain != 'NULL':
    #    c.execute("UPDATE USER set domain = domain || ? where USER_NAME = ?", [","+domain,name])





def select(name1,name2):
    c = conn.cursor()
    cursor = c.execute("SELECT USER_NAME ,password,domain from USER where USER_NAME = ? or USER_NAME = ? ;",[name1,name2] )
    #cursor = c.execute("SELECT USER_NAME ,password from USER")
    for row in cursor:
        #print("ID = ", row[0])
        print("USER_NAME = ", row[0])
        print("password = ", row[1])
        print("domian = ",row[2])
       # print("SALARY = ", row[3], "\n")

        print("数据操作成功")
        conn.commit()

def DomainInfo(domain):
    c = conn.cursor()
    c1 = conn.cursor()
    dict = {}
    #res = []
    if domain == '':
        return 'Error: missing domain'
    cursor = c.execute("SELECT distinct domain,USER_NAME from USER ")
    cursor1 = c1.execute("SELECT domain,USER_NAME from USER ")

    if len(list(cursor1)) == 0:
        exit("Error: No such domain")


    for row in cursor:
        temp = str(row[0])      #domain
        list1 = (temp.split(",")) #domain
        temp1 = str(row[1])     # user name
        #print(list1)
        for item in list1:
            #print(item)
            if item not in dict:
                #print(temp1)
                dict[item] = [temp1]
            else:
                if temp1 not in dict[item]:
                    dict[item].append(temp1)
    #print(dict['fucker'])
    '''
    for row in cursor:
        temp = str(row[0])
        list1 = (temp.split(","))
        #print(type(list1))
        for item in list1:
            if item in res:
                continue
            else:
                res.append(item)
    print(res)
    dict1 = dict.fromkeys(res)
    '''
    if domain not in dict:
        exit("NO such domian")
    else :
        return (dict[domain])
    conn.commit()
    #print(dict)

def SetType(objectname,type):
    c = conn.cursor()
    if objectname == '' or type == '':
        exit ("Arguemnt missing")
    c.execute("INSERT INTO OBJECTS (objectname,type) \
             VALUES (?,?)",[objectname,type])
    conn.commit()
    return ("Success")

def Typeinfo(country):
    res = []
    c = conn.cursor()
    c1 = conn.cursor()
    if country == '':
        exit("Arguemnt missing")
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
    if operation == '' or Dname == '' or Tname == '':
        exit ("Arguemnt missing")
    c.execute("INSERT INTO ACCESS (operationname,domainname,typename) \
                 VALUES (?,?,?)", [operation, Dname,Tname])
    conn.commit()
    return ("Success")


def canaccess(op,un,on):
    c0 = conn.cursor()
    c1 = conn.cursor()
    c2 = conn.cursor()
    if op == '' or un == '' or on == '':
        exit("Arguemnt missing")

    cursor0 = c0.execute("select distinct domainname,typename from ACCESS where operationname = ? ;",[op])
    cursor1 = c1.execute("select domain from USER where USER_NAME = ? ;",[un])
    cursor2 = c2.execute("select distinct type from OBJECTS where objectname = ? ;", [on])

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
        print("domainname = ", str(row[0]))
        print("typename = ", str(row[1]))
        t1 = row[0]
        t2 = row[1]
        if (t1 in domianlist)&(t2 in typelist):
                conn.commit()
                return "can access"
    conn.commit()
    return "can not access"
        #print("domainname = ", row[0])
        #print("typename = ", row[1])
        #temp1.append([row[0],row[1]])

def execute(args):
    args_passed = len(args)

    if args_passed < 2:
        return CMD_INFO

    base_cmd = args[1].lower()

    if base_cmd == 'adduser':
        if args_passed != 4:
            return 'Usage: portal AddUser <user> <password>'

        return insert(args[2], args[3])

    if base_cmd == 'authenticate':
        if args_passed != 4:
            return 'Usage: portal Authenticate <user> <password>'

        return authenticate(args[2], args[3])

    if base_cmd == 'setdomain':
        if args_passed != 4:
            return 'Usage: portal SetDomain <user> <domain>'

        return setDomain(args[2], args[3])

    if base_cmd == 'domaininfo':
        if args_passed != 3:
            return 'Usage: portal DomainInfo <domain>'

        return DomainInfo(args[2])

    if base_cmd == 'settype':
        if args_passed != 4:
            return 'Usage: portal SetType <object> <type>'

        return SetType(args[2], args[3])

    if base_cmd == 'typeinfo':
        if args_passed != 3:
            return 'Usage: portal TypeInfo <type>'

        return Typeinfo(args[2])

    if base_cmd == 'addaccess':
        if args_passed != 5:
            return 'Usage: AddAccess <operation> <domain> <type>'

        return addaccess(args[2], args[3], args[4])

    if base_cmd == 'canaccess':
        if args_passed != 5:
            return 'Usage: CanAccess <operation> <user> <object>'

        return canaccess(args[2], args[3], args[4])

    '''
        if base_cmd == 'reset':
            return self.reset()

        if base_cmd == 'help':
            return Portal.CMD_INFO

        # an invalid command was entered
        return Portal.CMD_INFO

        '''



def main():  # pragma: no cover
    if sys.version_info < (3, 0):
        print('Please make sure you are using Python 3.')
        return
    createtable()
    print(execute(sys.argv))


if __name__ == '__main__':  # pragma: no cover
    main()



# print(canaccess('doing','muggle','football'))


#conn.close()