
def calculate_average(*args):
    
    nums = len(args)
    
    total = 0
    for arg in args:
        total += arg
    
    avg = total / nums
    
    return nums, total, avg

n, s, avg = calculate_average(70, 80, 90)
print(f"""
입력 개수: {n}
총합: {s}
평균: {avg:.2f}""")

n, s, avg = calculate_average(70, 80, 90, 100, 200)
print(f"""
입력 개수: {n}
총합: {s}
평균: {avg:.2f}""")
