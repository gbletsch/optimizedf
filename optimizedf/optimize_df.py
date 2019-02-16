import pandas as pd
    

def _mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:  # we assume if not a df it's a series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2  # convert bytes to megabytes
    return "Total memory usage: {:03.2f} MB".format(usage_mb)


def optimize_df(df):
    '''Optimize df downcasting int and float columns and
    turning object columns in categorical when they have less then 50%
    unique values of the total.
    (Don't deal with datetime columns.)

    Ripped from 'https://www.dataquest.io/blog/pandas-big-data'
    to deal with large pandas dataframe without using parallel 
    os distributed computing.

    Parameters
    ----------
    df: pandas.dataframe
        df to be optimized

    Return
    ------
    dict with optimized column dtypes to use when reading from the database.
    '''

    print('Optimizing df...\n')

    # downcast int dtypes
    gl_int = df.select_dtypes(include=['int'])
    converted_int = gl_int.apply(pd.to_numeric, downcast='unsigned')

    # downcast float dtypes
    gl_float = df.select_dtypes(include=['float'])
    converted_float = gl_float.apply(pd.to_numeric, downcast='float')

    # deal with string columns
    gl_obj = df.select_dtypes(include=['object']).copy()
    converted_obj = pd.DataFrame()

    for col in gl_obj.columns:
        num_unique_values = len(gl_obj[col].unique())
        num_total_values = len(gl_obj[col])
        if num_unique_values / num_total_values < 0.5:
            converted_obj.loc[:, col] = gl_obj[col].astype('category')
        else:
            converted_obj.loc[:, col] = gl_obj[col]

    # join converted columns
    optimized_gl = df.copy()
    optimized_gl[converted_int.columns] = converted_int
    optimized_gl[converted_float.columns] = converted_float
    optimized_gl[converted_obj.columns] = converted_obj

    # make dict with optimized dtypes
    dtypes = optimized_gl.dtypes
    dtypes_col = dtypes.index
    dtypes_type = [i.name for i in dtypes.values]
    column_types = dict(zip(dtypes_col, dtypes_type))

    print('Original df size:', _mem_usage(df))
    print('Optimized df size:', _mem_usage(optimized_gl))

    return column_types