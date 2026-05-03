from main2 import processing_text, extract_words, find_unique_words


def write_file(filepath, content):
    try:
        with open(filepath, 'a', encoding='utf-8') as file: 
            file.write(content + '\n') 
    except Exception as e:
        print(f"Error: An error occurred while writing to the file: {e}")



def read_file(filepath):
    try:


        with open(filepath, 'r', encoding='utf-8') as file: # Specify encoding for broader character support
            content = file.read()
            return content

        
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")        
        write_file(filepath, "This is a new file created because it did not exist.")
        return None
    except Exception as e:
        print(f"Error: An error occurred while reading the file: {e}")
        return None



# Example usage
file_content = read_file('example.txt') # Assuming you have a file named 'example.txt'
if file_content:
    the_cleansed_text = processing_text(file_content)
    words = extract_words(the_cleansed_text)
    unique_words = find_unique_words(words)
    print("Original Text:", file_content)
    print("\n\nExtracted Words:", words)
    print("\n\nUnique Words:", unique_words)
else:
    print("File reading failed.")