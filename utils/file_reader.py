import pandas as pd
import xml.etree.ElementTree as ET
import yaml
import os

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.csv':
        return pd.read_csv(file_path)
    elif ext in ['.xls', '.xlsx']:
        return pd.read_excel(file_path)
    elif ext == '.json':
        return pd.read_json(file_path, lines=True) if file_path.endswith('.jsonl') else pd.read_json(file_path)
    elif ext == '.parquet':
        return pd.read_parquet(file_path)
    elif ext == '.xml':
        return parse_xml(file_path)
    elif ext in ['.yaml', '.yml']:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        return pd.json_normalize(data)
    elif ext == '.tsv':
        return pd.read_csv(file_path, sep='\t')
    else:
        raise ValueError("Unsupported file format")

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    rows = []
    for child in root:
        row = {}
        for sub in child:
            row[sub.tag] = sub.text
        rows.append(row)
    return pd.DataFrame(rows)
