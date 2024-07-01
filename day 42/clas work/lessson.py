# 1) შევქმნათ სია  რომელშიც გვექნება დადებითი და უარყოფითი რიცხვები. გავფილტროთ, უნდა დავაბრუნოთ ორი სია ერთში მხოლოდ დადებითი რიცხვები მეორეში მხოლოდ უარყოფითი რიცხვები

number = [1, -1 ,0 ,-5, 99, -3, 999, 0, 40, -90]

negative_number = []
pozitive_number = []

for i in range(len(number)):
    if number[i] == 0:
        continue
    elif number[i] < 0:
        pozitive_number.append(number[i])
    else:
        negative_number.append(number[i])

print("negative number is: ", negative_number)
print("pozitive number is: ", pozitive_number)