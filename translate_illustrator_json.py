import json
import requests
from tqdm import tqdm

API_KEY = "YOUR API KEY"

# Function to split the JSON file into smaller chunks
def split_json(file_path, chunk_size):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Extract the nested dictionary containing frames
    frames = data.get("YOUR_ILLUSTRATOR_FILENAME.ai", {})
    
    frame_keys = list(frames.keys())
    chunks = [frame_keys[i:i + chunk_size] for i in range(0, len(frame_keys), chunk_size)]
    
    for i, chunk in enumerate(chunks):
        chunk_data = {"YOUR_ILLUSTRATOR_FILENAME.ai": {key: frames[key] for key in chunk}}
        with open(f'chunk_{i}.json', 'w', encoding='utf-8') as chunk_file:
            json.dump(chunk_data, chunk_file, ensure_ascii=False, indent=4)
    
    return len(chunks)

# Function to translate text using Google Cloud Translation API
def translate_text(text, target_language='uk'):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'q': text,
        'target': target_language,
        'format': 'text',
        'key': 'YOUR API KEY'
    }
    response = requests.post(url, data=params)
    result = response.json()
    return result['data']['translations'][0]['translatedText']

# Function to translate a chunk of JSON file
def translate_chunk(file_path, target_language='uk'):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    frames = data.get("YOUR_ILLUSTRATOR_FILENAME.ai", {})
    
    for frame in tqdm(frames.values(), desc="Translating frames"):
        for paragraph in frame.values():
            if 'contents' in paragraph:
                paragraph['contents'] = translate_text(paragraph['contents'], target_language)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Function to merge translated chunks back into a single file
def merge_chunks(chunk_count, output_file):
    merged_data = {"YOUR_ILLUSTRATOR_FILENAME.ai": {}}
    for i in range(chunk_count):
        with open(f'chunk_{i}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            merged_data["YOUR_ILLUSTRATOR_FILENAME.ai"].update(data["YOUR_ILLUSTRATOR_FILENAME.ai"])
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(merged_data, file, ensure_ascii=False, indent=4)

# Example usage
chunk_size = 1  # Adjust this based on the size of your frames
input_file = 'large_file.json'  # Ensure this is the correct path to your JSON file

chunk_count = split_json(input_file, chunk_size)

for i in tqdm(range(chunk_count), desc="Translating chunks"):
    translate_chunk(f'chunk_{i}.json')

merge_chunks(chunk_count, 'translated_large_file.json')
