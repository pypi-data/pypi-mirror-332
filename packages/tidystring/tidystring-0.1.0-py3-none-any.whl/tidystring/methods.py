import re, pandas as pd

from .handlers import _series_intake, _string_intake, _string_output

# String Re-Case -------------------------------

def camel_to_snake(string):
    """Convert camel case string to snake case.

    Args:
        string (str): Camel case string

    Returns:
        str: Snake case string

    Examples:
        >>> camel_to_snake("camelCase")
        'camel_case'
    """
    string = re.sub(r'(?<!^)(?=[A-Z])', '_', string)
    return string.lower()

def snake_to_camel(string):
    """Convert snake case string to camel case.

    Args:
        string (str): Snake case string

    Returns:
        str: Camel case string

    Examples:
        >>> snake_to_camel("snake_case")
        'SnakeCase'
    """
    return ''.join(x.capitalize() or '_' for x in string.split('_'))

# stringr-Style --------------------------------

def str_detect(string, pattern, **kwargs):
    """Detect the presence of a pattern in a string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        pattern (str): Regular expression pattern to detect
        **kwargs: Additional keyword arguments for pandas str.contains()

    Returns:
        bool or pd.Series: Boolean or Series of booleans indicating pattern presence

    Examples:
        >>> str_detect("hello world", "world")
        True
        >>> str_detect(pd.Series(["hello", "world"]), "o")
        0     True
        1    False
        dtype: bool
    """
    string, str_type = _string_intake(string)
    result = string.contains(pattern, **kwargs)
    return _string_output(result, str_type)

def str_replace(string, *args, n=None, **kwargs):
    """Replace all occurrences of specified patterns in string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        *args: Patterns to replace in the string
        **kwargs: Additional keyword arguments for str.replace()
            n (int, optional): Number of replacements to make. Defaults to None (all occurrences).

    Returns:
        str or pd.Series: String with patterns replaced

    Examples:
        >>> str_replace("hello world", "o", "a")
        'hellar warld'
        >>> str_replace("hello world", "o", "a", n=1)
        'hellar world'
        >>> str_replace(pd.Series(["hello world", "hello there"]), "o", "a", n=1)
        0    hellar world
        1    hellar there
        dtype: object
    """

    if kwargs.get('n', None) is not None:
        kwargs['count'] = kwargs.pop('n')

    string, str_type = _string_intake(string)
    result = string.replace(*args, **kwargs)
    return _string_output(result, str_type)
    
def str_remove(string, *args, **kwargs):
    """Remove all occurrences of specified patterns from string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        *args: Patterns to remove from the string
        **kwargs: Additional keyword arguments for pandas str.replace()

    Returns:
        str or pd.Series: String with patterns removed

    Examples:
        >>> str_remove("hello world", "o")
        'hell wrld'
        >>> str_remove(pd.Series(["hello", "world"]), "o")
        0    hell
        1    wrld
        dtype: object
    """
    string, str_type = _string_intake(string)
        
    for arg in args:
        string = string.replace(arg, '', **kwargs)
        
    return _string_output(string, str_type)

def str_extract(string, pattern, **kwargs):
    """Extract first match of pattern from string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        pattern (str): Regular expression pattern to extract
        **kwargs: Additional keyword arguments for pandas str.extract()

    Returns:
        str or pd.Series: First match of pattern or empty string if no match

    Examples:
        >>> str_extract("hello world", "h(\\w+)")
        'ello'
        >>> str_extract(pd.Series(["hello world", "python"]), "\\w{2}o")
        0    hel
        1    pyt
        dtype: object
    """
    string, str_type = _string_intake(string)
    result = string.extract(f"({pattern})", **kwargs)
    return _string_output(result, str_type)

def str_split(string, pattern, maxsplit=-1):
    """Split string by pattern into list of components.

    Args:
        string (str or pd.Series): Input string or pandas Series
        pattern (str): Pattern to split on
        maxsplit (int, optional): Maximum number of splits. Defaults to -1 (all possible splits).

    Returns:
        list or pd.Series of lists: Split components

    Examples:
        >>> str_split("a.b.c", "\\.")
        ['a', 'b', 'c']
        >>> str_split("a.b.c", "\\.", 1)
        ['a', 'b.c']
    """
    string, str_type = _string_intake(string)
    result = string.split(pattern, n=maxsplit)
    return _string_output(result, str_type)

def str_trim(string, **kwargs):
    """Remove whitespace from start and end of string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        **kwargs: Additional keyword arguments for pandas str.strip()

    Returns:
        str or pd.Series: Trimmed string

    Examples:
        >>> str_trim("  hello  ")
        'hello'
        >>> str_trim(pd.Series(["  hello  ", " world "]))
        0    hello
        1    world
        dtype: object
    """
    string, str_type = _string_intake(string)
    result = string.strip(**kwargs)
    return _string_output(result, str_type)

