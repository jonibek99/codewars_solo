import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
daily='daily'
weekly='weekly'
monthly='monthly'
total_all='total_all'
python_group = '2'


when =total_all

if when == 'daily':
    file_name = f"python_{python_group}_daily"
elif when == 'weekly':
    file_name = f"python_{python_group}_weekly"
elif when == 'monthly':
    file_name = f"python_{python_group}_monthly"
else:
    file_name = f"python_{python_group}_total_all"  

df = pd.read_csv(f'data/results/{file_name}.csv')


#os.makedirs('pictures/codewars_results', exist_ok=True)
os.makedirs(f'when/{when}', exist_ok=True)  

fig, ax = plt.subplots(2, 2, figsize=(30, 15))
fig.suptitle(f'Python Codewars Results - {when.capitalize()}')


sns.lineplot(data=df, ax=ax[0, 0], x='username', y='total_completed', color='red',size=10)
ax[0, 0].grid(which='both')
ax[0, 0].set_ylabel('katalas_capacity')
ax[0, 0].set_xlabel('users')
ax[0, 0].tick_params(axis='x', rotation=90)


sns.barplot(data=df, ax=ax[0, 1], x='username', y='total_completed', color='black')
ax[0, 1].grid(which='both')
ax[0, 1].set_ylabel('katas_number')
ax[0, 1].set_xlabel('users')
ax[0, 1].tick_params(axis='x', rotation=90)


sns.histplot(data=df['total_completed'], ax=ax[1, 0], color='green', kde=True)
ax[1, 0].grid(which='both')
ax[1, 0].set_ylabel('cpacity')
ax[1, 0].set_xlabel('katas_number')
ax[1, 0].tick_params(axis='x', rotation=90)


sns.boxplot(data=df, ax=ax[1, 1], x='username', y='total_completed', color='blue')
ax[1, 1].grid(which='both')
ax[1, 1].set_ylabel('katas_number')
ax[1, 1].set_xlabel('users')
ax[1, 1].tick_params(axis='x', rotation=90)


#plt.savefig(f'pictures/codewars_results/python_{python_group}_{when}.svg', bbox_inches='tight')
plt.savefig(f'when/{when}/python_{python_group}.svg', bbox_inches='tight')

plt.tight_layout()
plt.show()

print(f"Grafiks_saved")
#print(f"1. pictures/codewars_results/python_{python_group}_{when}.svg")
print(f"2. when/{when}/python_{python_group}.svg")

