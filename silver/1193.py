import math

def is_even(int_n):
    if int_n % 2 == 0:
        return True
    else:
        return False

num = float(input())

# 현재 위치 또는 이전 줄을 나타냄
n = (-1 + math.sqrt(1+8*num))/2

#test
#print(n)

if n % 1 == 0:
    int_n = int(n)
    if is_even(int_n):
        print(f"{int_n}/1")
    else:
        print(f"1/{int_n}")
    
else:
    
    pre_n = int(n)
    pre_num = int(pre_n*(pre_n + 1) / 2)
    

    count = int(num - pre_num - 1)
    cur_n = pre_n + 1

    if is_even(cur_n):
        print(f"{1+count}/{cur_n - count}")
    
    else:
        print(f"{cur_n-count}/{1+count}")
        #print(type(count), type(pre_n), type(cur_n))