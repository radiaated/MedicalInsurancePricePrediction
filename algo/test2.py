import pandas as pd
from ID3 import ID3
from trees import trees
import importlib



df = pd.read_csv("./fake_ds.csv")


def gb(df, op):

    tmp_df = df.copy()

    mean_op = tmp_df[op].mean()
    tmp_df["latest_pred"] = tmp_df[op].mean()

    tmp_df.drop(columns=op, inplace=True)

    for resi in range(10):

        
        
        for i in tmp_df.index:
            tmp_df.loc[i, f"Residual_{resi}"] = df.loc[i, op] - tmp_df.loc[i,"latest_pred"]

        tmp_df.drop(columns="latest_pred", inplace=True)

        tree = ID3(tmp_df, f"Residual_{resi}")

        tree.build_tree()
        tree.show_tree()
        tree.create_tree(f"tree_{resi}")

        

        importlib.reload(trees)

        for i in tmp_df.index:
            tmp_df.loc[i,"latest_pred"] = 0.1 * getattr(trees, f"tree_{resi}")(tmp_df.loc[i].to_dict()) + mean_op

        print(f"Tree {resi} Completed:\n {tmp_df}")
        tmp_df.drop(columns=f"Residual_{resi}", inplace=True)


        


gb(df, "HoursPlayed")






