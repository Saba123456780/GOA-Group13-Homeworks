# შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს

def sum_of_numbers(numbers):
    total = sum(numbers)
    return total

numbers_list = [1, 2, 3, 4, 5]

result = sum_of_numbers(numbers_list)
print(f"რიცხვების ჯამია: {result}")
