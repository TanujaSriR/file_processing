def save_file(df, output_path, format):
    if format == 'csv':
        df.to_csv(output_path, index=False)
    elif format in ['xlsx', 'excel']:
        df.to_excel(output_path, index=False)
    elif format == 'json':
        df.to_json(output_path, orient='records', lines=True)
    elif format == 'parquet':
        df.to_parquet(output_path, index=False)
    elif format == 'tsv':
        df.to_csv(output_path, sep='\t', index=False)
    else:
        raise ValueError("Unsupported output format")