# 2) მომხმარებელს შემოატანინეთ რიცხვები, ამ რიცხვებისგან შექმენით სია შემდეგ კი დაითვალეთ რამდენი ორნიშნა რიცხვია 


numbers = []

while True:
    num_str = input("Enter a number (type 'done' to finish): ")
    
    if num_str == "done":
        break
    
    num = int(num_str)
    numbers.append(num)

count = 0
for i in numbers:
    if 10 <= i <= 99:
        count += 1

print(numbers)
print("There are", count ,"two-digit numbers in the list.")