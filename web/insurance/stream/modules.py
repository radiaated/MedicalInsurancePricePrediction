# Import modules
import numpy as np
import pandas as pd
from abc import ABC


def evaluate(model, X_test: pd.Series, y_test: pd.Series):

    y_test_pred = pd.Series(
        [model.predict(item.to_dict()) for _, item in X_test.iterrows()],
        index=X_test.index,
    )

    mae = np.mean(np.abs(y_test - y_test_pred))

    mse = np.mean(np.square(y_test - y_test_pred))

    r2_score = 1 - (
        np.sum(np.square(y_test - y_test_pred))
        / np.sum(np.square(y_test - np.mean(y_test)))
    )

    return {
        "mae": mae,
        "mse": mse,
        "r2_score": r2_score,
    }


# Helper functions
def cov(values: pd.Series):
    """
    Compute the coefficient of variation (CoV) for a numeric pandas Series.

    The coefficient of variation is defined as the ratio of the standard
    deviation to the mean:

        CoV = std(values) / mean(values)

    Parameters
    ----------
    values : pd.Series
        A pandas Series containing numeric values.

    Returns
    -------
    float
        The coefficient of variation of the input values.
    """

    return np.std(values) / np.abs(np.mean(values))


def stdr_xy(X: pd.Series, y: pd.Series):
    """
    Compute the standard deviation reduction (STDR) of target variable y
    after splitting by the categorical values in X.

    The function calculates:
        STDR = std(y) - sum_over_groups( (n_i / n) * std(y_i) )

    where:
        - y_i is the subset of y corresponding to each unique value in X
        - n_i is the size of each subset
        - n is the total number of samples

    Parameters
    ----------
    X : pd.Series
        A pandas Series containing categorical or discrete grouping values.
    y : pd.Series
        A pandas Series containing numeric target values aligned with X.

    Returns
    -------
    float
        The reduction in standard deviation of y after partitioning by X.
    """

    stdr = 0
    for val in X.unique():

        x_value = X[X == val]
        y_value = y.loc[x_value.index]

        stdr += (len(x_value) / len(X)) * np.std(y_value)

    stdr = np.std(y) - stdr

    return stdr


def encode_columns(columns: list):

    encoding = {}

    for i in range(len(columns)):

        encoding[i] = columns[i]

    return encoding


class DecisionNode:
    """
    A node in a decision tree structure.

    A DecisionNode can represent either:
    - An internal decision node that splits on a feature and contains branches, or
    - A leaf node that stores a predicted value.

    Parameters
    ----------
    feature_idx : int, optional
        The index of the feature used for splitting at this node.
        Should be None for leaf nodes.
    branches : dict, optional
        A dictionary mapping feature values to child DecisionNode objects.
        Used only for internal (non-leaf) nodes.
    leaf_value : float, optional
        The prediction value stored in the node if it is a leaf.
        Should be None for internal nodes.

    Attributes
    ----------
    feature_idx : int
        Feature index used for splitting at this node.
    branches : dict
        Mapping of feature values to child nodes.
    leaf_value : float
        Prediction value if the node is a leaf.
    """

    def __init__(
        self, feature_idx: int = None, branches: dict = None, leaf_value: float = None
    ):

        self.feature_idx = feature_idx
        self.branches = branches
        self.leaf_value = leaf_value


