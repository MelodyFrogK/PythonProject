print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is their name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

x = (name1+name2).lower()

t = x.count("t")
r = x.count("r")
u = x.count("u")
e = x.count("e")

l = x.count("l")
o = x.count("o")
v = x.count("v")

y = t+r+u+e
z = l+o+v+e
total = int(str(y)+str(z))

if total > 90 or total < 10:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 <= total <=50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")