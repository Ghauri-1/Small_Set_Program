import string



def processing_text(text):

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


# text = "Hello, World! This is a test.!!@!"
# text_after_processing = processing_text(text)
# print('Text before: ', text)
# print('\nText after: ', text_after_processing)


def extract_words(string):
    words = string.split()
    return words


def find_unique_words(words):
    unique_words = set(words)
    return unique_words