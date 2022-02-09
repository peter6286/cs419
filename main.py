import sqlite3

conn = sqlite3.connect('wo.db')
print ("数据库打开成功")
c = conn.cursor()
def createtable():
    # print()
    c.execute('''CREATE TABLE USER
    (USER_NAME    TEXT  PRIMARY KEY   NOT NULL,
    password      TEXT     NOT NULL,
    domain        CHAR(50));''')
    print("数据表创建成功")
    conn.commit()

def insert(user,password):
    list1 = [user,password,'NULL']
    c.execute("INSERT INTO USER (USER_NAME,password,domain) \
          VALUES ('Paul', 'dsfadf','NULL')")

    c.execute("INSERT INTO USER (USER_NAME,password,domain) \
              VALUES ('fingal', 'dfadf','NULL')")

    c.execute("INSERT INTO USER (USER_NAME,password,domain) \
             VALUES (?,?,?)",list1)

    conn.commit()
    print("数据插入成功")

def select():
    #sql = "SELECT USER_NAME ,password from USER where USER_NAME = %s;"
    cursor = c.execute("SELECT USER_NAME ,password from USER")
    for row in cursor:
        #print("ID = ", row[0])
        print("USER_NAME = ", row[0])
        print("password = ", row[1])
       # print("SALARY = ", row[3], "\n")

        print("数据操作成功")
        conn.commit()

createtable()
insert('peter','asdsf')
select()
conn.close()