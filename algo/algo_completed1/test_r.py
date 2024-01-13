from modules.GB import GB
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd
from predictor import predictor
import numpy as np

OUTPUT_COL = "charges"
L_R = 0.1
EST = 125

df = pd.read_csv("./csv/test.csv")

df.drop(columns="package", inplace=True)

train, test = train_test_split(df, test_size=0.2, random_state=42)

print("Mean: eheh: ", train["charges"].mean())

gb_obj = GB(train, OUTPUT_COL, L_R, EST)

gb_obj.train()

predicted_result = predictor(test, L_R, train[OUTPUT_COL].mean(), EST)

def mean_absolute_scale_error(y_true, y_pred):
    mae = np.mean(np.abs(y_true - y_pred))
    scale_factor = np.mean(np.abs(np.diff(y_true)))
    mase = mae / scale_factor
    return mase

def root_mean_square_error(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return rmse

print("mse: ", mean_squared_error(test["charges"],predicted_result["Predicted"]))
print("rmse: ", root_mean_square_error(test["charges"],predicted_result["Predicted"]))
print("r2_score: ", r2_score(test["charges"],predicted_result["Predicted"]))
print("mae: ", mean_absolute_error(test["charges"],predicted_result["Predicted"]))
print("mape: ", mean_absolute_percentage_error(test["charges"],predicted_result["Predicted"]))







