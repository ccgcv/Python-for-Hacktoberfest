#DSA Assignment 1
#Phone Book Directory Using Hash Tables
#Submitted by Navneet Das 3231

def Keyfunc(x):
    key = 0
    for i in range(len(x)):
        key += ord(x[i]) * (10 ** (len(x) - i + 1))
    return key

def Linear_Insertion(hash_table, t_size, x, y):
    key = Keyfunc(x)
    location = key % t_size
    if hash_table[location][1] == -1 or hash_table[location][1] == -2:
        hash_table[location][0] = x
        hash_table[location][1] = y
        return
    else:
        i = 1
        while i < t_size:
            location = (location + 1) % t_size
            if hash_table[location][1] == -1 or hash_table[location][1] == -2:
                hash_table[location][0] = x
                hash_table[location][1] = y
                return
            i += 1

def Quadratic_Insertion(hash_table, t_size, x, y):
    key = Keyfunc(x)
    location = key % t_size
    if hash_table[location][1] == -1 or hash_table[location][1] == -2:
        hash_table[location][0] = x
        hash_table[location][1] = y
        return
    else:
        i = 1
        while i < t_size:
            location = (location + i ** 2) % t_size
            if hash_table[location][1] == -1 or hash_table[location][1] == -2:
                hash_table[location][0] = x
                hash_table[location][1] = y
                return
            i += 1

def Linear_Search(hash_table, t_size, x):
    noc = 0
    key = Keyfunc(x)
    location = key % t_size
    if hash_table[location][0] == x:
        noc += 1
        print("Contact found at index", location, "with mobile number", hash_table[location][1])
        print("Comparisons done : ", noc)
        return
    elif hash_table[location][1] == -1:
        noc += 1
        print("Contact doesn't exist! Check Again!")
        print("Comparisons done : ", noc)
        return
    else:
        i = 1
        while i < t_size:
            location = (location + 1) % t_size
            if hash_table[location][0] == x:
                noc += 1
                print("Contact found at index", location, "with mobile number", hash_table[location][1])
                print("Comparisons done : ", noc)
                return
            elif hash_table[location][1] == -1:
                noc += 1
                break
            i += 1
            noc += 1
        print("Contact doesn't exist! Check Again!")
        print("Comparisons done : ", noc)

def Quadratic_Search(hash_table, t_size, x):
    noc = 0
    key = Keyfunc(x)
    location = key % t_size
    if hash_table[location][0] == x:
        noc += 1
        print("Contact found at index", location, "with mobile number", hash_table[location][1])
        print("Comparisons done : ", noc)
        return
    elif hash_table[location][1] == -1:
        noc += 1
        print("Contact doesn't exist! Check Again!")
        print("Comparisons done : ", noc)
        return
    else:
        i = 1
        while i < t_size:
            location = (location + i ** 2) % t_size
            if hash_table[location][0] == x:
                noc += 1
                print("Contact found at index", location, "with mobile number", hash_table[location][1])
                print("Comparisons done : ", noc)
                return
            elif hash_table[location][1] == -1:
                noc += 1
                break
            i += 1
            noc += 1
        print("Contact doesn't exist! Check Again!")
        print("Comparisons done : ", noc)

def Linear_Deletion(hash_table, t_size, x):
    key = Keyfunc(x)
    location = key % t_size
    if hash_table[location][0] == x:
        hash_table[location][0] = ''
        hash_table[location][1] = -2
        print("Contact Deleted")
        return
    elif hash_table[location][1] == -1:
        print("Contact doesn't exist! Check Again!")
        return
    else:
        i = 1
        while i < t_size:
            location = (location + 1) % t_size
            if hash_table[location][0] == x:
                hash_table[location][0] = ''
                hash_table[location][1] = -2
                print("Contact Deleted")
                return
            elif hash_table[location][1] == -1:
                break
            i += 1
        print("Contact doesn't exist! Check Again!")

def Quadratic_Deletion(hash_table, t_size, x):
    key = Keyfunc(x)
    location = key % t_size
    if hash_table[location][0] == x:
        hash_table[location][0] = ''
        hash_table[location][1] = -2
        print("Contact Deleted")
        return
    elif hash_table[location][1] == -1:
        print("Contact doesn't exist! Check Again!")
        return
    else:
        i = 1
        while i < t_size:
            location = (location + i ** 2) % t_size
            if hash_table[location][0] == x:
                hash_table[location][0] = ''
                hash_table[location][1] = -2
                print("Contact Deleted")
                return
            elif hash_table[location][1] == -1:
                break
            i += 1
        print("Contact doesn't exist! Check Again!")

def main():
    #for linear probing
    linear_hash_table = [['', -1] for i in range(11)]
    #for quadratic probing
    quadratic_hash_table = [['', -1] for i in range(11)]
    choice = 0
    while choice != 5:
        print("PHONE_BOOK MENU"),
        print("1 -> INSERTION")
        print("2 -> SEARCH")
        print("3 -> DELETE")
        print("4 -> DISPLAY ")
        print("5 -> EXIT")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            x = input("\nEnter Name of the Person : ")
            y = int(input("Enter Phone Number : "))
            Linear_Insertion(linear_hash_table, len(linear_hash_table), x, y)
            Quadratic_Insertion(quadratic_hash_table, len(quadratic_hash_table), x, y)
        elif choice == 2:
            x = input("\nEnter the name for searching : ")
            Linear_Search(linear_hash_table, len(linear_hash_table), x)
            Quadratic_Search(quadratic_hash_table, len(quadratic_hash_table), x)
        elif choice == 3:
            x = input("\nEnter the name for deleting contact: ")
            Linear_Deletion(linear_hash_table, len(linear_hash_table), x)
            Quadratic_Deletion(quadratic_hash_table, len(quadratic_hash_table), x)
        elif choice == 4:
            print("LINEAR HASH_TABLE:"),
            print(linear_hash_table)
            print("QUADRATIC HASH_TABLE:"),
            print(quadratic_hash_table)
main()
