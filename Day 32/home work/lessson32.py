# 2) გაანალიზეთ, დღევანდელი გაკვეთილი და დაწერეთ მსგავსი მაგალითი თქვნით,

academy = "Goa ari chad akademia"

aca = " "

for i in range(21):
    aca += academy[i]

print(aca)


# 3) დღევანდელი გაკვეთილის მსგავსად შემქენით ცვალდი "goa is the best"
# ფორ ციკლის მეშვეობით და დღეს ნასწავლი ინდექსაციით შეართეთ  "goa is the best" სფეისების გარეშე

Goa = "goa is the best" 

result = " "

for i in range(len(Goa)):
    if Goa[i] != " ":
        result += Goa[i]


print(result)

