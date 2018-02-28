# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:41:04 2018

@author: adminuser
"""
import random
import time

"""""""""""""""""""""
最简洁的快排
"""""""""""""""""""""
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])
 
"""""""""""""""""""""
一般快排
"""""""""""""""""""""    
def quick_sort(array, left, right):  
    if left >= right:  
        return  
    low = left  
    high = right  
    key = array[low]  
    while left < right:  
        while left < right and array[right] > key:  
            right -= 1  
        array[left] = array[right]
        print(left,right)
        while left < right and array[left] <= key:  
            left += 1
        array[right] = array[left]
        print(left,right)

    array[right] = key
    print("===key is {0},and array is {1}".format(key,array))
    quick_sort(array, low, left - 1)  
    quick_sort(array, left + 1, high)  


"""""""""""""""""""""
插入排序
"""""""""""""""""""""              
def insert(lists):
    count=len(lists)
    for i in range(1,count):
        key = lists[i]
        j = i - 1
        while j>=0:
            if lists[j]>key:
                lists[j + 1] = lists[j]
                lists[j] = key
    return lists


"""""""""""""""""""""
生成随机数据
"""""""""""""""""""""
def random_nums_generator(max_value, total_nums):
    num_lists = []
    for i in range(total_nums):
        num_lists.append(random.randint(0,max_value))
    return num_lists


def main():
    test = random_nums_generator(100,10)
    print('Initial list is:')
    print(test)
    print('**********quick_sort*************')
    
    start_time = time.time()
    r = quick_sort(test,0,len(test)-1)
    end_time = time.time()
    print (end_time-start_time)*1000
    
    print('**********qsort*************')

    start_time = time.time()
    print qsort(test)
    
    end_time = time.time()
    print(end_time*1000-start_time*1000)
    
if __name__ =='__main__':
    main()
    
    
def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    res = 0
    while l1 or l2:
        x = 0 if l1 == None else l1.val
        y = 0 if l2 == None else l2.val
        res = x + y + carry
        if res > 9:
            carry = int(res/10)
            res = res%10
        cur.next = ListNode(res)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next
    
    
            
        
        
        
        
        
        
        