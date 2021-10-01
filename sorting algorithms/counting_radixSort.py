def radix_count_sort(arr,n):
    m=arr[0]
    for i in arr:
        if(i>m):
            m=i
    passes=0
    while(m>0):
        m=m//10
        passes+=1

    output=[0]*n
    power=1
    for j in range(0,passes):
        count = [0] * 10
        for i in range(0, n):
            index = (arr[i] // power)
            count[index % 10]+=1

        for i in range(1,10):
            count[i]=count[i]+count[i-1]

        cnt = n-1
        while cnt>=0:
            index = (arr[cnt] // power)
            count[index % 10] -= 1
            output[count[index % 10]]=arr[cnt]
            cnt-=1

        for i in range(0,n):
            arr[i]=output[i]

        print("Pass  ",j+1,"  :- ")
        print(arr)
        power=power*10


    print("The final array is(Radix counting sort) :-\n")
    print(arr)






def main():
    n=int(input("Enter no of vlaues in the array :- "))
    students=[]
    print("Enter elements :- ")
    for i in range(0,n):
        students.append(int(input()))


    print("=================================================")
    print("Quick Sort")
    radix_count_sort(students,0,n-1)
    print("Result of quick sort is :- ")
    print(students)

#Main function
main();
