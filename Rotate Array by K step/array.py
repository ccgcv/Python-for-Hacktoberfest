'''Given an array, rotate the array to the right by k steps, where k is non-negative.  

📌Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

📌Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?'''

a=[1,2,3,4,5,6,7] 
k=3
# Output:[5,6,7,1,2,3,4]
# a=[-1,-100,3,99]
# k=2
# Output:[3,99,-1,-100]
'''Solution 1:Complexity=O(1)'''
Y=a[-k:]+a[0:-k]
print(Y)

'''Solution 2:Complexity=O(n)'''
# for i in range (0,k):
#     x=len(a)+1
#     y=a[x:]+a[0:x]
# print(y)

'''Solution 3:Complexity=O(n^2)'''
# a1=a[-k:]
# a2=a[0:-k]
# A=[]
# for i in range (0,len(a1)):
#     A.append(a1[i])
# for j in range(0,len(a2)):
#     A.append((a2[j]))
# print(A)





