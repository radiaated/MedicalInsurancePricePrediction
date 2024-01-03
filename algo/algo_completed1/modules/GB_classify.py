import math
from modules.ID3_classify import ID3 as id3_classify
import importlib
from trees import trees_classify


class GB:

    def __init__(self, dff, op, l_r, est):
        self.dff = dff
        self.op = op
        self.l_r = l_r
        self.est = est



    def train(self):

        temp_df = self.dff.copy()

        high_count = len(temp_df[temp_df[self.op] == True])
        low_count = len(temp_df[temp_df[self.op] == False])

        if low_count > high_count:
            high_count, low_count = low_count, high_count


        print(high_count)
        print(low_count)

        te =  math.log(high_count/low_count)



        prob =  math.exp(te) / ( 1+ math.exp(te))


        temp_df["Prob"] = prob
        temp_df["LogOdds"] = te
        open('./trees/trees_classify.py', 'w').close()

        for t in range(self.est):

            dfff = temp_df.copy()

            dfff[self.op] = self.dff[self.op]



            for k in dfff.index:
                if dfff.loc[k, self.op] == True:
                    dfff.loc[k, "Resi"] = 1 - dfff.loc[k, "Prob"]
                elif dfff.loc[k, self.op] == False:
                    dfff.loc[k, "Resi"] = 0 - dfff.loc[k, "Prob"]

        
            dfff = dfff.drop(columns=[self.op])
            


            id = id3_classify(dfff,"Resi")
            id.build_tree()
            id.create_tree(f"tree{t}")

            importlib.reload(trees_classify)

            for k in dfff.index:
                q = getattr(trees_classify, f"tree{t}")(dfff.loc[k].to_dict())
                new_te = dfff.loc[k, "LogOdds"] + 0.1 * q
        
                prob = math.exp(new_te) / (1 + math.exp(new_te))
                dfff.loc[k, "LogOdds"] = new_te
                dfff.loc[k, "Prob"] = prob

        return {"logodds": te}