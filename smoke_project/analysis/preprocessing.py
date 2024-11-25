import pandas as pd
import numpy as np


def handle_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in the data.
    - Fill numeric columns with the median.
    - Fill categorical columns with the most frequent value.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """
    for col in data.columns:
        if data[col].dtype in ['float64', 'int64']:
            data[col] = data[col].fillna(data[col].median())  # Fill numeric columns with median
        else:
            data[col] = data[col].fillna(data[col].mode()[0])  # Fill categorical columns with mode
    return data


def normalize_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize numeric columns in the DataFrame to have values between 0 and 1.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with normalized numeric columns.
    """
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].min()) / (
            data[numeric_cols].max() - data[numeric_cols].min())
    return data


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Perform all preprocessing steps: handle missing values and normalize data.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    data = handle_missing_values(data)
    data = normalize_data(data)
    return data


def remove_outliers(data: pd.DataFrame, z_thresh: float = 3.0) -> pd.DataFrame:
    """
    Remove outliers from numeric columns based on the Z-score method.

    Args:
        data (pd.DataFrame): Input DataFrame.
        z_thresh (float): Z-score threshold to detect outliers.

    Returns:
        pd.DataFrame: DataFrame with outliers removed.
    """
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    z_scores = np.abs((data[numeric_cols] - data[numeric_cols].mean()) / data[numeric_cols].std())
    outlier_mask = (z_scores < z_thresh).all(axis=1)
    return data[outlier_mask]


def encode_categorical_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Perform one-hot encoding on categorical columns.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with one-hot encoded categorical columns.
    """
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns
    data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
    return data
