
def max_of_three(a, b, c):
    if a >= b and a >= c:
        max_value = a
    elif b >= a and b >= c:
        max_value = b
    else:
        max_value = c
    
    return max_value

print(max_of_three(10, 10, 5))