import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
#df.columns[0] = 'TIME'
#print(df.columns)
df['HRM_POSTURE'] %= 360

#df.plot(x='Unnamed: 0', secondary_y=['HRM_HEART_RATE', 'HRM_RESPERATION_RATE'], color='blue')
df['HRM_HEART_RATE'].plot()
df['HRM_RESPERATION_RATE'].plot(secondary_y=True)
#df.plot(x='Unnamed: 0', y='HRM_RESPERATION_RATE', secondary_y=True, color='red')
#plt.plot(0, '', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")

#plt.legend(loc='best')
plt.show()
