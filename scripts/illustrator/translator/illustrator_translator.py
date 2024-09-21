"""
Script by Arif Furkan Karaca
Website: fecitekme.com | Email: arifkaraca@protonmail.com
Thanks for using this script. Let's make your JSON translations easier.
"""

import json
import requests
import os

# Function to sanitize and remove invalid control characters
def sanitize_json_string(json_string):
    import re
    # Regular expression to match invalid control characters (except valid ones like \n, \t, etc.)
    invalid_chars = re.compile(r'[\x00-\x1f\x7f-\x9f]')
    sanitized_string = invalid_chars.sub('', json_string)
    return sanitized_string

# Function to translate text using Google Cloud Translation API
# Sends a request to the API and returns the translated text.
def translate_text(text, target_language, api_key):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        'q': text,
        'target': target_language,
        'key': api_key
    }
    response = requests.post(url, data=params)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
    return response.json()['data']['translations'][0]['translatedText']

# Function to split text into manageable chunks
# Splits large text into smaller parts to meet API request limits.
def split_text(text, max_length=1000):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        if current_length + len(sentence) + 1 <= max_length:
            current_chunk.append(sentence)
            current_length += len(sentence) + 1
        else:
            chunks.append('. '.join(current_chunk))
            current_chunk = [sentence]
            current_length = len(sentence) + 1

    if current_chunk:
        chunks.append('. '.join(current_chunk))
    
    return chunks

# Function to translate a JSON file and save the output
# Handles the entire process of reading, translating, and saving JSON content.
def translate_json_file(input_path, output_path, target_language, api_key):
    with open(input_path, 'r', encoding='utf-8') as file:
        # Read raw content of the file first
        raw_content = file.read()

    # Sanitize the raw content to remove invalid control characters
        sanitized_content = sanitize_json_string(raw_content)

    # Now load the sanitized content into the JSON parser
        data = json.loads(sanitized_content)

    translated_data = {}
    total_frames = len(data[list(data.keys())[0]])

    # Directory to store temporary split files
    split_dir = "temp_splits"
    if not os.path.exists(split_dir):
        os.makedirs(split_dir)

    # Splitting and translating text frames
    for frame_index, frame_key in enumerate(data[list(data.keys())[0]]):
        translated_data[frame_key] = {}
        for paragraph_key, paragraph_content in data[list(data.keys())[0]][frame_key].items():
            original_text = paragraph_content["custom_content"]
            text_chunks = split_text(original_text)
            translated_chunks = [translate_text(chunk, target_language, api_key) for chunk in text_chunks]
            translated_text = '. '.join(translated_chunks)
            translated_data[frame_key][paragraph_key] = {"custom_content": translated_text}

            # Save each chunk as a temporary file
            with open(os.path.join(split_dir, f"split_{frame_index}_{paragraph_key}.json"), 'w', encoding='utf-8') as split_file:
                json.dump(translated_data[frame_key], split_file, ensure_ascii=False, indent=4)

        # Progress update
        print(f"Translated frame {frame_index + 1}/{total_frames}")

    # Merging all translated parts into one output file
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump({list(data.keys())[0]: translated_data}, file, ensure_ascii=False, indent=4)

    # Clean up temporary files and directory
    for filename in os.listdir(split_dir):
        file_path = os.path.join(split_dir, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)
    os.rmdir(split_dir)

    print(f"Translation completed and saved to {output_path}. Temporary files deleted.")

if __name__ == "__main__":
    input_file = "large_file.json"  # Path to the input JSON file
    output_file = "translated_large_file.json"  # Path to save the translated JSON file

    # Ask user for API key and target language
    api_key = input("Please enter your Google Cloud API key: ").strip()
    target_lang = input("Please enter the target language code (e.g., 'es' for Spanish): ").strip()

    translate_json_file(input_file, output_file, target_lang, api_key)
