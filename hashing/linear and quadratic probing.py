hash_size=11
hash_table_linear={}
for i in range (0,hash_size):
    hash_table_linear[i]=["-1",-1]

hash_table_quad={}
for i in range(0,hash_size):
    hash_table_quad[i]=["-1",-1]

#deleted values
delstr="deleted-entry"
delnum=-2

def hash_roll(str):
    p = 31
    power_of_p = 1
    hash_val = 0
    m = 1e9 + 9

    for i in range(len(str)):
        hash_val = ((hash_val + (ord(str[i]) -
                                 ord('a') + 1) *
                              power_of_p) % m)
 
        power_of_p = (power_of_p * p) % m
 
    return int(hash_val)%hash_size


def insert_linear(name,num):
    
    index=hash_roll(name)

    if(hash_table_linear[index][0]=="-1"):
        hash_table_linear[index]=[name,num]
    else:
        next_index=(index+1)%hash_size
        while(next_index!=index):
            if(hash_table_linear[next_index][0]=="-1"):
                hash_table_linear[next_index]=[name,num]
                return
            next_index=(next_index+1)%hash_size

        print("LINEAR HASH TABLE IS FULL CANNOT INSERT")


def search_linear(name):
    index=hash_roll(name)
    compar=1
    if(hash_table_linear[index][0]==name):
        print("Entry found and total ",compar," comparisions were required(LINEAR PROBING)")
        return
    elif(hash_table_linear[index][0]!="-1" ):
        next_index=(index+1)%hash_size
        while(next_index!=index):
            compar+=1
            if(hash_table_linear[next_index][0]==name):
                print("Entry  found and total ",compar,"comparisions were required(LINEAR PROBING)")
                return
            next_index=(next_index+1)%hash_size

        print("CANNOT FIND in LINEAR PROBING hashing table")
    else:
        print("CANNOT FIND in LINEAR PROBING hashing table")


def delete_linear(name):
    index=hash_roll(name)

    if(hash_table_linear[index][0]==name):
        print("Element deleted")
        hash_table_linear[index][0]=delstr
        hash_table_linear[index][1]=delnum
        return
    elif(hash_table_linear[index][0]!="-1"):
        next_index=(index+1)%hash_size
        while(next_index!=index):
            if(hash_table_linear[next_index][0]==name):
                print("Element deleted")
                hash_table_linear[next_index][0]=delstr
                hash_table_linear[next_index][1]=delnum
                return

            next_index=(next_index+1)%hash_size

        print("CANNOT FIND in LINEAR PROBING hashing table")
    else:
        print("CANNOT FIND in LINEAR PROBING hashing table")

def insert_quad(name,num):
    
    index=hash_roll(name)

    if(hash_table_quad[index][0]=="-1"):
        hash_table_quad[index]=[name,num]
    else:
        power=1
        next_index=(index+(power**2))%hash_size
        while(next_index!=index):
            if(hash_table_quad[next_index][0]=="-1"):
                hash_table_quad[next_index]=[name,num]
                return
            power+=1
            next_index=(index+(power**2))%hash_size
        
        print("QUADRATIC HASH TABLE IS FULL CANNOT INSERT")


def search_quad(name):
    index=hash_roll(name)
    compar=1
    if(hash_table_quad[index][0]==name):
        print("Phone number found and total ",compar," comparisions were required(QUADRATIC PROBING)")
        return
    elif(hash_table_quad[index][0]!="-1" ):
        power=1
        next_index=(index+(power**2))%hash_size
        while(next_index!=index):
            compar+=1
            if(hash_table_quad[next_index][0]==name):
                print("Phone number found and total ",compar," comparisions were required(QUADRATIC PROBING)")
                return
            power+=1
            next_index=(index+(power**2))%hash_size
        
        print("CANNOT FIND in LINEAR PROBING hashing table")
    else:
        print("CANNOT FIND in LINEAR PROBING hashing table")


def delete_quad(name):
    index=hash_roll(name)

    if(hash_table_quad[index][0]==name):
        print("Element deleted")
        hash_table_quad[index][0]=delstr
        hash_table_quad[index][1]=delnum
        return
    elif(hash_table_quad[index][0]!="-1"):
        power=1
        next_index=(index+(power**2))%hash_size
        while(next_index!=index):
            if(hash_table_quad[next_index][0]==name):
                print("Element deleted")
                hash_table_quad[next_index][0]=delstr
                hash_table_quad[next_index][1]=delnum
                return
            power+=1
            next_index=(index+(power**2))%hash_size
        
        print("CANNOT FIND in QUADRATIC PROBING hashing table")
    else:
        print("CANNOT FIND in QUADRATIC PROBING hashing table")




def display(hash_table):
    for i in range(0,hash_size):
        print("Name:- ",hash_table[i][0]," Entry:- ",hash_table[i][1])

 
def main():
    print("-___________________________________-")
    print("1.ADD A NEW Entry")
    print("2.SEARCH A NEW Entry")
    print("3.DELETE A NEW Entry")
    print("4.Display Linear Probing Hash Table")
    print("5.Display Quadratic Probing Hash Table")
    print("4.EXIT")
    print("-___________________________________-")
    while(1):
        n=int(input("Enter your choice:- "))
        if(n==1):
            name=input("Enter name of Entry:- ")
            num=int(input("Enter Entry:- "))
            insert_linear(name,num)
            insert_quad(name,num)
        elif(n==2):
            name=input("Enter name of Entry you want to find:- ")
            search_linear(name)
            search_quad(name)
        elif(n==3):
            name=input("Enter name of Entry you want to delete:- ")
            delete_linear(name)
            delete_quad(name)
        elif(n==4):
            display(hash_table_linear)
        elif(n==5):
            display(hash_table_quad)
        else:
            break




main()