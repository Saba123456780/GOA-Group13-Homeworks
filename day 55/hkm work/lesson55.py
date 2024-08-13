# დაწერე ფუნქცია, რომელიც იღებს x და y პარამეტრებს და აბრუნებს მათ სხვაობას. მაგალითად, გამოიყენე არგუმენტები 10 და 5. (გამოიტანა: 5)

def difference(x, y):
    return x - y

result = difference(10, 5)
print(result)

# შექმენი ფუნქცია, რომელიც იღებს word1 და word2 პარამეტრებს და აბრუნებს მათ ერთად შერწყმულს. მაგალითად, გამოიყენე არგუმენტები "გამარჯობა" და "მეგობარო". (გამოიტანა: "გამარჯობა მეგობარო")

def concatenate_words(word1, word2):
    return word1 + " " + word2

result = concatenate_words("გამარჯობა", "მეგობარო")
print(result)

# დაწერე ფუნქცია, რომელიც იღებს length და width პარამეტრებს და ითვლის მართკუთხედის ფართობს. მაგალითად, გამოიყენე არგუმენტები 4 და 6. (გამოიტანა: 24)

def rectangle_area(length, width):
    return length * width

result = rectangle_area(4, 6)
print(result)

# შექმენი ფუნქცია, რომელიც იღებს name პარამეტრს და აბრუნებს "გამარჯობა, [name]" შეტყობინებას. მაგალითად, გამოიყენე არგუმენტი "ანა". (გამოიტანა: "გამარჯობა, ანა")

def greet(name):
    return f"გამარჯობა, {name}"

result = greet("ანა")
print(result)

# შექმნი ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "დიდია" თუ number 10-ზე მეტია და "პატარა" თუ ნაკლებია. მაგალითად, გამოიყენე არგუმენტი 9. (გამოიტანა: "პატარა")

def check_number(number):
    if number > 10:
        return "დიდია"
    else:
        return "პატარა"

result = check_number(9)
print(result)

# დაწერე ფუნქცია, რომელიც აბრუნებს შეტყობინებას "კარგი დღე გქონდეს!". პარამეტრები არ არის საჭირო.

def good_day_message():
    return "კარგი დღე გქონდეს!"

result = good_day_message()
print(result)

# შექმნი ფუნქცია, რომელიც იღებს a და b პარამეტრებს და აბრუნებს მათ ჯამს. მაგალითად, გამოიყენე არგუმენტები 7 და 3. (გამოიტანა: 10)

def sum_of_two(a, b):
    return a + b

result = sum_of_two(7, 3)
print(result)

# დაწერე ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს number-ის კუბს. მაგალითად, გამოიყენე არგუმენტი 3. (გამოიტანა: 27)

def cube(number):
    return number ** 3

result = cube(3)
print(result)

# შექმენი ფუნქცია, რომელიც აბრუნებს შეტყობინებას "საუკეთესო ხარ!". პარამეტრები არ არის საჭირო.

def best_message():
    return "საუკეთესო ხარ!"

result = best_message()
print(result) 

# დაწერე ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "კენტი" ან "ლუწი". მაგალითად, გამოიყენე არგუმენტი 8. (გამოიტანა: "ლუწი")

def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

result = even_or_odd(8)
print(result)

