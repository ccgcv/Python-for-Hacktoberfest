hash_size=10
hash_table={}
for i in range (0,hash_size):
    hash_table[i]=[-1,-1]


def insert(x):
    index=x%hash_size
    if(hash_table[index][0]==-1):
        hash_table[index][0]=x
        return
    elif(hash_table[index][0]%hash_size==index):
        ret_index=index
        while(hash_table[ret_index][1]!=-1):
            ret_index=hash_table[ret_index][1]
        
        next_index=(ret_index+1)%hash_size
        while(next_index!=index):
            if(hash_table[next_index][0]==-1):
                hash_table[next_index][0]=x
                hash_table[ret_index][1]=next_index
                return
            next_index=(next_index+1)%hash_size
        flag=1
        print("Hash Table is Full")
        return
    else:
        hash_table[index][0],x=x,hash_table[index][0]
        prev_pos=x%hash_size;
        while(hash_table[prev_pos][1]!=index):
            prev_pos=hash_table[prev_pos][1]
                                          
        temp=index
        cnt=0
        temp+=1
        cnt+=1
        while(cnt<hash_size and hash_table[temp][0]!=-1 and hash_table[temp][0]%hash_size!=index):
            temp=(temp+1)%hash_size
            cnt+=1
        
        if(cnt==hash_size):
            hash_table[index][0],x=x,hash_table[index]
            flag=1
            print("Hash Table is Full")
            return
        
        if(hash_table[temp][0]==-1):
            hash_table[temp][0]=x
            hash_table[prev_pos][1]=temp
            return
        else:
            ret_index=temp
            while(hash_table[ret_index][1]!=-1):
                ret_index=hash_table[ret_index][1]
        
            next_index=(ret_index+1)%hash_size
            while(next_index!=index):
                if(hash_table[next_index][0]==-1):
                    hash_table[next_index][0]=x
                    hash_table[index][1]=ret_index
                    return
                next_index=(next_index+1)%hash_size

            hash_table[index][0],x=x,hash_table[index]
            flag=1
            print("Hash Table is Full")
            return


def search(x):
    index=x%hash_size
    compar=1
    if(hash_table[index][0]==x):
        print("Element found and total ",compar," comparisions were required")
        return
    elif(hash_table[index][0]%hash_size==index):
        ret_index=index
        while(hash_table[ret_index][1]!=-1):
            ret_index=hash_table[ret_index][1]
            compar+=1
            if(hash_table[ret_index][0]==x):
                print("Element found and total ",compar," comparisions were required")
                return

        print("CANNOT FIND and total ",compar," were required")
    else:
        print("CANNOT FIND and total ",compar," were required")




def display(hash_table):
    for i in range(0,hash_size):
        print("Index- ",i," Value:- ",hash_table[i][0]," Chain:- ",hash_table[i][1])


def main():
    print("-___________________________________-")
    print("1.ADD A NEW NUMBER")
    print("2.SEARCH A NEW NUMBER")
    print("3.DELETE A NEW NUMBER")
    print("4.Display Hash Table")
    print("4.EXIT")
    print("-___________________________________-")
    while(1):
        n=int(input("Enter your choice:- "))
        if(n==1):
            x=int(input("Enter the number you want to insert:- "))
            insert(x)
            display(hash_table)
        elif(n==2):
            flag=0
            x=int(input("Enter the number you want to search:- "))
            if(flag==1):
                continue
            search(x)
        else:
            break