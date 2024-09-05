def clean_labels(df):
    '''
    The function replace the names in lower case, replace spaces, dots and colons
    Delete the empty spaces at the beginning and at the end of the string
    Rename the labels
    '''
    df.columns = df.columns.str.lower().str.replace(" ","_").str.replace(".","_").str.replace(":","").str.strip()
    df.rename(columns={"species_" : "species", "unnamed_11" : "death"}, inplace= True)
    return df

def clean_rows(df):
    '''
    The function delete the rows with more than 4000 values to keep the data since 1969
    '''
    df = df.loc[:4000]
    return df

def drop_cols(df, cols_to_drop):
    '''
    Delete de colums indicated in cols_to_drop
    '''
    df = df.drop(columns=cols_to_drop)
    return df

def clean_sex(df):
    '''
    Changes the sex labels to only M and F
    '''
    changes = {' M': 'M', 'M x 2': 'M','M ': 'M', 'lli': 'F'}
    df['sex'] = df['sex'].replace(changes)
    return df

def null_values_sex(sex):
    '''
    Replace the null values in the column 'sex' with the mode
    '''
    sex = sex.fillna(sex.mode()[0])
    return sex
    
def null_values_year(year):
    '''
    Replace the null values in the column 'year' with the previous value
    '''
    year = year.fillna(method ='bfill')
    return year

def filter_country(df, value):
    ''' 
    Delete the rows with a country that appears less than `value` times
    ''' 
    df = df[df['country'].map(df['country'].value_counts()) > value]
    return df


def filter_state(df, value):
    '''
    Delete the rows with a state that appears less than `value` times
    '''
    df = df[df['state'].map(df['state'].value_counts()) > value]
    return df

def filter_year(df):
    '''
    Delete the rows with year = 2024 to have a better analysis
    '''
    df = df.loc[df['year'] != 2024]
    return df

def filter_death(df):
    '''
    Delete the rows whose values in the column 'death' are not 'Y' or 'N'
    '''
    df = df.loc[(df['death']=='Y') | (df['death']=='N')]
    return df
