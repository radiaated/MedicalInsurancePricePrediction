
import math
from . import trees_classify_BASIC
from . import trees_classify_STANDARD
from . import trees_classify_PREMIUM

def predictor_BASIC(dfd, l_r, te, est):

    d_temp = dfd.copy()

    d_temp["log_odd"]  = te

    for df_i in d_temp.index:

        for i in range(est):

            q = getattr(trees_classify_BASIC, f"tree{i}")(d_temp.loc[df_i].to_dict())
            d_temp.loc[df_i, "log_odd"] = d_temp.loc[df_i, "log_odd"] + l_r * q


    for df_i in d_temp.index:

        prob = math.exp(d_temp.loc[df_i,"log_odd"]) / (1 + math.exp(d_temp.loc[df_i,"log_odd"]))
        d_temp.loc[df_i,"Prob"] = prob


        if prob < 0.5:
            d_temp.loc[df_i,"Predicted"] = False
        elif prob >= 0.5:
            d_temp.loc[df_i,"Predicted"] = True

    
    return d_temp

def predictor_STANDARD(dfd, l_r, te, est):

    d_temp = dfd.copy()

    d_temp["log_odd"]  = te

    for df_i in d_temp.index:

        for i in range(est):

            q = getattr(trees_classify_STANDARD, f"tree{i}")(d_temp.loc[df_i].to_dict())
            d_temp.loc[df_i, "log_odd"] = d_temp.loc[df_i, "log_odd"] + l_r * q


    for df_i in d_temp.index:

        prob = math.exp(d_temp.loc[df_i,"log_odd"]) / (1 + math.exp(d_temp.loc[df_i,"log_odd"]))
        d_temp.loc[df_i,"Prob"] = prob


        if prob < 0.5:
            d_temp.loc[df_i,"Predicted"] = False
        elif prob >= 0.5:
            d_temp.loc[df_i,"Predicted"] = True

    
    return d_temp

def predictor_PREMIUM(dfd, l_r, te, est):

    d_temp = dfd.copy()

    d_temp["log_odd"]  = te

    for df_i in d_temp.index:

        for i in range(est):

            q = getattr(trees_classify_PREMIUM, f"tree{i}")(d_temp.loc[df_i].to_dict())
            d_temp.loc[df_i, "log_odd"] = d_temp.loc[df_i, "log_odd"] + l_r * q


    for df_i in d_temp.index:

        prob = math.exp(d_temp.loc[df_i,"log_odd"]) / (1 + math.exp(d_temp.loc[df_i,"log_odd"]))
        d_temp.loc[df_i,"Prob"] = prob


        if prob < 0.5:
            d_temp.loc[df_i,"Predicted"] = False
        elif prob >= 0.5:
            d_temp.loc[df_i,"Predicted"] = True

    
    return d_temp



