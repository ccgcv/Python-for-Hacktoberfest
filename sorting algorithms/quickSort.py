

def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h
    while (i < j):
        while (i < h and arr[i] < pivot):
            i += 1
        while (j> l and arr[j] > pivot):
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick_sort(arr,l,h):
    if(l<h):
        value=partition(arr,l,h)
        print("Partition to left of pivot",value)
        print(arr[l:value])
        print("Partition to right of pivot", value)
        print(arr[value + 1:h + 1])
        quick_sort(arr,l,value-1)
        quick_sort(arr,value + 1,h)



def main():
    n=int(input("Enter no of vlaues in the array :- "))
    students=[]
    print("Enter elements :- ")
    for i in range(0,n):
        students.append(int(input()))


    print("=================================================")
    print("Quick Sort")
    quick_sort(students,0,n-1)
    print("Result of quick sort is :- ")
    print(students)

#Main function
main();
