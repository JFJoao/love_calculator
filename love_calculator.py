# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
counting1 = 0
counting2 = 0

T = name1_lower.count("t") + name2_lower.count("t")
counting1 += T
R = name1_lower.count("r") + name2_lower.count("r")
counting1 += R
U = name1_lower.count("u") + name2_lower.count("u")
counting1 += U
E = name1_lower.count("e") + name2_lower.count("e")
counting1 += E

L = name1_lower.count("l") + name2_lower.count("l")
counting2 += L
O = name1_lower.count("o") + name2_lower.count("o")
counting2 += O
V = name1_lower.count("v") + name2_lower.count("v")
counting2 += V
E = name1_lower.count("e") + name2_lower.count("e")
counting2 += E

score_total = int(f"{counting1}{counting2}")
if score_total <10 or score_total > 90:
    print(f"Your score is {score_total}, you go together like coke and mentos.")
elif score_total >40 and score_total < 50:
    print(f"Your score is {score_total}, you are alright togheter.")
else:
    print(f"Your score is {score_total}")
