def selection_sort(nums):
    # Значение i соответствует кол-во отсортированных значений
    for i in range(len (nums)):
        lowest_number_ind = i
        # этот цикл перебирает несортированные массивы 
        for j in range (i+1, len(nums)):
            if nums[j]<nums[lowest_number_ind]:
                lowest_number_ind=j
        nums[i], nums[lowest_number_ind] = nums[lowest_number_ind] , nums[i]

numbers=[1,5,3,5,16,3,6,4,6,7,2131,514,613,4112,26323,7262,24252]
selection_sort(numbers)
print (numbers)

