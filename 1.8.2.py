import random;

def quicksort(nums):
    less = [];
    equal = [];
    greater = [];

    if len(nums) > 1:
        pivot = nums[0];
        for x in nums:
            if x < pivot:
                less.append(x)
            if x == pivot: 
                equal.append(x)
            if x > pivot:
                greater.append(x);
        return quicksort(less)+equal+quicksort(greater);
    else:
        return nums

nums = [];
for x in range(10):
    i = random.randint(0,100);
    nums.append(i);
print('Nieposortowane: ');
print(nums);
print('Posortowane: ');
print(quicksort(nums));