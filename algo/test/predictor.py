import test2
import pandas as pd
from trees import trees_new_cv
from sklearn.model_selection import train_test_split
import math

# df = pd.read_csv("./df_cleaned.csv")

# train, test = train_test_split(df, test_size=0.2)

def predictor(dff, l_r, mean_y):

    dff["Predicted"]  = mean_y

    ii = 0

    for df_i in dff.index:

        for i in range(100):

            tree_dict = dff.loc[df_i].to_dict()

            # print(tree_dict)
            resi = getattr(trees_new_cv, f"tree_{i}")(tree_dict)

            print(f"Resi_{i}: {resi}")

            dff.loc[df_i, "Predicted"] = dff.loc[df_i, "Predicted"] + l_r * resi

        ii += 1
        print(f"p_{ii}")

    
    return dff

# xx = predictor(test, 0.1, 13443.710835802802)

# xx["diff"] = abs( xx["charges"] - xx["Predicted"] )

# print(xx.describe())







        
