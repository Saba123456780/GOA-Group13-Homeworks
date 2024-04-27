# 1) მომხმარებელს შემოატანინეთ ტესტში მიღებული ქულა, თუ ქულა მეტია 90 - ზე და ნაკლებია 100 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა სრულიად. თუ მიღებული ქულა მეტია 70 - ზე და  ნაკლებია 80 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით, თუ მიღებული ქულა მეტია 40 -  ზე და ნაკლებია 70 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 500 ლარტით, ხოლო თუ მიღებული ქულა ნაკლებია 40 ზე, მაგ შემტხვევაში დაპრინტეთ, ტქვენ არ დაგიფინანსდებათ სწავლის პროცესი


user_score = int(input("Enter the test score below: "))


if user_score > 90 and user_score < 100:
    print("your studies will be fully funded")

elif user_score > 70 and user_score < 80:
    print("1500 GEL has financed your studies")

elif user_score > 40 and user_score < 70:
    print("500 GEL has financed your studies")

elif user_score < 40:
    print("Your study process was not financed there")
    

# 2) მოსწავლეს შემოატანინეთ სკოლის ტესტში მიღებული ნიშანი, თუ ეს მიღებული ნიშანი უდრის 10 - ს, მაგ შემთხვევაში მასწავლებელმა, მშობელთან შეაქოს მოსწავლე, თუ მიღებული ნიშანი უდრის 8 -ს ან 9 - ს, მაგ შემთხვევაში, მასწავლებელმა, მშობელს პატარა შენიშვნა მისცეს. თუ მიღებული ქულა უდრის 5  - ს მაგ შემთხვევაში, მასწავლებელმა, მშობელს მისცეს შენიშვნა, ხოლო თუ მიღებული ნიშანი ნაკლებია 5 ზე, მაგ შემთხვევაში, მასწავლებელმა გააგდოს მოსწავლე სკოლიდან

user_score = int(input("Enter the test score below: "))

if user_score == 10:
    print("Your will is very good")

elif user_score == 9 or user_score == 8:
    print("you are a bit lazy!")
elif user_score == 5:
    print("I don't want to do anything and look at me!!")
elif user_score < 5:
    print("Your child does nothing and is expelled from school")
