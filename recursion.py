def recursive_search(numbers_list,target,index=0):
    if index == len(numbers_list):
        return -1
    elif numbers_list[index]== target:
        return index
    else: 
        return recursive_search(numbers_list,target,index + 1)
    
user_input = input("Enter a list of numbers separated by space: ")
numbers_list = list(map(int,user_input.split()))
print(numbers_list)
target = int(input("Enter the number you are looking for:"))

search_result = recursive_search(numbers_list,target,)
if search_result != -1 :
    print(f"Number {target} found at index {search_result}")
else:
    print("Number not found in the list")