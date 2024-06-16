initial_price = int(input("enter product price: "))

discount_percentage = 20

discount_amount = initial_price * discount_percentage / 100

new_price = initial_price - discount_amount

print("new price is", new_price)



kenti = []
luwi = []

number = int(input("enter number: "))

if number % 2 != 0:
    kenti.append(number)
else:
    luwi.append(number)

print("კენტების სია", kenti)
print("ლუწების სია", luwi)