import csv,sys,os

def create(file):
    if file == "USER.csv":
        path = file
        with open(path, 'w') as f1:
            csv_write = csv.writer(f1)
            csv_head = ["USER_NAME", "password"]
            csv_write.writerow(csv_head)
        f1.close()

    if file =="OBJECTS.csv":
        path = file
        with open(path, 'w') as f2:
            csv_write = csv.writer(f2)
            csv_head = ["objectname", "type"]
            csv_write.writerow(csv_head)
        f2.close()

    if file == "ACCESS.csv":
        path = file
        with open(path, 'w') as f3:
            csv_write = csv.writer(f3)
            csv_head = ["opertaionname", "domainname", "typename"]
            csv_write.writerow(csv_head)
        f3.close()

    if file == "DOMAIN.csv":
        path = file
        with open(path, 'w') as f4:
            csv_write = csv.writer(f4)
            csv_head = ["username", "domain"]
            csv_write.writerow(csv_head)
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
    return ("success in adding user")


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
    for item1,item2 in temp1:
        if (item1 in temp2) & (item2 in temp3):
            return ("success in access")
    exit("Do not had access")

def execute(args):

    args_passed = len(args)
    if args_passed < 2:
        exit("please look up the command info")

    else:
        base_cmd = args[1].lower()

        if base_cmd == 'adduser':
            if args_passed != 4:
                exit(' Input argument adduser user password')
            if (args[2] == "USER_NAME"):
                exit("use another name")
            if str(args[2]).isspace():
                exit("username missing")

            print(adduser(args[2], args[3]))

        elif base_cmd == 'authenticate':
            if args_passed != 4:
                exit('Input argument Authenticate user password')

            print(authenticate(args[2], args[3]))

        elif base_cmd == 'setdomain':
            if args_passed != 4:
                exit('Input argument SetDomain user domain')

            if (args[2] == "username"):
                exit("use another name")

            if str(args[3]).isspace():
                exit("missing domain")

            print(setDomain(args[2], args[3]))

        elif base_cmd == 'domaininfo':
            if args_passed != 3:
                exit('Input argument DomainInfo domain')

            if str(args[2]).isspace():
                exit("missing domain")

            ans = DomainInfo(args[2])
            for item in ans:
                print(item)

        #return DomainInfo(args[2])

        elif base_cmd == 'settype':
            if args_passed != 4:
                exit('Input argument SetType object type')

            if str(args[2]).isspace():
                exit("missing object")

            if str(args[3]).isspace():
                exit("missing type_name")

            if (args[2] == "objectname"):
                exit("use another name")

            print(SetType(args[2], args[3]))

        elif base_cmd == 'typeinfo':
            if args_passed != 3:
                exit('Input argument TypeInfo type')

            if str(args[2]).isspace():
                exit("missing type_name")

            ans = Typeinfo(args[2])
            for item in ans:
                print(item)

        #return Typeinfo(args[2])

        elif base_cmd == 'addaccess':
            if args_passed != 5:
                exit('Input argument - operation domain type')

            if str(args[2]).isspace():
                exit("missing operation")

            if str(args[3]).isspace():
                exit("missing domain")

            if str(args[4]).isspace():
                exit("missing type")

            if (args[2] == "objectname"):
                exit("use another name")

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
    execute(sys.argv)


if __name__ == '__main__':  # pragma: no cover
    if not os.path.exists('USER.csv'):
        create('USER.csv')
    if not os.path.exists('OBJECTS.csv'):
        create('OBJECTS.csv')
    if not os.path.exists('DOMAIN.csv'):
        create('DOMAIN.csv')
    if not os.path.exists('ACCESS.csv'):
        create("ACCESS.csv")
    main()




