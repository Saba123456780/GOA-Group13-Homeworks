# 2)მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე დაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ


user_mother = int(input("Enter your mother age: "))
user_father = int(input("Enter your father age: "))

if user_mother > user_father:
    print("Mother is older than father")
else:
    print("Father is older than mother")