import pandas as pd
from ID3 import ID3
from trees import trees_new_cv
import importlib



# df = pd.read_csv("./fake_ds.csv")


def gb(dff, op, l_r):

    tmp_df = dff.copy()

    mean_op = tmp_df[op].mean()
    print(mean_op)
    tmp_df["latest_pred"] = tmp_df[op].mean()

    tmp_df.drop(columns=op, inplace=True)

    open('./trees/trees_new_cv.py', 'w').close()

    for resi in range(100):

        # print(f"\n{tmp_df}")

        for i in tmp_df.index:
            tmp_df.loc[i, f"Residual_{resi}"] = dff.loc[i, op] - tmp_df.loc[i,"latest_pred"]

        tp_lat = tmp_df["latest_pred"]
        tmp_df.drop(columns="latest_pred", inplace=True)

        tree = ID3(tmp_df, f"Residual_{resi}")

        tree.build_tree()
        tree.show_tree()
        tree.create_tree(f"tree_{resi}")

        tmp_df["latest_pred"] = tp_lat

        importlib.reload(trees_new_cv)

        for i in tmp_df.index:
            # print(f"record:\n", tmp_df.loc[i])
            qrs = getattr(trees_new_cv, f"tree_{resi}")(tmp_df.loc[i].to_dict())
            tmp_df.loc[i,"latest_pred"] = tmp_df.loc[i,"latest_pred"] + l_r * qrs

        print(f"Tree {resi} Completed:\n {tmp_df}")

        tmp_df.drop(columns=f"Residual_{resi}", inplace=True)

    return mean_op, tmp_df






