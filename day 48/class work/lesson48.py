# მოცემულია სია, რომელშიც მოთავასებულია 10 ელემენტი ჩვენ ეს ელემეტები უნდა დავპრინტოთ

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for element in elements:
    print(element)


# ევქმნათ ცარიელი სია, მომხმარებელს შევეკითხოთ 1000 ჯერ თუ რისი დამატება სურს სიაში

elements = []


for _ in range(1000):
    item = input("გთხოვთ დაამატეთ სიაში რაც გინდათ ")
    elements.append(item)

print("სიის ელემენტები:")
for element in elements:
    print(element)


# შევქმანათ ცარიელი სია, სადაც დავამატებთ მომხარებლის მიერ არჩეულ სიტყვას მაგრამ ყურადღებით იყავით რომ ეს სიტყვა არ აღემატებოდეს 6 ასოს

elements = []

while True:
    word = input("გთხოვთ შეიყვანოთ სიტყვა (ან შეიყვნეთ 'stop' სიის დასრულებისათვის): ")
    
    if word.lower() == "stop":
        break
    if len(word) <= 6:
        elements.append(word)
    else:
        print("შეიყვანეთ სიტყვა, რომელიც არ აღემატება 6 ასოს.")


print("სიის ელემენტები:")
for element in elements:
    print(element)

# შევქმნათ ცარიელი სია, სიაში დავამატოთ, კიდევ 2 სია და გადავატაროთ for loop ში

list1 = []
list2 = []
list3 = []


list1.extend(["პირველი", "ელემენტი", "ლისტი"])
list2.extend(["მეორე", "ელემენტი", "ლისტი"])
list3.extend(["მესამე", "ელემენტი", "ლისტი"])

lists = [list1, list2, list3]

for lst in lists:
    print("სიაში არსებული ელემენტები:")
    for element in lst:
        print(element)
    print()  


# შექმნილი არის სია სადაც წერია, ჩვენი სახელი და გვარი, str სახით
#  მიზანია, რომ წამოვიღოთ ეს სტრინგები და შევართოთ ერთ ცვლადში


name_list = ["saba", "nakashidze"]

full_name = " ".join(name_list)

print("თქვენი სრული სახელი არის:", full_name)

# შექმენით ქართული მამაპაპური list დაარქვით S_A_Q_A_R_T_V_E_L_O
# შეეკითხეთ მომხმარებელს ქართველი ფეხბურთელების სახელები 12 ჯერ და დაამატეთ სიაში

S_A_Q_A_R_T_V_E_L_O = []

for i in range(12):
    player_name = input("შეიყვანეთ ქართველი ფეხბურთელების სახელი: ")
    S_A_Q_A_R_T_V_E_L_O.append(player_name)

print("დამატებული ფეხბურთელების სახელები: ")
for name in S_A_Q_A_R_T_V_E_L_O:
    print(name)