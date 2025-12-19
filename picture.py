import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

python_group='7'

daily=f"python_{python_group}_daily"
weekly=f"python_{python_group}_weekly"
monthly=f"python_{python_group}_monthly"
total_ll=f'python_{python_group}_total_all'

df=pd.read_csv(f'data/results/{monthly}.csv')

fig, ax = plt.subplots(2,2,figsize=(16, 8))
fig.suptitle('Python_Codewars_results')

sns.lineplot(data=df,ax=ax[0,0],color='red').grid(which='both')
sns.barplot(data=df,ax=ax[0,1],color='black').grid(which='both')
sns.histplot(data=df,ax=ax[1,0],color='blue').grid(which='both')
sns.boxplot(data=df,ax=ax[1,1],color='yellow').grid(which='both')
plt.savefig('pictures/codewars_results/codewars.svg')
plt.show()







