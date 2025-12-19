import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

python_group='0'
number='0'
when='daily'
daily=f"python_{python_group}_daily"
weekly=f"python_{python_group}_weekly"
monthly=f"python_{python_group}_monthly"
total_ll=f'python_{python_group}_total_all'

df=pd.read_csv(f'data/results/{total_ll}.csv')

fig, ax = plt.subplots(2,2,figsize=(20, 8))
fig.suptitle('Python_Codewars_results')
plt.xticks(rotation=90)
sns.lineplot(data=df,ax=ax[0,0],x=df.username,y=df.total_completed,color='red').grid(which='both')

plt.ylabel('katalar_soni')
plt.xlabel('foydananuvchilar')
sns.barplot(data=df,ax=ax[0,1],x=df.username,y=df.total_completed,color='black').grid(which='both')
sns.histplot(data=df,ax=ax[1,0],x=df.username,y=df.total_completed,color='green').grid(which='both')
sns.boxplot(data=df,ax=ax[1,1],x=df.username,y=df.total_completed,color='blue').grid(which='both')
plt.ylabel('katalar_soni')
plt.xlabel('foydananuvchilar')
for a in ax.flat:
    a.tick_params(axis='x', rotation=90)


for i in python_group:
    if number in i:
        plt.savefig(f'pictures/codewars_results/python_{python_group}.svg')

plt.tight_layout()
plt.show()







