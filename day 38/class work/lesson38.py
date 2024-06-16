# შევქმნათ სია, შემდეგ მომხმარებელს შემოვატანინოთ 10 რიცხვი, ეს 10 რიცხვი დავამატოთ სიაში,
# შევქმნათ მეორე სია სადაც დავამტებთ წინა სიიდან ყველა ლუწ რიცხვს, ასევე შევქმნათ მესამე სია სადაც დავამატებთ პირველი სიიდან ველა კენტ რიცხვს.


numbers = []

for i in range(10):
    number = int(input(f"შეიყვანეთ მთელი რიცხვი {i+1}/10: "))
    numbers.append(number)

print("შევქმნათ პირველი სია:", numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print("შევქმნათ მეორე სია ლუწ რიცხვებით:", even_numbers)

odd_numbers = [num for num in numbers[::2]]
print("შევქმნათ მესამე სია კენტ რიცხვებით:", odd_numbers)
