def radix_sort(arr,n):
    m=arr[0]
    for i in arr:
        if(i>m):
            m=i
    passes=0
    while(m>0):
        m=m//10
        passes+=1

    bucket = []
    for i in range(0, 10):
        bucket.append([])

    power=1
    for j in range(0,passes):
        for i in range(0, n):
            index = (arr[i] // power)
            bucket[index % 10].append(arr[i])
        cnt = 0
        print("Bucket array after ",j+1,"traversal")
        print(bucket)

        for i in range(0, len(bucket)):
            while (len(bucket[i]) != 0):
                arr[cnt] = bucket[i][0]
                cnt += 1
                bucket[i].remove(bucket[i][0])

        print("Pass  ",j+1,"  :- ")
        print(arr)
        power=power*10

    print("The final array is(Radix bucket sort) :-")
    print(arr)

def main():
    n=int(input("Enter no of vlaues in the array :- "))
    students=[]
    print("Enter elements :- ")
    for i in range(0,n):
        students.append(int(input()))


    print("=================================================")
    print("Quick Sort")
    radix_sort(students,0,n-1)
    print("Result of quick sort is :- ")
    print(students)

#Main function
main();
