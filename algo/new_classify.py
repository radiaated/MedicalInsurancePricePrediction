import math
import importlib
from ID3_classify import ID3
from trees import trees_classify
import pandas as pd

open(f"./trees/trees_classify.py", "w").close()

df = pd.read_csv("csv/aug_csv_cleaned3.csv")

dff = df.copy()



for pack in dff["package"].unique():

    dff[f"package_{pack}"] = dff["package"] == pack

dff.drop(columns=["package", "charges"], inplace=True)
dff.drop(columns=["package_Gold","package_Platinum"], inplace=True)

print(dff.keys())

# for i in range(len(dff.index)):

#     if dff.loc[i,"charges"] < 10000:
#         dff.loc[i,"charges"] = "<10000"
#     elif 10000 <= dff.loc[i,"charges"] < 30000:
#         dff.loc[i,"charges"] = "10000-30000"
#     else:
#          dff.loc[i,"charges"] = ">30000"



from sklearn.model_selection import train_test_split

train, test = train_test_split(dff, test_size=0.2, random_state=42)


high_count = len(train[train["package_Bronze"] == True])
low_count = len(train[train["package_Bronze"] == False])

if low_count > high_count:
    high_count, low_count = low_count, high_count


print(high_count)
print(low_count)

te =  math.log(high_count/low_count)



prob =  math.exp(te) / ( 1+ math.exp(te))


train["Prob"] = prob
train["LogOdds"] = te
for t in range(100):

    train1 = train.copy()

    train1["package_Bronze"] = train["package_Bronze"]



    for k in train1.index:
        if train1.loc[k, "package_Bronze"] == True:
            train1.loc[k, "Resi"] = 1 - train1.loc[k, "Prob"]
        elif train1.loc[k, "package_Bronze"] == False:
            train1.loc[k, "Resi"] = 0 - train1.loc[k, "Prob"]

   
    train1 = train1.drop(columns=["package_Bronze"])



    id = ID3(train1,"Resi")
    id.build_tree()
    id.create_tree(f"tree{t}")

    importlib.reload(trees_classify)

    for k in train1.index:
        q = getattr(trees_classify, f"tree{t}")(train1.loc[k].to_dict())
        new_te = train1.loc[k, "LogOdds"] + 0.1 * q
 
        prob = math.exp(new_te) / (1 + math.exp(new_te))
        train1.loc[k, "LogOdds"] = new_te
        train1.loc[k, "Prob"] = prob






def predictor(dfd, l_r):

    dfdd = dfd.copy()

    dfdd["Predicted"]  = te

    ii = 0

    for df_i in dfdd.index:

        for i in range(15):

            q = getattr(trees_classify, f"tree{i}")(dfdd.loc[df_i].to_dict())
            dfdd.loc[df_i, "Predicted"] = dfdd.loc[df_i, "Predicted"] + l_r * q
        print(dfdd)

    for df_i in dfdd.index:

        dfdd.loc[df_i,"Prob"] = math.exp(dfdd.loc[df_i,"Predicted"]) / (1 + math.exp(dfdd.loc[df_i,"Predicted"]))

    
    return dfdd

x = predictor(test, 0.1)


for i in x.index:

    if x.loc[i,"Prob"] < 0.5:
        x.loc[i,"package_Bronze"] = False
    elif x.loc[i,"Prob"] >= 0.5:
        x.loc[i,"package_Bronze"] = True

from sklearn.metrics import accuracy_score

test["package_Bronze"] = test["package_Bronze"].map({True: "yes", False: "no"})

x["package_Bronze"] = x["package_Bronze"].map({True: "yes", False: "no"})



print("Accuracy:", accuracy_score(test["package_Bronze"], x["package_Bronze"]))