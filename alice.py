import sys


def remove_pairs(message:str) -> str:
    """
    This function removes all duplicate characters from a given string.
    Parameters:
    message : str
        The input string to be processed.
    Returns:
    str
        The processed string without duplicate characters.
    """
    text = []
    for letter in message:
        if text and text[-1] == letter:
            text.pop()
        else:
            text.append(letter)
    return "".join(text)

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r", encoding='utf-8') as file:
        ciphered_message = file.read().strip()
    clear_text = remove_pairs(ciphered_message)
    print(clear_text)