def str_to_title(string, **kwargs):
    """Convert string to title case.

    Args:
        string (str or pd.Series): Input string or pandas Series
        **kwargs: Additional keyword arguments for pandas str.title()
            remove_dashes (bool, optional): Remove dashes from string. Defaults to False.

    Returns:
        str or pd.Series: Title-cased string

    Examples:
        >>> str_to_title("hello world")
        'Hello World'
        >>> str_to_title(pd.Series(["hello world", "python code"]))
        0    Hello World
        1    Python Code
        dtype: object
    """
    if kwargs.pop('remove_dashes', False):
        string = str_dash_to_space(string)

    string, str_type = _string_intake(string)
    result = string.title(**kwargs)
    return _string_output(result, str_type)

def str_to_upper(string, **kwargs):
    """Convert string to uppercase.

    Args:
        string (str or pd.Series): Input string or pandas Series
        **kwargs: Additional keyword arguments for pandas str.upper()

    Returns:
        str or pd.Series: Uppercase string

    Examples:
        >>> str_to_upper("hello")
        'HELLO'
        >>> str_to_upper(pd.Series(["hello", "world"]))
        0    HELLO
        1    WORLD
        dtype: object
    """
    string, str_type = _string_intake(string)
    result = string.upper(**kwargs)
    return _string_output(result, str_type)

def str_to_lower(string, **kwargs):
    """Convert string to lowercase.

    Args:
        string (str or pd.Series): Input string or pandas Series
        **kwargs: Additional keyword arguments for pandas str.lower()

    Returns:
        str or pd.Series: Lowercase string

    Examples:
        >>> str_to_lower("HELLO")
        'hello'
        >>> str_to_lower(pd.Series(["HELLO", "WORLD"]))
        0    hello
        1    world
        dtype: object
    """
    string, str_type = _string_intake(string)
    result = string.lower(**kwargs)
    return _string_output(result, str_type)

def str_upper_cut(string, **kwargs):
    """Capitalize the first n characters of string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        **kwargs: Additional arguments
            n (int, optional): Number of characters to capitalize. Defaults to 1.

    Returns:
        str or pd.Series: String with first n characters capitalized

    Examples:
        >>> str_upper_cut("hello")
        'Hello'
        >>> str_upper_cut("hello", n=2)
        'HEllo'
    """
    string, str_type = _series_intake(string)
    string = string.astype(str) # convert
    
    def upper_cut(s):
        return s[:kwargs.get('n', 1)].upper() + s[kwargs.get('n', 1):]
    
    result = string.map(upper_cut)
    return _string_output(result, str_type)

def str_startswith(string, pattern, **kwargs):
    """Check if string starts with pattern.

    Args:
        string (str or pd.Series): Input string or pandas Series
        pattern (str): Pattern to check
        **kwargs: Additional keyword arguments for pandas str.startswith()

    Returns:
        bool or pd.Series: True if string starts with pattern, False otherwise

    Examples:
        >>> str_startswith("hello world", "hello")
        True
        >>> str_startswith(pd.Series(["hello", "world"]), "w")
        0    False
        1     True
        dtype: bool
    """
    string, str_type = _string_intake(string)
    result = string.startswith(pattern, **kwargs)
    return _string_output(result, str_type)

def str_endswith(string, pattern, **kwargs):
    """Check if string ends with pattern.

    Args:
        string (str or pd.Series): Input string or pandas Series
        pattern (str): Pattern to check
        **kwargs: Additional keyword arguments for pandas str.endswith()

    Returns:
        bool or pd.Series: True if string ends with pattern, False otherwise

    Examples:
        >>> str_endswith("hello world", "world")
        True
        >>> str_endswith(pd.Series(["hello", "world"]), "o")
        0     True
        1    False
        dtype: bool
    """
    string, str_type = _string_intake(string)
    result = string.endswith(pattern, **kwargs)
    return _string_output(result, str_type)
    
# additional methods --------------------------------

