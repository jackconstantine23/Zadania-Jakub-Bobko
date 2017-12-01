import random;
nums = [];
for x in range(50):
    i = random.randint(0,100);
    nums.append(i);
print('Nieposortowane: ');
print(nums);
sorted = False;
while not sorted:
    sorted = True;
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            sorted = False; 
            nums[i], nums[i+1] = nums[i+1], nums[i];
print('Posortowane: ')
print(nums);
