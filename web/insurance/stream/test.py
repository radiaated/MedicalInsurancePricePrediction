import pandas as pd
import numpy as np
import pickle

from modules import (
    GradientBoosting,
    EncoderPipeline,
    CategoricalLabelEncoder,
    DiscretizationEncoder,
    DecisionTree,
    DecisionNode,
)

with open("encoders_1.pkl", "rb") as file:

    encoders = pickle.load(file)

with open("gb_regression_1.pkl", "rb") as file:

    gb = pickle.load(file)

data = encoders.transform(
    {
        "age": 22,
        "gender": "male",
        "region": "southeast",
        "smoker": "yes",
        "children": 2,
        "occupation": "Unemployed",
        "bmi": 32,
        "medical_history": "no",
        "family_medical_history": "no",
        "exercise_frequency": "Never",
        "coverage_level": "Basic",
    }
)
