import pandas as pd
from .ID3 import ID3
from trees import trees_regr
import importlib



class GB:

    def __init__(self, dff, op, l_r, est):
        self.dff = dff
        self.op = op
        self.l_r = l_r
        self.est = est

    def train(self):

        tmp_df = self.dff.copy()

        mean_op = tmp_df[self.op].mean()
        print(mean_op)
        tmp_df["latest_pred"] = tmp_df[self.op].mean()

        tmp_df.drop(columns=self.op, inplace=True)

        open('./trees/trees_regr.py', 'w').close()

        for resi in range(self.est):

            for i in tmp_df.index:
                tmp_df.loc[i, f"Residual_{resi}"] = self.dff.loc[i, self.op] - tmp_df.loc[i,"latest_pred"]

            tp_lat = tmp_df["latest_pred"]
            tmp_df.drop(columns="latest_pred", inplace=True)

            tree = ID3(tmp_df, f"Residual_{resi}")

            tree.build_tree()
            tree.show_tree()
            tree.create_tree(f"tree_{resi}")

            tmp_df["latest_pred"] = tp_lat

            importlib.reload(trees_regr)

            for i in tmp_df.index:

                qrs = getattr(trees_regr, f"tree_{resi}")(tmp_df.loc[i].to_dict())
                tmp_df.loc[i,"latest_pred"] = tmp_df.loc[i,"latest_pred"] + self.l_r * qrs

            print(f"Tree {resi} Completed:\n {tmp_df}")

            tmp_df.drop(columns=f"Residual_{resi}", inplace=True)

        return mean_op, tmp_df






