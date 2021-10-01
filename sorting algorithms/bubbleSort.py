def bubble_sort(arr,n):
    print("======================================================\n")
    print("BUBBLE SORT :- ")
    swapcnt=0
    cnt = 0;
    print("Pass number ", cnt, ":- ", arr)
    cnt += 1
    for i in range(0,n):
        flag=1

        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapcnt+=1
                flag=0

        print("Pass number ", cnt, ":- ", arr)
        cnt += 1
        if(flag==1):
            break

    print("TOP 5 scores are:- \n")
    cnt=0
    for i in  arr[::-1]:
        print(i)
        cnt+=1
        if(cnt==5):break

    print("Total swap counts are :- ",swapcnt)
    print("======================================================\n")


def main():
        n=int(input("Enter no of values in the array :- "))
        students=[]
        print("Enter percentage of students :- ")
        for i in range(0,n):
            students.append(int(input()))

    
        bubble_sort(students[:],n)
    
main()