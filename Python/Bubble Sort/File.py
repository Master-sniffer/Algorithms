def bubble_sort(nums):
    # Делаем так, чтобы цикл хотя бы раз запустился
    swap=True
    while swap:
        swap=False
        for i in range (len (nums)-1):
            if nums[i]>nums[i+1]:
                #Меняем элементы
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swap = True
numbers = [5,2,6,3,1,2,4,5,6,2,131,5,3,4]
bubble_sort(numbers)
print (numbers)
