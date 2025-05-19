
import random

table = int(input("Enter number of table: "))
row = int(input("Enter number of row: "))
column = int(input("Enter number of column: "))

option = int(input("""
Choose your output option: 
1. Starting from 1 and increasing in column direction
2. Output a random value between 1 and 100
Option (1 or 2): """))

for i in range(table):
    print()
    print(f"Table {i + 1}")
    
    if option == 1:
        
        count = 1
        
        for _ in range(row):
            for _ in range(column):
                print(count, end="\t")
                count += 1
                
            print()
            
    elif option == 2:
        
        used = []
        
        for _ in range(row):
            for _ in range(column):
                
                while True:
                    
                    number = random.randint(1, 100)
                    
                    if number not in used:
                        used.append(number)
                        print(number, end=" ")
                        break
            print()        