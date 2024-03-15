
import numpy as np
import pandas as pd
from trees import trees_classify
import importlib

# df = pd.read_csv("./fake_ds.csv")

def std(x):
    return np.std(x)
   
def std_r(y_std, sd_x_y):
    return y_std - sd_x_y

class ID3:

    tree_code = ""

    def __init__(self, dff, op):
        self.dff = dff
        self.op = op

    def build_tree(self, dff = None, curr_depth=1):
        
        if not isinstance(dff, pd.DataFrame):
            dff = self.dff.copy()
        split_col = ""
        max_std = -1
        y_std = np.std(dff[self.op])
        if len(dff.index) == 0:
            self.tree_code += ("\t" * curr_depth) + f"return 0\n"
        
        elif y_std * y_std < 0.1 or len(dff.index) <= 3 or curr_depth >= 5:

            nom = dff[self.op].sum()
            den = 0

            for k in dff.index:
                # print(dff)
                den += dff.loc[k, "Prob"] * (1 - dff.loc[k, "Prob"])

            



       
            self.tree_code += ("\t" * curr_depth) + f"return {nom / den}\n"
            # return dff[op].mean()
        
        else:
            att_crit = []
            
            for col in dff.keys():

                if not col in ["Prob", "LogOdds", self.op]:
      
                    tmp_df = dff.filter(items=[col, self.op])
                    
                    x = tmp_df.groupby(col).agg([std, "count"])


                    x.columns = ["std", "count"]

                    sd_x_y = 0
                    for u in tmp_df[col].unique():

                        sd_x_y += x["std"][u] * (x["count"][u] / len(tmp_df.index))
                    
                    if y_std - sd_x_y > max_std:
                        max_std = std_r(y_std, sd_x_y)
                        att_crit = self.dff[col].unique()
                        split_col = col
    
            n = True
            for att in att_crit:

                # print("_" + str(att))
                if n:
                    self.tree_code += ("\t" * curr_depth) + f"if tree_dict['{split_col}'] == " + (f"'{att}'" if isinstance(att, str) else str(att)) + ":\n"
                else:
                    self.tree_code += ("\t" * curr_depth) + f"elif tree_dict['{split_col}'] == " + (f"'{att}'" if isinstance(att, str) else str(att)) + ":\n"
                
                n=False

                tmpp_dff = dff
            
                tmpp_dff = tmpp_dff[tmpp_dff[split_col] == att].filter(items=[x for x in dff.keys() if x != split_col])
                self.build_tree(tmpp_dff, curr_depth + 1)

    def show_tree(self):
        # print(self.tree_code)
        pass

    def create_tree(self, tree_name):
        
        self.tree_code = f"\ndef {tree_name}(tree_dict):\n" + self.tree_code
        
        
        ftree = open(f"./trees/trees_classify.py", "a+")
        ftree.write(self.tree_code)
        ftree.close()

# ftree = open(f"./trees/trees_classify.py", "w").close()
# # id = ID3(df,"HoursPlayed")
# # id.build_tree()
# # id.create_tree("tree1")
# import math

# dfff = pd.read_csv("fake_ds2.csv")
# dffff = dfff.copy()

# yes_count = len(dfff[dfff["play"] == "yes"])
# no_count = len(dfff[dfff["play"] == "no"])

# print(yes_count)
# print(no_count)

# te =  math.log(yes_count/no_count)



# prob =  math.exp(te) / ( 1+ math.exp(te))


# dfff["Prob"] = prob
# dfff["LogOdds"] = te
# for t in range(5):

   

#     dfff["play"] = dffff["play"]



#     for k in dfff.index:
#         if dfff.loc[k, "play"] == "yes":
#             dfff.loc[k, "Resi"] = 1 - dfff.loc[k, "Prob"]
#         elif dfff.loc[k, "play"] == "no":
#             dfff.loc[k, "Resi"] = 0 - dfff.loc[k, "Prob"]

   
#     dfff = dfff.drop(columns=["play"])

#     print(dfff)

#     id = ID3(dfff,"Resi")
#     id.build_tree()
#     id.create_tree(f"tree{t}")

#     importlib.reload(trees_classify)

#     for k in dfff.index:
#         q = getattr(trees_classify, f"tree{t}")(dfff.loc[k].to_dict())
#         new_te = dfff.loc[k, "LogOdds"] + 0.9 * q

#         print(q)
 
#         prob = math.exp(new_te) / (1 + math.exp(new_te))
#         dfff.loc[k, "LogOdds"] = new_te
#         dfff.loc[k, "Prob"] = prob

# dfff["play"] = dffff["play"]
# print(dfff)