class DecisionTree:
    """
    A simple Decision Tree implementation for regression tasks.

    The tree splits data based on the feature that maximizes a custom
    standard deviation reduction metric (stdr_xy). Splitting stops when:
    - The number of samples is less than or equal to min_samples
    - The maximum depth is reached
    - The covariance of the target values is below the splitting threshold

    Parameters
    ----------
    splitting_threshold : float
        Minimum covariance threshold required to continue splitting.
    max_depth : int
        Maximum depth allowed for the tree.
    min_samples : int
        Minimum number of samples required to split a node.
    """

    def __init__(
        self, max_depth: int, min_samples: int, splitting_threshold: float = None
    ):
        """
        Initialize the Decision Tree with stopping criteria.

        Parameters
        ----------
        splitting_threshold : float
            Minimum covariance required to continue splitting.
        max_depth : int
            Maximum depth of the tree.
        min_samples : int
            Minimum number of samples required to split.
        """

        # Threshold for covariance stopping condition
        self.splitting_threshold = splitting_threshold

        # Maximum allowed depth of the tree
        self.max_depth = max_depth

        # Minimum number of samples required to perform a split
        self.min_samples = min_samples

        # Root node of the tree (DecisionNode)
        self.root: DecisionNode = None

        self.column_encoding = None

        self.columns_values = None

    def build(self, X_train: pd.DataFrame, y_train: pd.Series, depth: int = 0):
        """
        Recursively builds the decision tree.

        Parameters
        ----------
        X_train : pd.DataFrame
            Feature dataset.
        y_train : pd.Series
            Target values.

        Returns
        -------
        DecisionNode
            A node representing either a leaf or an internal split node.
        """

        # Stopping conditions:
        # 1. Too few samples
        # 2. Maximum depth reached
        # 3. Target covariance is below threshold

        if (
            len(X_train) <= self.min_samples
            or depth >= self.max_depth
            or (self.splitting_threshold and cov(y_train) <= self.splitting_threshold)
        ):

            # Create a leaf node with the mean target value
            return DecisionNode(leaf_value=np.mean(y_train))

        # Track the best standard deviation reduction
        max_stdr = None

        # Feature chosen for splitting
        split_feature = None

        # Iterate over all features to find the best split

        for col in X_train.columns:

            # Compute custom standard deviation reduction metric
            stdr = stdr_xy(X_train[col], y_train)

            # Update best feature if improvement found
            if max_stdr == None or stdr > max_stdr:

                max_stdr = stdr
                split_feature = col

        # Dictionary to store child branches
        branches = {}

        # Create a branch for each unique value of the selected feature
        for col_value in self.columns_values[split_feature]:
            if col_value not in X_train[split_feature].values:
                branches[col_value] = DecisionNode(leaf_value=np.mean(y_train))

            else:

                # Subset of X where feature equals the specific value
                X_col_value = X_train[X_train[split_feature] == col_value]

                if len(X_col_value) == 0:
                    branches[col_value] = DecisionNode(leaf_value=np.mean(y_train))

                else:

                    # Corresponding target values
                    y_col_value = y_train.loc[X_col_value.index]

                    # Remove the splitting feature from the subset
                    X_col_value = X_col_value.drop(split_feature, axis=1)

                    # Recursively build subtree for this branch
                    branches[col_value] = self.build(
                        X_col_value, y_col_value, depth + 1
                    )

        # Return internal decision node
        return DecisionNode(feature_idx=split_feature, branches=branches)

    def fit(self, X_train: pd.DataFrame, y_train: pd.Series):
        """
        Train the Decision Tree on the provided dataset.

        Parameters
        ----------
        X_train : pd.DataFrame
            Training features.
        y_train : pd.Series
            Training target values.
        """

        self.columns_values = {}

        self.column_encoding = encode_columns(X_train.columns)

        reverse_column_encoding = {
            val: key for key, val in self.column_encoding.items()
        }

        X_train = X_train.rename(columns=reverse_column_encoding)
        X_train.columns = X_train.columns.astype(int)

        for col in X_train.columns:
            self.columns_values[col] = X_train[col].unique()

        # Build the tree starting from the root
        self.root = self.build(X_train, y_train)

    def __visualize_node(self, node: DecisionNode, depth=0):
        """
        Recursively prints a visual representation of the tree.

        Parameters
        ----------
        node : DecisionNode
            Current node being visualized.
        depth : int
            Current depth (used for indentation).
        """

        # If this is a leaf node, print its value
        if node.leaf_value:
            print(node.leaf_value)
            return

        # Print feature used for splitting
        print("[ %s ]" % self.column_encoding[node.feature_idx])

        # Recursively print branches
        for feature_value, node in node.branches.items():

            # Indentation based on depth level
            print("\t" * depth + f" -- {feature_value} --> ", end="")

            self.__visualize_node(node, depth=depth + 1)

    def visualize(self):
        """
        Public method to print the full tree structure.
        """

        self.__visualize_node(self.root)

    def __traverse(self, node: DecisionNode, X: dict):
        """
        Recursively traverse the tree to make a prediction.

        Parameters
        ----------
        node : DecisionNode
            Current node in traversal.
        X : dict
            Single sample represented as a dictionary of feature-value pairs.

        Returns
        -------
        float
            Predicted value from the leaf node.
        """

        # If leaf node, return stored prediction
        if node.leaf_value != None:
            return node.leaf_value

        # Get the feature value for current split
        feature_value = X[node.feature_idx]

        # Move to the corresponding child node
        next_node = node.branches.get(feature_value)

        # Continue traversal
        return self.__traverse(next_node, X)

    def predict(self, X: dict):
        """
        Predict the output for a single sample.

        Parameters
        ----------
        X : dict
            Feature dictionary for one data sample.

        Returns
        -------
        float
            Predicted value.
        """

        # Encode the column names of input data to feature idx
        X_inp = X.copy()

        for key, value in self.column_encoding.items():

            X_inp[key] = X_inp.pop(value)

        # Return the predicted value
        return self.__traverse(self.root, X_inp)


