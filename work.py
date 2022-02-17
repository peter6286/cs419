import csv,sys,os


def create():
    path1,path2,path3,path4 = "USER.csv","OBJECTS.csv","ACCESS.csv","DOMAIN.csv"

    with open(path1,'w') as f1:
        csv_write = csv.writer(f1)
        csv_head = ["USER_NAME","password"]
        csv_write.writerow(csv_head)

    with open(path2,'w') as f2:
        csv_write = csv.writer(f2)
        csv_head = ["objectname","type"]
        csv_write.writerow(csv_head)

    with open(path3,'w') as f3:
        csv_write = csv.writer(f3)
        csv_head = ["opertaionname","domainname","typename"]
        csv_write.writerow(csv_head)


    with open(path4,'w') as f4:
        csv_write = csv.writer(f4)
        csv_head = ["username","domain"]
        csv_write.writerow(csv_head)

    f1.close()
    f2.close()
    f3.close()
    f4.close()

def checkuser(user):
    path = "USER.csv"
    with open(path, 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            #print(line[0])
            if line[0] == user:
                return True
    f.close()
    return False


def checkdomain(domain):
    path = "DOMAIN.csv"
    with open(path, 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line[1] == domain:
                f.close()
                return True
    f.close()
    return False


def checktype(type):
    path = "OBJECTS.csv"
    with open(path, 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line[1] == type:
                f.close()
                return True
    f.close()
    return False



def adduser(user,password):
    if checkuser(user):
        exit("user name already exit")
    else:
        path = "USER.csv"
        with open(path, 'a+') as f:
            csv_write = csv.writer(f)
            data_row = [user, password]
            csv_write.writerow(data_row)
    f.close()
    return ("success in add")


def authenticate(user,password):
    path = "USER.csv"
    with open(path, 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line[0] == user:
                if line[1] == password:
                    f.close()
                    return ("success in auth")
                else:
                    f.close()
                    exit("bad password")
        f.close()
        exit("NO such user")


def setDomain(name,domain):
    path = "DOMAIN.csv"
    if checkuser(name):
        with open(path,'a+') as f:
            csv_write = csv.writer(f)
            data_row = [name,domain]
            csv_write.writerow(data_row)
            f.close()
            return ("success in setting domain")
    else:
        exit("No such user")

def DomainInfo(domain):
    path = "DOMAIN.csv"
    res = []
    with open(path, 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line[1] == domain:
                if line[0] not in res:
                    res.append(line[0])
    f.close()
    return res if len(res)!=0 else exit("NO such Domain")



def SetType(objectname,type):
    path = "OBJECTS.csv"
    with open(path, 'a+') as f:
        csv_write = csv.writer(f)
        data_row = [objectname, type]
        csv_write.writerow(data_row)
    f.close()
    return ("success in adding type")

def Typeinfo(type):
    path = "OBJECTS.csv"
    res = []
    with open(path, 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line[1] == type:
                if line[0] not in res:
                    res.append(line[0])
    f.close()
    return res if len(res) != 0 else exit("NO such Type")



def addaccess(operation,Dname,Tname):
    path = "ACCESS.csv"
    '''
    if checkdomain(Dname) & checktype(Tname):
        with open(path, 'a+') as f:
            csv_write = csv.writer(f)
            data_row = [operation,Dname,Tname]
            csv_write.writerow(data_row)
    else:
        exit("No such Domain name or type name")
    '''

    with open(path, 'a+') as f:
        csv_write = csv.writer(f)
        data_row = [operation, Dname, Tname]
        csv_write.writerow(data_row)

    f.close()
    return ("success in adding access")


def canaccess(op,un,on):
    path1 = "ACCESS.csv"
    temp1 = []
    with open(path1, 'r') as f1:
        csv_read = csv.reader(f1)
        for line in csv_read:
            if line[0] == op:
                    if (line[1],line[2]) not in temp1:
                        temp1.append((line[1],line[2]))

    path2 = "DOMAIN.csv"
    temp2 = []
    with open(path2, 'r') as f2:
        csv_read = csv.reader(f2)
        for line in csv_read:
            if line[0] == un :
                if line[1] not in temp2:
                    temp2.append(line[1])

    temp3 = []
    path3 = "OBJECTS.csv"
    with open(path3, 'r') as f3:
        csv_read = csv.reader(f3)
        for line in csv_read:
            if line[0] == on:
                if line[1] not in temp3:
                    temp3.append(line[1])
    f1.close()
    f2.close()
    f3.close()
    #print(temp1)
    #print(temp2)
    #print(temp3)
    for item1,item2 in temp1:
        if (item1 in temp2) & (item2 in temp3):
            return ("success in access")
    exit("Do not had access")

def execute(args):

    args_passed = len(args)
    if args_passed < 2:
        return ("please look up the command info")

    else:
        base_cmd = args[1].lower()

        if base_cmd == 'adduser':
            if args_passed != 4:
                exit(' Input argument adduser user password')

            print(adduser(args[2], args[3]))

        elif base_cmd == 'authenticate':
            if args_passed != 4:
                exit('Input argument Authenticate user password')

            print(authenticate(args[2], args[3]))

        elif base_cmd == 'setdomain':
            if args_passed != 4:
                exit('Input argument SetDomain user domain')

            print(setDomain(args[2], args[3]))

        elif base_cmd == 'domainfo':
            if args_passed != 3:
                return 'Input argument DomainInfo domain'
            ans = DomainInfo(args[2])
            for item in ans:
                print(item)

        #return DomainInfo(args[2])

        elif base_cmd == 'settype':
            if args_passed != 4:
                exit('Input argument SetType object type')

            print(SetType(args[2], args[3]))

        elif base_cmd == 'typeinfo':
            if args_passed != 3:
                exit ('Input argument TypeInfo type')

            ans = Typeinfo(args[2])
            for item in ans:
                print(item)

        #return Typeinfo(args[2])

        elif base_cmd == 'addaccess':
            if args_passed != 5:
                exit('Input argument - operation domain type')

            print(addaccess(args[2], args[3], args[4]))

        elif base_cmd == 'canaccess':
            if args_passed != 5:
                print('Input argument CanAccess operation user object')

            print(canaccess(args[2], args[3], args[4]))

        else:
            exit("make sure the command is correct")


def main():
    if sys.version_info < (3, 0):
        print('Please make sure you are using Python 3.')
        return
    #createtable()
    execute(sys.argv)


if __name__ == '__main__':  # pragma: no cover
    if not os.path.exists('USER.csv'):
        create()
    main()


















#create()
#adduser("muggle","1234")
#print(checkuser('peter'))
#print(authenticate('peter','1234'))
#print(setDomain('muggle','fucker'))
#print(setDomain('peter','fucker'))
#print(setDomain('anna','lover'))
#print(DomainInfo("fucker"))
#SetType('liverpool','pm')
#SetType('chelsea','pm')
#SetType('real','spain')
#SetType('guangzhou','china')
#print(Typeinfo('chin'))
#print(addaccess('watch','fucker','pm'))
#print(addaccess('watch','lover','china'))
#print(addaccess('read','fucker','spain'))
#print(canaccess('watch','muggle','liverpool'))
#print(canaccess('watch','muggle','real'))




