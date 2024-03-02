
from trees import trees_regr

def predictor(dff, l_r, mean_y, est):

    temp_df = dff.copy()

    temp_df["Predicted"]  = mean_y

    for df_i in temp_df.index:
        print(df_i)

        for i in range(est):

            tree_dict = temp_df.loc[df_i].to_dict()

            resi = getattr(trees_regr, f"tree_{i}")(tree_dict)

            temp_df.loc[df_i, "Predicted"] = temp_df.loc[df_i, "Predicted"] + l_r * resi

    return temp_df








        