class GradientBoosting:
    def __init__(
        self,
        learners_count: int,
        learning_rate: float,
        max_depth: int,
        min_samples: int,
        splitting_threshold: float = None,
    ):
        self.learners_count = learners_count
        self.learning_rate = learning_rate
        self.splitting_threshold = splitting_threshold
        self.max_depth = max_depth
        self.min_samples = min_samples
        self.learners = None
        self.f_c = None

    def fit(
        self, X_train: pd.DataFrame, y_train: pd.Series, validation_data: list = None
    ):
        self.f_c = np.mean(y_train)
        f_x = pd.Series([self.f_c] * len(y_train), index=y_train.index)

        for i in range(self.learners_count):

            print("Training Learner: ", i + 1)

            residual = y_train - f_x
            d_t = DecisionTree(
                splitting_threshold=self.splitting_threshold,
                max_depth=self.max_depth,
                min_samples=self.min_samples,
            )
            d_t.fit(X_train, residual)

            if self.learners:
                self.learners.append(d_t)
            else:
                self.learners = [d_t]

            f_x += self.learning_rate * pd.Series(
                [d_t.predict(row.to_dict()) for _, row in X_train.iterrows()],
                index=y_train.index,
            )

            if validation_data != None:

                print(evaluate(self, validation_data[0], validation_data[1]))

    def predict(self, X: dict):
        y_pred = self.f_c + sum(
            (self.learning_rate * learner.predict(X)) for learner in self.learners
        )
        return y_pred


class BaseEncoder(ABC):
    """Base encoder class for custom encoding strategies."""

    def fit_transform(self, X: pd.DataFrame, columns: list | dict):
        pass

    def transform(self, X: dict):
        pass


class CategoricalLabelEncoder(BaseEncoder):
    """Encoder for label encoding multiple categorical columns."""

    def __init__(self):
        self.encoding = None

    def fit_transform(self, X: pd.DataFrame, columns: list):
        X_ = X.copy()
        self.encoding = {}

        for column in columns:
            self.encoding[column] = {
                value: i for i, value in enumerate(X_[column].unique())
            }

        for column in columns:
            for col_value in self.encoding[column].keys():
                X_[column] = X_[column].replace(
                    col_value, self.encoding[column][col_value]
                )

        return X_

    def transform(self, X: dict):
        X_ = X.copy()

        for column, column_encoding in self.encoding.items():
            X_[column] = column_encoding[X_[column]]

        return X_


class DiscretizationEncoder(BaseEncoder):
    """Encoder for discretizing continuous features into specified intervals."""

    def __init__(self):
        self.encoding = None

    def fit_transform(self, X: pd.DataFrame, columns: dict):
        X_ = X.copy()
        self.encoding = columns

        for column, col_discrete_infos in columns.items():
            for col_discrete_info in col_discrete_infos:
                if not col_discrete_info[1]:
                    X_[column] = X_[column].apply(
                        lambda x: (
                            col_discrete_info[0] if x < col_discrete_info[2] else x
                        )
                    )
                elif not col_discrete_info[2]:
                    X_[column] = X_[column].apply(
                        lambda x: (
                            col_discrete_info[0] if x >= col_discrete_info[1] else x
                        )
                    )
                else:
                    X_[column] = X_[column].apply(
                        lambda x: (
                            col_discrete_info[0]
                            if (x >= col_discrete_info[1])
                            and (x < col_discrete_info[2])
                            else x
                        )
                    )

        return X_

    def transform(self, X: dict):
        X_ = X.copy()

        for column, col_discrete_infos in self.encoding.items():
            t = filter(
                lambda col_discrete_info: (
                    X_[column] < col_discrete_info[2]
                    if not col_discrete_info[1]
                    else (
                        X_[column] >= col_discrete_info[1]
                        if not col_discrete_info[2]
                        else X_[column] >= col_discrete_info[1]
                        and X_[column] < col_discrete_info[2]
                    )
                ),
                col_discrete_infos,
            )

            X_[column] = list(t)[0][0]

        return X_


class EncoderPipeline:
    """Pipeline for applying multiple encoders sequentially."""

    def __init__(self):
        self.encoders = []

    def fit_transform(self, X: pd.DataFrame, encoders: list):
        X_ = X.copy()

        for encoder in encoders:
            X_ = encoder[0].fit_transform(X_, encoder[1])
            self.encoders.append(encoder[0])

        return X_

    def transform(self, X: dict):
        X_ = X.copy()

        for encoder in self.encoders:
            X_ = encoder.transform(X_)

        return X_
