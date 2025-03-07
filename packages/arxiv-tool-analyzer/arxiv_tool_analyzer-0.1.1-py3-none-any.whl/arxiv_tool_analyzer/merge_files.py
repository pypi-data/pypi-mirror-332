import pandas as pd

def merge_excel_files(file_paths, output_path):
    dfs = [pd.read_excel(file) for file in file_paths]
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_excel(output_path, index=False)
    print(f"Merged files saved to '{output_path}'.")