def str_concat(*args, sep='_', **kwargs):
    """Concatenate strings or Series with separator.

    This function can concatenate:
    1. Multiple strings into a single string
    2. Multiple pandas Series element-wise
    3. Multiple columns from a DataFrame

    Args:
        *args: Strings or Series to concatenate
            - If first arg is DataFrame, remaining args are treated as column names
            - If all args are Series, concatenates row-wise
            - If all args are strings, joins with separator
        sep (str, optional): Separator to use between concatenated items. Defaults to '_'.
        **kwargs: Additional keyword arguments

    Returns:
        str or pd.Series: Concatenated string(s)

    Raises:
        ValueError: If args[0] is DataFrame but not all remaining args are valid column names
        TypeError: If args are not all strings or all Series

    Examples:
        >>> str_concat("hello", "world")
        'hello_world'
        >>> str_concat("hello", "world", sep="-")
        'hello-world'
        >>> str_concat(pd.Series(["a", "b"]), pd.Series(["c", "d"]))
        0    a_c
        1    b_d
        dtype: object
    """
    if isinstance(args[0], pd.DataFrame):
        df = args[0] # Assume remaining args are columns
        cols = list(args[1:])  # Columns to concatenate
        if not all(col in df.columns for col in cols):
            raise ValueError("All arguments must be column names in the DataFrame")
        return df[cols].astype(str).agg(sep.join, axis=1)
    
    # Check if all arguments are strings or all are Series
    if all(isinstance(arg, pd.Series) for arg in args):
        # Concatenate all Series row-wise
        return pd.concat(args, axis=1).astype(str).agg(sep.join, axis=1)
    elif all(isinstance(arg, str) for arg in args):
        # Join all strings into one string with separator
        return sep.join(args)
    
    raise TypeError("All arguments must be either all strings or all pandas Series")

def str_dash_to_space(string, dashes=["-", "_"], **kwargs):
    """Replace all occurrences of specified dashes with spaces.

    Args:
        string (str or pd.Series): Input string or pandas Series
        dashes (list, optional): List of dashes to replace. Defaults to ["-", "_"].
        **kwargs: Additional keyword arguments for str_replace()
            n (int, optional): Number of replacements to make. Defaults to None (all occurrences).

    Returns:
        str or pd.Series: String with dashes replaced by spaces

    Examples:
        >>> str_dash_to_space("hello-world")
        'hello world'
        >>> str_dash_to_space(pd.Series(["hello-world", "hello_world"]))
        0    hello world
        1    hello world
        dtype: object
    """
    if kwargs.get('n', None) is not None:
        kwargs['count'] = kwargs.pop('n')

    for dash in dashes:
        string = str_replace(string, dash, " ", **kwargs)
    return string

# search + replace methods ----------------------------------

def str_search_apply(string, pattern, func, **kwargs):
    """Apply a function to each regex match in string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        pattern (str): Regular expression pattern to match
        func (callable): Function to apply to each match
        **kwargs: Additional keyword arguments passed to func

    Returns:
        str or pd.Series: String with function applied to each match

    Examples:
        >>> str_search_apply("hello world", "\\w+", lambda x: x.upper())
        'HELLO WORLD'
        >>> str_search_apply("ab12cd34", "\\d+", lambda x: str(int(x) * 2))
        'ab24cd68'
    """
    string, str_type = _series_intake(string)
    string = string.astype(str) # convert
    
    def apply_func(match):
        return func(match.group(), **kwargs)
    
    # Apply the func to all matches
    result = string.apply(lambda s: re.sub(pattern, lambda m: apply_func(m), s))
    return _string_output(result, str_type)

def str_search_recase(string, pattern, case):
    """Change the case of text matching a pattern in string.

    Args:
        string (str or pd.Series): Input string or pandas Series
        pattern (str): Regular expression pattern to match
        case (str): Case transformation to apply. One of:
            - 'lower': Convert to lowercase
            - 'upper': Convert to uppercase
            - 'title': Convert to title case
            - 'snakecase': Convert to snake_case
            - 'camelcase': Convert to CamelCase

    Returns:
        str or pd.Series: String with case transformation applied to matches

    Raises:
        NotImplementedError: If case is not one of the supported options

    Examples:
        >>> str_search_recase("hello WORLD", "\\w+", "upper")
        'HELLO WORLD'
        >>> str_search_recase("helloWorld", "\\w+", "snakecase")
        'hello_world'
    """
    case_options = ['lower', 'upper', 'title', 
                    'snakecase', 'camelcase']
    
    if case not in case_options:
        raise NotImplementedError(f"Implemented case options: {case_options}.")
    
    string, str_type = _series_intake(string)
    
    def recase(match):
        if case == 'upper':
            return match.group().upper()
        elif case == 'lower':
            return match.group().lower()
        elif case == 'title':
            return match.group().title()
        elif case == 'snakecase':
            return camel_to_snake(match.group())
        elif case == 'camelcase':
            return snake_to_camel(match.group())
        
    # Apply the recase function to all matches
    result = string.apply(lambda s: re.sub(pattern, lambda m: recase(m), s))
    return _string_output(result, str_type)