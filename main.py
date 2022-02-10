import sqlite3

conn = sqlite3.connect('wo.db')
print ("数据库打开成功")

def createtable():
    # print()
    c0 = conn.cursor()
    c1 = conn.cursor()
    c2 = conn.cursor()

    #c0.execute('''CREATE TABLE USER
    #(USER_NAME    TEXT  PRIMARY KEY   NOT NULL,
    #password      TEXT     NOT NULL,
    #domain        CHAR(50));''')

    #c1.execute('''CREATE TABLE OBJECTS
    #    (objectname  TEXT NOT NULL,
    #    type         TEXT NOT NULL  );''')

    c2.execute('''CREATE TABLE ACCESS
           (operationname  TEXT NOT NULL,
            domainname  TEXT NOT NULL 
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
    cursor = c.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [name])
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
    dict = {}
    #res = []
    if domain == '':
        return 'Error: missing domain'
    cursor = c.execute("SELECT domain,USER_NAME from USER ")

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
    conn.commit()
    #print(dict)
    return (dict[domain])

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








createtable()
#insert('Daniel','CDEFG')
#insert('peter','hjgk')
#insert('chelsea','hjgk')
#insert('liverpool','opte')
#insert('Milan','lower')
#setDomain('liverpool','PL')
#setDomain('chelsea','PL')
#setDomain('Milan','italy')
#select('milan','chelsea')
#print(authenticate('peter','CEFG'))
#print(DomainInfo("PL"))
#SetType('Minamino','Japan')
#SetType('takumi','Japan')
#SetType('Mane','Sengal')
#SetType('Salah','Egypt')
print(Typeinfo('Japan'))


conn.close()