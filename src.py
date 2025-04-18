import requests
import json

def download_openai_file(file_id, api_key, output_file="batch_output.jsonl"):
    """
    Downloads a file from OpenAI using the specified file_id and API key,
    then writes the content to the output_file.

    Parameters:
        file_id (str): The OpenAI file ID.
        api_key (str): Your OpenAI API key.
        output_file (str, optional): The local filename to save the content. Defaults to "batch_output.jsonl".
    """
    url = f"https://api.openai.com/v1/files/{file_id}/content"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"File downloaded successfully and saved as '{output_file}'.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        print(f"Response: {response.text}")



def load_jsonl_file(file_path):
    """
    Load a JSON Lines file and return a list of dictionaries.
    
    Parameters:
        file_path (str): The path to the JSONL file.
        
    Returns:
        list: A list of dictionaries loaded from the file.
    """
    data = []
    # Open the file for reading
    with open(file_path, "r", encoding="utf-8") as file:
        # Process each line (each line is a valid JSON object)
        for line in file:
            # Check if the line is not empty, then parse JSON and add to the list.
            if line.strip():
                data.append(json.loads(line))
    return data
