import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
#df.columns[0] = 'TIME'
#print(df.columns)
#df['HRM_POSTURE'] %= 360

plt.plot('Unnamed: 0', 'HRM_HEART_RATE', data=df, color='blue')
plt.plot('Unnamed: 0', 'HRM_RESPERATION_RATE', data=df, color='red')
#plt.plot(0, '', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")

#plt.legend(loc='best')
plt.show()
