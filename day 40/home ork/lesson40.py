# 1) გააკეთეთ საკლასო დავალება ხელახლა თქვენით და კარგად გაანალიზეთ და გაიაზრეთ "მომხმარებელს შემოვატანინოთ 10 რიცხვი შემდეგ დავამატოთ სიაში, გავფილტროთ ეს სია ორ ნაწილად ლუწებად და კენტებად და დავამატოთ ახალ სიაში ლუწები ცალკე კენტები ცალკე"


odd_even = []

even = []
odd = []


for i in range(10):
    num = int(input("Enter number: "))
    odd_even.append(num)

for i in range(len(odd_even)):
    if odd_even[i] % 2 == 0:
        even.append(odd_even[i])
    else:
        odd.append(odd_even[i])

print("ლუწების სია",  even)
print(" კენტების სია",  odd)


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

