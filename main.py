from codewars import User, Users
from pprint import pprint
import csv

# Convert dict to CSV file
def dict_to_csv(data, path):
    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# users = []
# Read data from csv file
group ='python_8'

users = []

with open(f'group/{group}.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        users.append({
            'username': row['username'],
            'fullname': row['fullname']
        })
        
# print(users)
users = Users(users)
total_all = users.get_total_all()
dict_to_csv(total_all,f'data/results/{group}_total_all.csv')

daily=users.get_total_daily()
dict_to_csv(daily,f'data/results/{group}_daily.csv')

weekly = users.get_total_weekly()
dict_to_csv(weekly,f'data/results/{group}_weekly.csv')

monthly = users.get_total_monthly()
dict_to_csv(monthly,f'data/results/{group}_monthly.csv')
