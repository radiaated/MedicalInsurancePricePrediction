import math
from modules.ID3_classify import ID3 as id3_classify
import importlib
from trees import trees_classify


def gb_classify(dff, op, l_r, est, te):

    high_count = len(dff[dff[op] == True])
    low_count = len(dff[dff[op] == False])

    if low_count > high_count:
        high_count, low_count = low_count, high_count


    print(high_count)
    print(low_count)

    te =  math.log(high_count/low_count)



    prob =  math.exp(te) / ( 1+ math.exp(te))


    dff["Prob"] = prob
    dff["LogOdds"] = te
    for t in range(100):

        dfff = dff.copy()

        dfff["package_Bronze"] = dfff["package_Bronze"]



        for k in dfff.index:
            if dfff.loc[k, "package_Bronze"] == True:
                dfff.loc[k, "Resi"] = 1 - dfff.loc[k, "Prob"]
            elif dfff.loc[k, "package_Bronze"] == False:
                dfff.loc[k, "Resi"] = 0 - dfff.loc[k, "Prob"]

    
        dfff = dfff.drop(columns=["package_Bronze"])



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