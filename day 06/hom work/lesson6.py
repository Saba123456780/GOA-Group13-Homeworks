#  2) დღევანდელი ნასწავლი მასალის გამოყენებით, გააკეთეთ პროგრამა რომელიც მომხმარებელს შეეკითხება მის სახელს გვარს საკს საცხოვრებელს და შემდეგ დაბეჭდავს ამ ყველაფერს ტერმილანში ერთი დიდი წინადადების სახით, და ასევე    დაბეჭდავს თუ რამდენი წლის იქნება მომხმარებელი 20 წლის შემდეგ



user_num = input("Enter your name: ")
user_lastname = input("Enter your last name: ")
user_adress = input("Enter your adress: ")
user_age = int(input("Enter your age: "))

print(user_num, user_lastname, user_adress, user_age + 20)