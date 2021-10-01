def insertion_sort(arr,n):
    print("======================================================\n")
    print("INSERTION SORT :- ")
    cnt=0
    print("Pass number ", cnt, ":- ", arr)
    cnt += 1
    for i in range(1,n):
        current=arr[i]

        j=i-1
        while j>=0 and current<arr[j]:
            arr[j+1]=arr[j]
            j=j-1

        arr[j+1]=current

        print("Pass number ", cnt, ":- ", arr)
        cnt += 1
    print("Sorted array is (Insertion sort):- \n",arr)
    print("======================================================\n")


def main():
        n=int(input("Enter no of values in the array :- "))
        students=[]
        print("Enter percentage of students :- ")
        for i in range(0,n):
            students.append(int(input()))

    
        insertion_sort(students[:],n)
    
main()