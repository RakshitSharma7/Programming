def createList():
    l=[]
    while True:
        try:
            n=int(input("Enter Num: "))
            l.append(n)
        except Exception as e:
            return l


# BINARY SEARCH
# def binarySearch(l,start,end,target):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == l[mid]:
#             return mid
#         elif target < l[mid]:
#             end = mid - 1
#         elif target > l[mid]:
#             start = mid + 1
#     return -1

#   BINARY SEARCH ASCENDING

# def binarySearchAsc(l,start,end,target):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == l[mid]:
#             return mid
#         elif target < l[mid]:
#             end = mid - 1
#         elif target > l[mid]:
#             start = mid + 1
#     return -1
#
#
# BINARY SEARCH DESCENDING

# def binarySearchDesc(l,start,end,target):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == l[mid]:
#             return mid
#         elif target < l[mid]:
#             start = mid + 1
#         elif target > l[mid]:
#             end = mid - 1
#     return -1
#
# l=createList()
# n=len(l)
# target=int(input("Enter the Target Element: "))
#
# if l[0]<l[n-1]:
#     res=binarySearchAsc(l,0,n-1,target)
# else:
#     res = binarySearchDesc(l, 0, n - 1, target)
#
# if res!=-1:
#     print("Target Element ",target," Found at index: ",res)
# else:
#     print("Target Element",target," Not Found")



# BINARY SEARCH RECURSION

# def binarySearch(l,start,end,target):
#     mid=(start+end)//2
#     if target==l[mid]:
#         return mid
#     elif start>end:
#         return -1
#
#     if target<l[mid]:
#         return binarySearch(l,start,mid-1,target)
#     elif target>l[mid]:
#         return binarySearch(l,mid+1,end,target)

# ORDER AGNOSTIC BINARY SEARCH

# def binarySearch(l,start,end,target):
#     flag=True
#     if l[start]>l[end]:
#         flag=False
#     while start<=end:
#         mid = (start + end) // 2
#         if target==l[mid]:
#             return mid
#         if flag:
#             if target<l[mid]:
#                 end=mid-1
#             elif target>l[mid]:
#                 start=mid+1
#         else:
#             if target<l[mid]:
#                 start=mid+1
#             elif target>l[mid]:
#                 end=mid-1
#     return -1



# RECURSION

def binarySearch(l,start,end,target,flag):
    mid=(start+end)//2
    if target==l[mid]:
        return mid
    elif start>end:
        return -1

    if flag:
        if target < l[mid]:
            return binarySearch(l, start, mid - 1, target, flag)
        elif target > l[mid]:
            return binarySearch(l, mid + 1, end, target, flag)
    else:
        if target < l[mid]:
            return binarySearch(l, start+1, end, target, flag)
        elif target > l[mid]:
            return binarySearch(l, start , mid-1, target, flag)

l=createList()
n=len(l)
target=int(input("Enter the Target Element: "))
flag=True
if flag:
    if l[0]>l[n-1]:
        flag=False
res=binarySearch(l,0,n-1,target,flag)
if res!=-1:
    print("Target Element ",target," Found at index: ",res)
else:
    print("Target Element",target," Not Found")