import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, explained_variance_score, max_error,mean_absolute_error, mean_squared_error, mean_squared_log_error, median_absolute_error
import test2
import predictor
import numpy as np

# df = pd.read_csv("./df_cleaned2.csv")
# train, test = train_test_split(df, test_size=0.2)

# type(train)
# x = test2.gb(train, "charges", 0.1)

train1 = pd.read_csv("./train1.csv")
test1 = pd.read_csv("./test1.csv")


print(test1.describe())

trained = test2.gb(train1, "charges", 0.1)

xx = predictor.predictor(test1, 0.1, train1['charges'].mean())
# xx = predictor.predictor(test1, 0.1, trained[0])



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


# print("r22", 1- ssr/sst)

testtt = pd.read_csv("./test1.csv")

print("r2", r2_score(testtt["charges"], xx["Predicted"]))
print("explained_variance_score", explained_variance_score(testtt["charges"], xx["Predicted"]))
print("max_error", max_error(testtt["charges"], xx["Predicted"]))
print("mean_absolute_error", mean_absolute_error(testtt["charges"], xx["Predicted"]))
print("mean_squared_error", mean_squared_error(testtt["charges"], xx["Predicted"]))
print("mean_squared_log_error", mean_squared_log_error(testtt["charges"], xx["Predicted"]))
print("median_absolute_error", median_absolute_error(testtt["charges"], xx["Predicted"]))

