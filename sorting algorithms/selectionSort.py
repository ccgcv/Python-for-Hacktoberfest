def selection_sort(arr,n):
    print("======================================================\n")
    print("SELECTION SORT :- ")
    cnt = 0
    print("Pass number ", cnt, ":- ", arr)
    cnt += 1
    swapcnt=0
    for i in range(0,n):
        minm=i
        for j in range(i+1,n):
            if(arr[j]<arr[minm]):
                minm=j
                swapcnt+=1

        arr[i],arr[minm]=arr[minm],arr[i]
        print("Pass number ", cnt, ":- ", arr)
        cnt += 1


    print("Sorted array is (Selection sort):- \n",arr)
    print("Total swapcount is:- ",swapcnt)
    print("======================================================\n")


def main():
        n=int(input("Enter no of values in the array :- "))
        students=[]
        print("Enter percentage of students :- ")
        for i in range(0,n):
            students.append(int(input()))

    
        selection_sort(students[:],n)
    
main()