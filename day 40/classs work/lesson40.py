# 1) მომხმარებელს შემოვატანინოთ 10 რიცხვი შემდეგ დავამატოთ სიაში, გავფილტროთ ეს სია ორ ნაწილად ლუწებად და კენტებად და დავამატოთ ახალ სიაში 
# ლუწები ცალკე კენტები ცალკე


number = []
odd = []
even = []
for i in range(5):
    num = int(input("Enter number: "))
    number.append(num)

for i in range(len(number)):
    if number[i] % 2 == 0:
      even.append(number[i])
    else:
       odd.append(number[1])

print(odd)
print(even)