from modules.GB_classify import GB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd
from predictor_classify import predictor
import numpy as np

OUTPUT_COL = "package"
L_R = 0.1
EST = 15

df = pd.read_csv("./csv/ds.csv")

for u in df[OUTPUT_COL].unique():
    for k in df.index:
        df.loc[k, f"{OUTPUT_COL}_{u}"] = df.loc[k, OUTPUT_COL] == u
    

df.drop(columns=["charges", "package_Gold", "package_Platinum", "package"], inplace=True)

train, test = train_test_split(df, test_size=0.2, random_state=42)

gb_obj = GB(train, "package_Bronze", 0.1, EST)

te_obj = gb_obj.train()

predicted_result = predictor(test, 0.1, te_obj["logodds"], EST)

test["package_Bronze"] = test["package_Bronze"].map({True: "yes", False: "no"})

predicted_result["Predicted"] = predicted_result["Predicted"].map({True: "yes", False: "no"})



print("Accurancy: ", accuracy_score(test["package_Bronze"], predicted_result["Predicted"]))











