def find_lcm(a, b):
    max_num = max(a, b)

    while True:
        if max_num % a == 0 and max_num % b == 0:
            lcm = max_num
            break
        max_num += 1
    return lcm
a, b = map(int, input().split())
lcm = find_lcm(a, b)
print(lcm)
