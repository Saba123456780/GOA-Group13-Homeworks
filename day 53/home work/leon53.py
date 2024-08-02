# შექმენით ფუნქცია რომელშიც დააბრუნებს სიაში არსებული რიცხვების საშუალო არითმეტიკულკს
def average_of_numbers(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  
    average = total_sum / count
    return average

numbers_list = [1, 2, 3, 4, 5]

result = average_of_numbers(numbers_list)
print(f"რიცხვების საშუალო არითმეტიკულია: {result}")
