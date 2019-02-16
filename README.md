# optimizedf

Optimize a pandas DataFrame changing some columns dtypes.

Optimize df downcasting int and float columns and turning object columns in categorical when they have less then 50% unique values of the total.
Don't deal with datetime columns.

Ripped from 'https://www.dataquest.io/blog/pandas-big-data' to deal with large pandas dataframe without using parallel os distributed computing.

## Installing

This is my preferred way of sharing/storing/installing packages. Use pip to install it from that repo directly.

```
pip install git+https://github.com/gbletsch/optimizedf.git
```

Or if, for some reason, you don't want to use git:

```
pip install https://github.com/gbletsch/optimizedf/zipball/master
```


## Example:


```python
>> from optimizedf.optimize_df import optimize_df
>> columns_optimized = optimize_df(df)

Optimizing df...

Original df size: Total memory usage: 643.34 MB
Optimized df size: Total memory usage: 100.69 MB
        
>> print(df.dtypes)

N_AIH                     object
NASC              datetime64[ns]
DT_INTER          datetime64[ns]
DT_SAIDA          datetime64[ns]
US_TOT                   float32
DIAS_PERM                 uint16
ANO_CMPT                category
DIAG_PRINC              category
MORTE                      uint8
IDADE                      uint8
CNES                    category
UF                      category
SEXO                    category
ETNIA                   category
COMPLEX                 category
CAR_INT                 category
MUNIC_RES               category
MUNIC_MOV               category
DIAG_PRINC_CAT          category
dtype: object
    
>> df = df.astype(columns_optimized)
>> print(df.dtypes)

N_AIH                     object
NASC              datetime64[ns]
DT_INTER          datetime64[ns]
DT_SAIDA          datetime64[ns]
US_TOT                   float32
DIAS_PERM                 uint16
ANO_CMPT                category
DIAG_PRINC              category
MORTE                      uint8
IDADE                      uint8
CNES                    category
UF                      category
SEXO                    category
ETNIA                   category
COMPLEX                 category
CAR_INT                 category
MUNIC_RES               category
MUNIC_MOV               category
DIAG_PRINC_CAT          category
dtype: object

```
