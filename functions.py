

def clean_state(df, value):
    # We can delete the states that have less than 16 attack
    df = df[df['State'].map(df['State'].value_counts()) > value]
    return df


def clean_country(df, value):
    # We can delete the countries that have less than 13 attack
    df = df[df['Country'].map(df['Country'].value_counts()) > value]
    return df


def clean_sex(df, sub):
    changes = {' M': 'M', 'M x 2': 'M','M ': 'M', 'lli': 'F'}
    df[sub] = df[sub].replace(changes)
    return df