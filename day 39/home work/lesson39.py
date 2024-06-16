#  1) მომხმარებელს შემოატანინეთ ათი რიცხვი, ეს რიცხვები დაამატეთ სიაში, ამ სიიდან დაახარისხეთ ეს რიცხვები ორ ჯგუფად, რიცხვები რომლებიც მეტია 100 ზე და რიცხვები რომლებიც ნაკლებია 100 ზე


numbers = []


for i in range(10):
    num = int(input("შემოიტანეთ რიცხვი: "))
    numbers.append(num)

# მეტია 100-ზე და ნაკლებია 100-ზე რიცხვების ორ ჯგუფად გახარისხება
greater_than_100 = [num for num in numbers if num > 100]
less_than_100 = [num for num in numbers if num < 100]

print("მეტია 100-ზე:", greater_than_100)
print("ნაკლებია 100-ზე:", less_than_100)
