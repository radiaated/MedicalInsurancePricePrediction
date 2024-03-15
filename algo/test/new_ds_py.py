from test2 import gb
import pandas as pd
from predictor import predictor


df = pd.read_csv("csv/aug_csv_cleaned3.csv")

print(df.keys())



from sklearn.model_selection import train_test_split

train, test = train_test_split(df, test_size=0.2, random_state=42)

q = gb(train, "charges", 0.1)
x = predictor(test, 0.1, train["charges"].mean())

from sklearn.metrics import r2_score

acc = r2_score(test["charges"], x["Predicted"])
print(acc)