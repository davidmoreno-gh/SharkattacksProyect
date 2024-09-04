def clean_labels(df_sharkattack):
    # rename and replace the columns into correct names
    df_sharkattack.columns = df_sharkattack.columns.str.lower().str.replace(" ","_").str.replace(".","_").str.replace(":","").str.strip()
    df_sharkattack = df_sharkattack.rename(columns={"species_" : "species"})
    return df_sharkattack


def clean_rows(df_sharkattack):
    '''
    Columns: unnamed_21 and unnamed_22 have all or almost all null values ​​4402
    Columns: pdf, href_formula, href, case_number, case_number_1, original_order no they have so many null values ​​but we are not going to need them for our analysis so we are going to eliminate them too
    '''
    df_sharkattack.loc[:4402]
    # save the columns to remove into list
    columns_failed = ['date','type','name','injury','time','species','source','pdf', 'href_formula', 'href', 'case_number', 'case_number_1', 'original_order','unnamed_21','unnamed_22']
    # next remove it
    df_sharkattack = df_sharkattack.drop(columns = columns_failed)
    # change column name: unnamed_11 to representative name
    df_sharkattack = df_sharkattack.rename(columns={"unnamed_11" : "death"})

    return df_sharkattack

def clean_state(df, value):
    # We can delete the states that have less than 16 attack
    df = df[df['state'].map(df['state'].value_counts()) > value]
    return df

def clean_country(df, value):
    # We can delete the countries that have less than 13 attack
    df = df[df['country'].map(df['country'].value_counts()) > value]
    return df


def clean_sex(df, sub):
    changes = {' M': 'M', 'M x 2': 'M','M ': 'M', 'lli': 'F'}
    df[sub] = df[sub].replace(changes)
    return df