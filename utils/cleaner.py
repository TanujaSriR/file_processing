def clean_data(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.drop_duplicates(inplace=True)
    df.fillna("missing", inplace=True)
    return df