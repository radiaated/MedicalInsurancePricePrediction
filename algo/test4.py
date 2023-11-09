import pandas as pd
from sklearn.model_selection import train_test_split
import test2
import predictor
import numpy as np

df = pd.read_csv("./df_cleaned.csv")
train, test = train_test_split(df, test_size=0.2)

# type(train)
# x = test2.gb(train, "charges", 0.1)

trained = test2.gb(train, "charges", 0.1)

xx = predictor.predictor(test, 0.1, trained[0])



# xx["diff"] = abs( xx["charges"] - xx["Predicted"] )



# print(xx)

# xx["sq_diff"] = numpy.square(xx["diff"])

# print(xx)


# mae = xx['diff'].sum() / len(xx.index)

# print(f"MAE: {mae}")
# print(f"max: {xx['charges'].max()}")
# print(f"min: {xx['charges'].min()}")
# print(f"mean: {xx['charges'].mean()}")

ssr = np.mean(np.square(xx["charges"] - xx["Predicted"]))

sst = np.mean(np.square(xx["charges"] - np.mean(xx["charges"])))


print(1- ssr/sst)