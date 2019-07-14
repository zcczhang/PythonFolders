import pandas as pd
import matplotlib.pyplot as plt


def clean_plot():
    aqi_data1 = pd.read_csv('Real Time AQI of Major Cities in the World.csv', na_values=['-'])
    aqi_data = aqi_data1.copy()
    for i in aqi_data.index:
        aqi_data['City'][i] = aqi_data1['City'][i].split('(')[0]
    # save as csv by pd without import csv
    aqi_data.to_csv('Cleaned: Real Time AQI of Major Cities in the World.csv', index=False)

    top50_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI',
                      title='Top 50 Major City with the Worst AQI in the World', figsize=(20, 10))

    plt.show()


clean_plot()
