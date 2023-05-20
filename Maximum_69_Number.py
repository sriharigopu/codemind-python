def maximum69Number(num):
    num_str = str(num)
    max_num = num 
    for i in range(len(num_str)):
        if num_str[i] == '6': 
            new_num = num_str[:i] + '9' + num_str[i+1:] 
        else: 
            new_num = num_str[:i] + '6' + num_str[i+1:] 
        max_num = max(max_num, int(new_num)) 
    return max_num
num = int(input())
print(maximum69Number(num))