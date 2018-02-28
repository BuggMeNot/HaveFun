def binary_sqrt(n):
    
    l,r = 0,n
    if n ==0 or n ==1:
        return n
    
    while(l < r):
        mid = (r - l )/2 + l
        if mid == n/mid:
            return int(mid)
        if mid < n/mid:
            
            print("l = ",l)
            print("mid = ",mid)
            l = mid + 1
        else:
            print("r = ",r)
            r = mid - 1
    if l > n/l:
        return int(l) - 1
    else:
        return l
    
def binary_search(l,target,low,high):
    if len(l)  == 0:
        return False

    mid = (high-low)//2 + low
    print('mid = ',mid)
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        print('left')
        print('low = ',low)
        print('high = ' , high)
        print(l[low:mid])
        return binary_search(l,target,low,mid)
    elif l[mid] < target:

        print('right')
        print('low = ' ,low)
        print('high = ' , high)
        print(l[mid:high])
        return binary_search(l,target,mid+1,high)
  

l = [1,2,3,4,5,6,7,8,9,11,22,33,35]
print(binary_search(l,9,0,13))

def search(seq, num, low, high):
    if low == high:
        if num == seq[low]:
            print("Found it: ", num,low)
            return num,low
        else:
            print("No Found!")
            return False
    else:
        middle = (low + high) // 2
        if num > seq[middle]:
            print(num, ' > ', seq[middle])
            print('low = ',low)
            print('high = ',high)
            search(seq, num, middle + 1, high)
        else:
            print(num ,' <= ', seq[middle])
            print('low = ',low)
            print('high = ',high)
            search(seq, num, low, middle)

a = search(l, 11, 5,13)
#print a
    