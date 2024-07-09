print("Welcome to tip calculator")
bill = float(input("what was the total bill?\n"))
tipper = float(input("How much tip you want?\n"))
spl = float(input("how many people should pay?\n"))


ans = (bill + bill*(tipper/100))/spl
print(f"each person will get: {float(ans)}")
