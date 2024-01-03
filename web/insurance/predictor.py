
from . import trees_regr

def predictor(dff, l_r, mean_y, est):

    temp_df = dff.copy()
    

    temp_df["Predicted"]  = mean_y

    for df_i in temp_df.index:

        for i in range(est):

            print(i)
            tree_dict = temp_df.loc[df_i].to_dict()

            print(tree_dict)

            resi = getattr(trees_regr, f"tree_{i}")(tree_dict)
            print(resi)
            
            

            temp_df.loc[df_i, "Predicted"] = temp_df.loc[df_i, "Predicted"] + l_r * resi

    return temp_df








        
