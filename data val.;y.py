import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np







file_paths = [
    r'C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Data validation\Daily time stamps\1.2-2.2.csv',
    r'C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Data validation\Daily time stamps\2.4-3.4.csv',
    r'C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Data validation\Daily time stamps\3.4-4.4.csv',
    r'C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Data validation\Daily time stamps\4.4-5.4.csv',
    r'C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Data validation\Daily time stamps\5.4-6.4.csv',
    r'C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Data validation\Daily time stamps\6.4-7.4.csv'
]


    
dataframes = [pd.read_csv(file_path) for file_path in file_paths]


combined_df=pd.concat(dataframes, ignore_index =True)

def find_meter_label(dataframes, index):
    if index < 0 or index >= len(dataframes):
        return None  # Invalid index

    dataframe = dataframes[index]
    if not dataframe.empty and 'Meter Label' in dataframe.iloc[0]:
        return dataframe.iloc[0]['Meter Label']
    else:
        return None
    
    
def print_meter_label_column(dataframes, index):
    if index < 0 or index >= len(dataframes):
        print("Invalid index")
        return

    dataframe = dataframes[index]
    if not dataframe.empty and 'Meter Label' in dataframe.columns:
        meter_label_column = dataframe['Meter Label']
        print(meter_label_column)
    else:
        print("DataFrame is empty or 'Meter Label' column not found")

    

def get_meter_label(dataframes):
    labels=pd.DataFrame()
    for i, df in enumerate(dataframes):
        if 'Meter Label' in df.columns:
            labels[f'Meter Label_{i+1}'] = df['Meter Label']
    return labels 


def get_daily_close_read(dataframes):
    labels=pd.DataFrame()
    for i, df in enumerate(dataframes):
        if 'Daily Close Read' in df.columns:
            labels[f'Meter Label_{i+1}'] = df['Daily Close Read']
    return labels 
    
def combine_dataframes(dataframes):
    meter_labels_df = get_meter_label(dataframes)
    daily_close_read_df = get_daily_close_read(dataframes)
    combined_df = pd.concat([meter_labels_df, daily_close_read_df], axis =1)
    return combined_df


combined_dataframe=combine_dataframes(dataframes)
combined_dataframe.index = combined_dataframe.iloc[:, 0]
combined_dataframe = combined_dataframe.iloc[:, 1:]

print(combined_dataframe)


#x=np.array([5,7])
#y=np.array([2,9])
#print(plt.plot(x,y))

x = combined_dataframe.iloc[:, 0]
y = combined_dataframe.iloc[:, 6]

plt.plot(x, y)
plt.xlabel('Meter Label')
plt.ylabel('Daily Close Read')
plt.title('Meter Label vs Daily Close Read')
plt.show()




