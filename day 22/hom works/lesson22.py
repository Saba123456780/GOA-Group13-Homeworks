# 2) ივარჯიშეთ ძალიან ბევრი while ლუპზე


# 1)

num = 0
while num < 11:
  print(num)
  num += 1

# 2)

number = 0
while number < 10:
  number += 1
  if number == 3:
    continue
  print(number)

# 3)

user_phone_number = 571021155 

user_input = int(input("enter your phone number"))

while user_input == user_phone_number:
  print("swori nomeria")
  break
else:
  user_input != user_phone_number
  print("arasworia gtxovt tavidan sheiyvanmet")
