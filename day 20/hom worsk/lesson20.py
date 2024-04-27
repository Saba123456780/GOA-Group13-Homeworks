# 3) for loop-ებზე ივარჯიშეთ


user_num = int(input("enter number 1-100: "))

if user_num < 1:
    print("eror")
elif user_num > 100:
    print("eror")
else:
    for i in range( 100,user_num-1,-1):
        if i %2 ==0:
            print(i ,end=" ")


for i in range(100, 80, -2):
    print(i)