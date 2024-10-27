print("Welcome to the tip calculator! ")

total_bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * total_bill + total_bill #or total_bill * (1+ tip/100)

bill_per_person = bill_with_tip / people

print(f"Each person should pay: ${bill_per_person}")