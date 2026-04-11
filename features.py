import pandas as pd

def add_features(df):
    df = df.copy()

    # Age group
    age = df['insured_age']

    df['age_group'] = 'Adult'
    df.loc[age < 13, 'age_group'] = 'Child'
    df.loc[(age >= 13) & (age <= 19), 'age_group'] = 'Teenager'
    df.loc[(age >= 20) & (age <= 29), 'age_group'] = 'Youth'
    df.loc[(age >= 50) & (age <= 64), 'age_group'] = 'Middle Age'
    df.loc[age >= 65, 'age_group'] = 'Senior'

    # Police report
    df['police_report_available'] = (
        df['police_report_available']
        .astype(str)
        .str.lower()
        .map({'yes': 1, 'no': 0})
        .fillna(0)
    )

    return df