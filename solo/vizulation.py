import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
daily='daily'
weekly='weekly'
monthly='monthly'
total_all='total_all'
python_group = '8'


when = daily # Bu yerni o'zgartiring: 'daily', 'weekly', yoki 'monthly'

# when qiymatiga qarab fayl nomini aniqlash
if when == 'daily':
    file_name = f"python_{python_group}_daily"
elif when == 'weekly':
    file_name = f"python_{python_group}_weekly"
elif when == 'monthly':
    file_name = f"python_{python_group}_monthly"
else:
    file_name = f"python_{python_group}_daily"  # default

df = pd.read_csv(f'data/results/{file_name}.csv')

# Papkalarni yaratish
#os.makedirs('pictures/codewars_results', exist_ok=True)
os.makedirs(f'when/{when}', exist_ok=True)  # when papkasiga qarab alohida papka

fig, ax = plt.subplots(2, 2, figsize=(40, 15))
fig.suptitle(f'Python Codewars Results - {when.capitalize()}')

# 1. Line plot
sns.lineplot(data=df, ax=ax[0, 0], x='username', y='total_completed', color='red')
ax[0, 0].grid(which='both')
ax[0, 0].set_ylabel('katalar_soni')
ax[0, 0].set_xlabel('foydananuvchilar')
ax[0, 0].tick_params(axis='x', rotation=90)

# 2. Bar plot
sns.barplot(data=df, ax=ax[0, 1], x='username', y='total_completed', color='black')
ax[0, 1].grid(which='both')
ax[0, 1].set_ylabel('katalar_soni')
ax[0, 1].set_xlabel('foydananuvchilar')
ax[0, 1].tick_params(axis='x', rotation=90)

# 3. Histplot
sns.histplot(data=df['total_completed'], ax=ax[1, 0], color='green', kde=True)
ax[1, 0].grid(which='both')
ax[1, 0].set_ylabel('soni')
ax[1, 0].set_xlabel('katalar_soni')
ax[1, 0].tick_params(axis='x', rotation=90)

# 4. Boxplot
sns.boxplot(data=df, ax=ax[1, 1], x='username', y='total_completed', color='blue')
ax[1, 1].grid(which='both')
ax[1, 1].set_ylabel('katalar_soni')
ax[1, 1].set_xlabel('foydananuvchilar')
ax[1, 1].tick_params(axis='x', rotation=90)

# Ikkala joyga saqlash
#plt.savefig(f'pictures/codewars_results/python_{python_group}_{when}.svg', bbox_inches='tight')
plt.savefig(f'when/{when}/python_{python_group}.svg', bbox_inches='tight')

plt.tight_layout()
plt.show()

print(f"Grafiklar saqlandi:")
#print(f"1. pictures/codewars_results/python_{python_group}_{when}.svg")
print(f"2. when/{when}/python_{python_group}.svg")