from calendar import isleap
from datetime import datetime, date
import time
import json
from pathlib import Path

class AgeCalculator:
def __init__(self):
self.months = ['January', 'February', 'March', 'April', 'May', 'June', 
'July', 'August', 'September', 'October', 'November', 'December']

def judge_leap_year(self, year):
return isleap(year)

def month_days(self, month, leap_year):
if month in [1, 3, 5, 7, 8, 10, 12]:
return 31
elif month in [4, 6, 9, 11]:
return 30
elif month == 2 and leap_year:
return 29
elif month == 2 and (not leap_year):
return 28

def get_valid_date(self):
while True:
try:
print("\nEnter your date of birth:")
year = int(input("Year (1900-present): "))
month = int(input("Month (1-12): "))
day = int(input("Day (1-31): "))
# Validate date
current_year = datetime.now().year
if not (1900 <= year <= current_year):
print("Invalid year. Please enter a year between 1900 and present.")
continue
if not (1 <= month <= 12):
print("Invalid month. Please enter a month between 1 and 12.")
continue
max_days = self.month_days(month, self.judge_leap_year(year))
if not (1 <= day <= max_days):
print(f"Invalid day. For {self.months[month-1]} {year}, please enter a day between 1 and {max_days}.")
continue
return year, month, day
except ValueError:
print("Please enter valid numbers.")

def calculate_age(self):
print("Welcome to the Age Calculator!")
name = input("Enter your name: ")
birth_year, birth_month, birth_day = self.get_valid_date()
# Calculate age
today = date.today()
age = today.year - birth_year
if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
age -= 1
# Calculate months and days
total_months = age * 12 + (today.month - birth_month)
# Calculate total days
start_date = date(birth_year, birth_month, birth_day)
days = (today - start_date).days
# Calculate upcoming milestone
next_milestone = (age // 10 + 1) * 10
days_to_milestone = (date(birth_year + next_milestone, birth_month, birth_day) - today).days
# Create results
result = f"\nResults for {name}:\n"
result += f"Age: {age} years\n"
result += f"Age in months: {total_months} months\n"
result += f"Age in days: {days} days\n\n"
result += f"Next age milestone: {next_milestone} years\n"
result += f"Days until next milestone: {days_to_milestone} days\n\n"
# Add fun facts
result += "Fun Facts:\n"
result += f"- You've experienced approximately {age * 365} sunrises\n"
result += f"- You've slept around {int(days * 8/24)} days total\n"
result += f"- Your heart has beaten approximately {int(days * 24 * 60 * 80)} times\n"
print(result)
return result

def save_results(self, results):
try:
filename = f"age_calculation_{int(time.time())}.txt"
with open(filename, 'w') as f:
f.write(results)
print(f"\nResults saved to {filename}")
except Exception as e:
print(f"\nError saving results: {str(e)}")

def load_results(self):
try:
files = list(Path('.').glob('age_calculation_*.txt'))
if not files:
print("\nNo saved results found")
return
latest_file = max(files, key=lambda x: x.stat().st_mtime)
with open(latest_file, 'r') as f:
content = f.read()
print(f"\nLoaded results from {latest_file.name}:")
print(content)
except Exception as e:
print(f"\nError loading results: {str(e)}")

def main():
calculator = AgeCalculator()
while True:
print("\n=== Age Calculator Menu ===")
print("1. Calculate Age")
print("2. Load Previous Results")
print("3. Exit")
choice = input("\nEnter your choice (1-3): ")
if choice == '1':
results = calculator.calculate_age()
save = input("\nWould you like to save these results? (y/n): ")
if save.lower() == 'y':
calculator.save_results(results)
elif choice == '2':
calculator.load_results()
elif choice == '3':
print("\nThank you for using the Age Calculator!")
break
else:
print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
main()