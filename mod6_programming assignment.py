from datetime import datetime

# 13.1
current_date = datetime.today()

with open("today.txt", "w") as file:
    file.write(current_date.strftime("%Y-%m-%d"))

# 13.2: Read the date back and parse it
with open('today.txt', 'r') as file:
    today_string = file.read()
print(today_string)

# 13.3
parsed_date = datetime.strptime(today_string, '%Y-%m-%d').date()

print(parsed_date)