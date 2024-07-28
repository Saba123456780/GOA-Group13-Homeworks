# შექმენით სია, რომელიც თავდაპირველად იქნება ცარიელი შემდეგ კი ამ სიაში ჩაამატეთ 10 ელემენტი 
my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.append(10)

# შექმენით ორი სია ერთში თქვენი ხელით ჩაწერეთ ლუწი რიცხვები, მეორეში კენტი რიცხვები შემდეგ კი ეს ორი სია გააერთიანეთ extend ის გამოყენებით 
# ლუწი რიცხვების სია
even_numbers = [2, 4, 6, 8, 10]

odd_numbers = [1, 3, 5, 7, 9]

even_numbers.extend(odd_numbers)

print(even_numbers)

#  შექმენით სია რომელშიც იქნება 20 ელემენტი, შემდეგ კი დაბეჭდეთ თითოეული სათითაოდ for loop ის გამოყენებით
# 20 ელემენტის სიის შექმნა
my_list = [i for i in range(1, 21)]

for element in my_list:
    print(element)


# შექმენით რიცხვებით სავსე სია რომელშიც იქნება 1 დან 20 მდე ყველა რიცხვი, შემდეგ კი ამ სიიდან ამოშალეთ ყველა კენტი რიცხვი და დაამატეთ ახალ სიაში, ორივე სია დაბეჭდეთ
# პირველი სია: რიცხვები 1-დან 20-მდე
original_list = [i for i in range(1, 21)]

odd_numbers = [number for number in original_list if number % 2 != 0]

even_numbers = [number for number in original_list if number % 2 == 0]

print("ორიგინალური სია:")
print(original_list)

print("\nკენტი რიცხვების სია:")
print(odd_numbers)

print("\nლუწი რიცხვების სია:")
print(even_numbers)


# შექმენით სია რომელშიც იქნება 10 განსხვავებული რიცხვი შემდეგ კი დაბეჭდეთ ყველა ლისტის ელემენტის ჯამი

numbers = [3, 7, 1, 14, 8, 5, 11, 6, 9, 2]

total_sum = sum(numbers)

print("ელემენტების ჯამი:", total_sum)


# შექმენით რიცხვებით სავსე სია, გამოითვალეთ ამ სიის ელემენტების საშუალო არითმეტიკული

numbers = [4, 8, 15, 16, 23, 42, 7, 9, 11, 13]

total_sum = sum(numbers)

count = len(numbers)

average = total_sum / count

print("საშუალო არითმეტიკული:", average)
