# q1

# salary=int(input("enter your salary: "))
# yearofservice=int(input("enter your years of service: "))

# if yearofservice > 5:
#     bonus= 0.05 * salary
#     total= (0.05 * salary)+salary
#     print(f"you are eligble for the bonus. your full amount is : {bonus} + {salary} = {total}")
# else:
#     print("you are not eligble for bonus")

# q2

# unit=int(input("enter the unit : "))

# if unit <= 100:
#     bill=0
# elif unit <=200:
#     bill=(unit-100)* 5
# else:
    #  bill =(unit-200)*10 + 500             # """"the 500 is added form the second unit total(100*5=500)"""
# print(f"your bill is : {bill}")


# q3

# day=int(input("enter a no : "))

# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wensday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("satuday")
# else:
#     print("the no is invild")


# q4

# city=(input("enter a city : "))
# if (city=="delhi"):
#     print("red fort")
# elif (city=="agra"):
#     print("taj mahal")
# elif (city=="jaipur"):
#     print("jal")
# else:
#     print("that city is not avalible")


# q5

# no=int(input("enter a number : "))

# lst= no % 10

# if lst % 3==0:
#     print(f"the lst digit of {no} the lst no {lst} is divisble by 3")
# else:
#     print(f"the lst digit of {no} the lst no {lst} is not divisble by 3")


# q6

cost=int(input("enter the cost of the bike : "))

if cost > 100000:
    tax=0.15
    tax=0.15 * cost
    total=(0.05* cost)+cost
elif cost > 50000:
    tax=0.10 * cost
    total=(0.15* cost)+cost

else:
    tax=0.05*cost
    total=(0.05* cost)+cost


print(f"your road tax is {tax}.the total amount is {total}")