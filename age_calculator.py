age_calculator.py

from datetime import date

print("===== AGE CALCULATOR =====")

birth_day = int(input("Enter Birth Day: "))
birth_month = int(input("Enter Birth Month: "))
birth_year = int(input("Enter Birth Year: "))

today = date.today()

age = today.year - birth_year

if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print("\nYour Age is:", age, "years")
