
def insertion_sort (nums):
    #Сортировку начинаем со второго элемента, так как считаем, что первый правильный
    for i in range (1, len(nums)):
        item_which_insert= nums[i]
        #Сохраняем на индекс предыдущего элемента
        j=i-1
        # Элементы сортированного сегмента вставляем вперед, если они больше элемента вставки
        while j>=0 and nums[j] > item_which_insert:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]= item_which_insert

random_list_of_nums = [9, 1, 15, 28, 6]  
insertion_sort(random_list_of_nums)  
print(random_list_of_nums)
