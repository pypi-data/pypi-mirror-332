import pandas as pd

# Intake / Output -----------------------------

def _series_intake(string):
    """Convert input to pandas Series if not already.

    Args:
        string (str or pd.Series): Input string or pandas Series

    Returns:
        tuple: (converted input, input type)
            - pd.Series: Converted input
            - type: Original input type
    """
    if isinstance(string, pd.Series):
        return string, pd.Series
    
    return pd.Series([string]), str

def _string_intake(string):
    """Convert input to pandas Series with str accessor if not already.

    Args:
        string (str or pd.Series): Input string or pandas Series

    Returns:
        tuple: (converted input with str accessor, input type)
            - pd.Series.str: Converted input with str accessor
            - type: Original input type
    """
    if isinstance(string, pd.Series):
        return string.str, pd.Series
    
    return pd.Series([string]).str, str

def _string_output(string, str_type):
    """Convert output back to original input type.

    Args:
        string (str or pd.Series): Processed string or pandas Series
        str_type (type): Original input type

    Returns:
        str or pd.Series: Processed string in original input type
    """
    if str_type == pd.Series:
        return string
    
    return string[0] # single string

def _handle_inplace(df, kwargs):
    """Handle inplace and copy operations for DataFrame modifications.

    Args:
        df (pd.DataFrame): Input DataFrame
        kwargs (dict): Keyword arguments containing 'inplace' and 'copy' options

    Returns:
        tuple: (DataFrame to operate on, boolean indicating if operation is inplace)
            - pd.DataFrame: DataFrame to operate on
            - bool: Indicates if operation is inplace

    Raises:
        ValueError: If both 'inplace' and 'copy' are set to True
    """
    if kwargs.get('inplace', False) and kwargs.get('copy', False):
        raise ValueError("Cannot set both inplace and copy to True.")
    
    if kwargs.pop('copy', False):
        return df.copy(), False
    
    if kwargs.pop('inplace', False):
        return df, True # inplace
    
    return df.copy(), False # if not specified, default to False