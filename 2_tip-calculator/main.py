#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

bill = float(input("총 비용은 얼마입니까?  $"))

tip = int(input("팁은 얼마나 주시겠습니까? 10%, 12%, or 15%?"))

people = int(input("몇 명이서 식사하셨습니까?"))

result = round(bill * (1 + tip / 100) / people,2)

print(f"총액은 인당 ${result} 입니다.")
