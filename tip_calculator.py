print("welcome to the tip calculator!!")
bill = float(input("what was the total bill??"))
tip = (int(input("what percentage? 10,12,15 ?")))
people = (int(input("how many people?")))
bill_with_tip = tip/100 *bill +bill
bill_per_person = bill_with_tip / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay{final_amount} dollars.")