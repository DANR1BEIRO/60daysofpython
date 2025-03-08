import json
from typing import Any

def save_data(file: str, data: Any) -> None:
    """
    Save datas in a JSON file

    Args:
        file (str): Path to JSON file
        data (Any): Data that will be stored in the file
    """
    
    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
def load_data(file: str) -> Any:
    """Read data from JSON file

    Args:
        file (str): Path to JSON file

    Returns:
        Any: Data loaded and readed from JSON
    """
    try:
        with open(file, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File don't found! path of file {file}")
        return {}

data_example = {"name": "goku", "city": "kaioh planet", "Occupation": "Fighter"}

file_name = "name_goku.json"

save_data(file_name, data_example)

loaded_data = load_data(file_name)

print("Loaded data: ", loaded_data)