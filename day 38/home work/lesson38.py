# 1) შექმნათ სია სადაც მოათავსებთ თქვენი საყავრელ ფილმების სახელებს(მინიმუმ 10 სახელი), შემდეგ კი მათ დაბეჭდავთ ცალცალკე, 

movies = [
    "solo leveling",
    "koleqcioneri",
    "asterix and obelix",
    "tron legacy",
    "scream",
    "black panter",
    "iron man",
    "wnom",
    "dzidza",
    "spider-man"
]

for movie in movies:
    print(movie)
# 2) შექმნათ სია სადაც მოათავსებთ თქვენი ოჯახის წევრების სახელებს(მინიმუმ 10 სახელი) 
# შემდეგ კი დაბეჭდავთ გრძელ წინადადებაში ყველა სახელს ერთად მაგ. 
# # ჩემი სახელია {თქვენი სახელი} ჩემი დედიკოს სახელია {დედიკოს სახელი} ჩემი მამიკოს სახელია {მამიკოს სახელს}

family_members = {
    "ჩემი": "საბა",
    "ჩემი დედიკოს": "მაკა",
    "ჩემი მამიკოს": "გიზო",
    "ჩემი ძმის": "გაბრიელი",
    "ჩემი ბიცოლას": "ელზა",
    "ჩემი ძიის": "ბექა",
    "ჩემი ბაბუას": "გიო",
    "ჩემი ბებიას": "თამარი"
}

for member, name in family_members.items():
    print(f"{member} სახელია {name}")

# 3) შექმნათ სია სადაც მოათავსებთ თქვენი მეგობრის სახელებს(მინიმუმ 10 სახელი) შემდეგ დაბეჭდავთ მათ ცალცალკე for ლუპის გამოყენებით

friends = ["ლუკა", "საბა", "კახა", "ნიკა", "გიო", "ანდრია", "ალექსანდრე", "მარი", "ნინო", "ანანო"]

for friend in friends:
    print(friend)

# 4) შექმნით სიას სადაც მოათავსებთ თქვენი ყველა ჯგუფელის სახელს და გვარს,
# დაბეჭდავთ მათ ცალცალკე და ყველას დაახასიათებთ მაგ. ანდრია არის ასეთი, ასეთი, ასეთი ...