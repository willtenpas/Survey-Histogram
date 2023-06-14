import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#assigning data to a data frame and isolating the submit time
df = pd.read_csv('2023-06-13-survey.csv')
submitTime = pd.to_datetime(df['Timestamp'])

#isolating just the minutes using dt and minute
minuteTime = submitTime.dt.minute
binWidth = max(minuteTime)-min(minuteTime)

#creating the plot
plt.style.use('seaborn')
minuteTime.hist(edgecolor='orange', linewidth=3.0, bins=binWidth)
plt.title('Frequency of the Minute the Survey Was Submitted At')
plt.xlabel('Time')
labels = ['2:{:02d}'.format(i) for i in range(min(minuteTime),max(minuteTime))]
plt.xticks(range(min(minuteTime),max(minuteTime)), labels, rotation='vertical')
plt.show()
plt.savefig('histogram.png')

