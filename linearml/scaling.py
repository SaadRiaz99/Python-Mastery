from  sklearn.preprocessing import StandardScaler ,MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

data = {
    'Student_ID': range(1, 16),
    'Study_Hours_Per_Week': [4.5, 9.0, 12.5, 16.0, 20.5, 24.0, 28.5, 32.0, 36.5, 40.0, 15.0, 8.5, 22.0, 30.0, 38.0],
    'Marks_Obtained':       [42,  51,  58,   65,   72,   78,   85,   89,   95,   98,   60,  49,  75,  88,  94]
}
df = pd.DataFrame(data)
features_to_scale = df[['Study_Hours_Per_Week', 'Marks_Obtained']]
standar_scale = StandardScaler()
standard_scaled = standar_scale.fit_transform(features_to_scale)

print("Standard Scaled Data Form")
print(pd.DataFrame(standard_scaled , columns=["Study Hour" , "Marks Obtained"]))


