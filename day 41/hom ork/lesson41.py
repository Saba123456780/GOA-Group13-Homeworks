#  გადმოგვეცემა რიცხვებით სავსე სია, ჩვენ ამ სიიდან უნდა შევკრიბოთ ყველა ხუთის ჯერადი რიცხვი და დავბეჭდოთ
#  მათი ჯამი

number = [1,3,4,5,6,7,8,9,10,30,15,100,370,35,60,]

multiple_five = []

for i in range(len(number)):
    if number[i] % 5 == 0:
        multiple_five.append(number[i])
        
print(sum(multiple_five))
        


