
def contains(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))