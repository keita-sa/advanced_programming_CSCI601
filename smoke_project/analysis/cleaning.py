import pandas as pd


def clean_data(df):
    """
    Perform data cleaning on the simulation data.

    Parameters:
        df (pd.DataFrame): Raw simulation data.

    Returns:
        pd.DataFrame: Cleaned simulation data.
    """
    # Step 1: Remove duplicate rows if any
    df_cleaned = df.drop_duplicates()

    # Step 2: Handle missing values
    # For this example, we assume missing values should be forward-filled
    if df_cleaned.isnull().values.any():
        df_cleaned = df_cleaned.fillna(method='ffill')  # Forward fill
        df_cleaned = df_cleaned.fillna(method='bfill')  # Backward fill if forward fill is not enough

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

    return df_cleaned
