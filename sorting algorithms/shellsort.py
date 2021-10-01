def shell_sort(arr,n):
    print("======================================================\n")
    print("SHELL SORT :- ")
    interval = n // 2
    cnt = 0
    print("Pass number ", cnt, ":- ", arr)
    cnt += 1
    while interval > 0:
        for i in range(interval,n):
            curr=arr[i]
            j=i
            while j>=interval and arr[j-interval]>curr:
                arr[j]=arr[j-interval]
                j-=interval

            arr[j]=curr


        print("Pass number ", cnt, ":- ", arr)
        cnt += 1
        interval //= 2

    print(arr)

    print("======================================================\n")


def main():
        n=int(input("Enter no of values in the array :- "))
        students=[]
        print("Enter percentage of students :- ")
        for i in range(0,n):
            students.append(int(input()))

    
        shell_sort(students[:],n)
    
main()