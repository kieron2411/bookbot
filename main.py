def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = count_words(text)
    dict_list = dict_to_list(count_characters(text))
    print(f"--- Begin report of {path} ---")
    print(f"There are {num_words} words in the document.\n")
    for dict in dict_list:
        print(f"The character {dict["char"]} was found {dict["count"]} times.")
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def dict_to_list(dict):
    dict_list = []
    for item in dict:
        if item.isalpha():
            dict_list.append({"char": item, "count": dict[item]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["count"]

def get_text(path):
    with open(path) as f:
        return f.read()

main()