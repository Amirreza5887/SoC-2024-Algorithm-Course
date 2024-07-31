n = int(input())
input_arr = input()

array =input_arr.split()
array = [int(number) for number in array] 

def unique_counter(arr) :

    temp = []
    for i in arr :
        if i not in temp:
            temp.append(i)

    return len(temp)

print(unique_counter(array))





