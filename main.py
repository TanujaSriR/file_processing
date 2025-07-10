from utils.file_reader import read_file
from utils.cleaner import clean_data
from utils.converter import save_file
from utils.logger import get_logger
import os
import sys

logger = get_logger()

def main():
    if len(sys.argv) != 3:
        logger.error("Usage: python main.py <input_file_path> <output_format>")
        return

    input_path = sys.argv[1]
    output_format = sys.argv[2].lower()

    logger.info(f"Reading file: {input_path}")
    df = read_file(input_path)

    logger.info("Cleaning data")
    df_cleaned = clean_data(df)

    filename = os.path.basename(input_path).split('.')[0]
    os.makedirs("data/output_files", exist_ok=True)
    output_path = f"data/output_files/{filename}_cleaned.{output_format}"
    logger.info(f"Saving cleaned file to: {output_path}")
    save_file(df_cleaned, output_path, output_format)

    logger.info("File processed successfully.")

if __name__ == "__main__":
    main()
