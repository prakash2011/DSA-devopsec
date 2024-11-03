#quick sort
def quick(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while i<=high and arr[i]<=pivot:
            i+=1
        while j>low and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j


def quicksort(arr,low,high):
    if low<high:
        partionindex=quick(arr,low,high)
        quicksort(arr,low,partionindex-1)
        quicksort(arr,partionindex+1,high)

# insertion sort
def insertionsort(n,arr):
    
    for i in range(0,n):
        j=i
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1




#merge sort
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1

    while left<=mid and right<=high:
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else :
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]


def mergesort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)





#bubble sort
def bubblesort(n,arr):
    for i in range(n-1,0,-1):
        didswap=0 # optimize performance run only o(n) if in order array
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                didswap=1
        if didswap==0:
            break
        print('run')
        


# selection sort
def selectionsort(n,arr):
    for i in range(0,n-2+1):
        mini=i
        for j in range(i,n-1+1):
            if arr[j]<arr[mini]:
                mini=j
                # print(arr[mini])
        arr[mini],arr[i]=arr[i],arr[mini]

n=int(input('Enter the array Size :'))
# for i in range(0,n):
arr=list(input().split(' '))
# selectionsort(n,arr)
# bubblesort(n,arr)
# insertionsort(n,arr)
# mergesort(arr,0,n)
quicksort(arr,0,n-1)
for i in range(0,n):
    print(arr[i],end=' ')
