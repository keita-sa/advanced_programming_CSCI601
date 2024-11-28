import pandas as pd


def clean_data(df, remove_outliers_method=None, interpolate_method=None):
    """
    Perform data cleaning on the simulation data.

    Parameters:
        df (pd.DataFrame): Raw simulation data.
        remove_outliers_method (str): Method for removing outliers ('iqr' or 'zscore').
        interpolate_method (str): Interpolation method for missing values.

    Returns:
        pd.DataFrame: Cleaned simulation data.
    """
    # Step 1: Remove duplicate rows if any
    df_cleaned = df.drop_duplicates()

    # Step 2: Handle missing values
    # For this example, we assume missing values should be forward-filled
    if df_cleaned.isnull().values.any():
        df_cleaned = df_cleaned.fillna(method='ffill').fillna(method='bfill')

    # Step 3: Check for and handle unrealistic values (e.g., extremely high forces or positions)
    # Define thresholds (these should be set based on domain knowledge or data inspection)
    force_threshold = 100
    position_threshold = 1000

    # Cap forces and positions at thresholds
    df_cleaned['fx'] = df_cleaned['fx'].clip(-force_threshold, force_threshold)
    df_cleaned['fy'] = df_cleaned['fy'].clip(-force_threshold, force_threshold)
    df_cleaned['fz'] = df_cleaned['fz'].clip(-force_threshold, force_threshold)

    df_cleaned['x'] = df_cleaned['x'].clip(-position_threshold, position_threshold)
    df_cleaned['y'] = df_cleaned['y'].clip(-position_threshold, position_threshold)
    df_cleaned['z'] = df_cleaned['z'].clip(-position_threshold, position_threshold)

    # Step 4: Add a new column for total force (useful for analysis)
    df_cleaned['total_force'] = (df_cleaned['fx'] ** 2 + df_cleaned['fy'] ** 2 + df_cleaned['fz'] ** 2) ** 0.5

    # Remove outliers if specified
    if remove_outliers_method == 'iqr':
        df_cleaned = remove_outliers_iqr(df_cleaned)
    elif remove_outliers_method == 'zscore':
        df_cleaned = remove_outliers_zscore(df_cleaned)

    # Interpolate missing values if specified
    if interpolate_method:
        df_cleaned = interpolate_missing_values(df_cleaned, method=interpolate_method)

    return df_cleaned

def remove_outliers_iqr(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_cleaned = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df_cleaned

def remove_outliers_zscore(df, threshold=3.0):
    from scipy.stats import zscore
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    z_scores = zscore(df[numeric_cols])
    df_cleaned = df[(abs(z_scores) < threshold).all(axis=1)]
    return df_cleaned

def interpolate_missing_values(df, method='linear', axis=0):
    """
    Interpolate missing values in the DataFrame.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        method (str): Interpolation method (e.g., 'linear', 'quadratic').
        axis (int): Axis along which to interpolate (0 for index, 1 for columns).

    Returns:
        pd.DataFrame: DataFrame with interpolated missing values.
    """
    return df.interpolate(method=method, axis=axis)
