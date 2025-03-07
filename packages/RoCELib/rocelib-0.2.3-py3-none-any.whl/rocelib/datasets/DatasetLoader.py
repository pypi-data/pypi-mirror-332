from abc import ABC, abstractmethod

import pandas as pd


class DatasetLoader(ABC):
    """
    An abstract class used to outline the minimal functionality of a dataset loader

    ...

    Attributes / Properties
    ------------------------

    _data: pd.DataFrame
        Stores the dataset as a DataFrame, only has value once load_data() called

    X: pd.DataFrame
        Stores the feature columns as a DataFrame, only has value once load_data() called

    y: pd.DataFrame
        Stores the target column as a DataFrame, only has value once load_data() called

    -------

    Methods
    -------

    get_negative_instances() -> pd.DataFrame:
        Filters all the negative instances in the dataset and returns them

    get_random_positive_instance() -> pd.Series:
        Returns a random instance where the target variable is NOT the neg_value

    -------
    """

    def __init__(self, target_column_label, neg_value):
        self._data = None
        if target_column_label is None:
            raise ValueError("target_column_label must be provided")
        if neg_value is None:
            raise ValueError("neg_value must be provided")
        self.neg_value = neg_value
        self._target_column_label = target_column_label

    @property
    def data(self) -> pd.DataFrame:
        """
        Returns whole dataset as DataFrame
        @return: pd.DataFrame
        """
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    @abstractmethod
    def X(self) -> pd.DataFrame:
        """
        Returns only feature variables as DataFrame
        @return: pd.DataFrame
        """
        pass

    @property
    @abstractmethod
    def y(self) -> pd.Series:
        """
        Returns only target variable as Series
        @return: pd.Series
        """
        pass

    def get_negative_instances(self) -> pd.DataFrame:
        """
        Filters all the negative instances in the dataset and returns them
        @param neg_value: What target value counts as a "negative" instance
        @param column_name: Target column's name
        @return: All instances with a negative target value
        """
        return self.data[self.data[self._target_column_label] == self.neg_value].drop(columns=[self._target_column_label])



    def get_random_positive_instance(self) -> pd.Series:
        """
        Returns a random instance where the target variable is NOT the neg_value
        @param neg_value: What target value counts as a "negative" instance
        @param column_name: Target column's name
        @return: Random instance in dataset with positive target value
        """
        return self.data[self.data[self._target_column_label] != self.neg_value].drop(columns=[self._target_column_label]).sample()
