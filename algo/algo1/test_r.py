from modules.GB import GB
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd
from predictor import predictor
import numpy as np
import pprint


test_result = []
def mean_absolute_scale_error(y_true, y_pred):
    mae = np.mean(np.abs(y_true - y_pred))
    scale_factor = np.mean(np.abs(np.diff(y_true)))
    mase = mae / scale_factor
    return mase

def root_mean_square_error(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return rmse

OUTPUT_COL = "charges"
L_R = 0.55
EST = 50

df = pd.read_csv("./csv/cleaned.csv")

df.drop(columns="package", inplace=True)


fold_size = int(0.2 * len(df))
print("Fold size: ", fold_size)
fold = int(len(df) / fold_size)
print("Fold: ", fold)

for kf in range(fold):
    train = pd.DataFrame()
    test = pd.DataFrame()
    start_i = kf * fold_size
    end_i = start_i + fold_size
    test = df.loc[start_i:end_i]
    print("Test: ", start_i, end_i)
    for kf2 in range(fold):
        if not kf2 * fold_size in range(start_i, end_i):
            print("Train: ", kf2 * fold_size, kf2 * fold_size + fold_size)
            train = pd.concat([train, df.loc[kf2 * fold_size: kf2 * fold_size + fold_size - 1]], ignore_index=False, axis=0)



    

    print("Mean: eheh: ", train["charges"].mean())

    gb_obj = GB(train, OUTPUT_COL, L_R, EST)

    gb_obj.train()

    predicted_result = predictor(test, L_R, train[OUTPUT_COL].mean(), EST)
    predicted_result2 = predictor(train, L_R, train[OUTPUT_COL].mean(), EST)


    mse = mean_squared_error(test["charges"],predicted_result["Predicted"])
    rmse = root_mean_square_error(test["charges"],predicted_result["Predicted"])
    r2_score_train = r2_score(train["charges"],predicted_result2["Predicted"])
    r2_score_test = r2_score(test["charges"],predicted_result["Predicted"])
    mae = mean_absolute_error(test["charges"],predicted_result["Predicted"])
    mape = mean_absolute_percentage_error(test["charges"],predicted_result["Predicted"])

    test_result.append({    "mse": mse,
                            "rmse": rmse,
                            "r2_score_train": r2_score_train,
                            "r2_score_test": r2_score_test,
                            "mae": mae,
                            "mape": mape
                        })


    print("mse: ", mse)
    print("rmse: ", rmse)
    print("r2_score_train: ", r2_score_train)
    print("r2_score_test: ", r2_score_test)
    print("mae: ", mae)
    print("mape: ", mape)



pprint.pprint(test_result)







