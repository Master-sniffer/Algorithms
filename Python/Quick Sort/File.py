def partions(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного

    pivot = nums[(low+high)//2]
    i=low -1
    j=high+1
    while True:
        i+=1
        while nums[i] < pivot:
            i+=1
        
        j-=1
        while nums[j] >pivot:
            j-=1
        
        if i>=j:
            return j
        
        nums[i] , nums[j] = nums[j],nums[i]

def quick_sort(nums):
    #Создаем вспомагательную функцию, которая будет вызывать рекурсию

    def quickSort (items, low, high):
        if low<high :
            # This is the index after the pivot, where our lists are split
            split_index = partions(items,low,high)
            quickSort(items, low, split_index)
            quickSort(items, split_index+1, high)
    
    quickSort(nums,0,len(nums)-1)

# Проверяем, что оно работает
random_list_of_nums = [22, 5, 1, 18, 99]  
quick_sort(random_list_of_nums)  
print(random_list_of_nums) 
