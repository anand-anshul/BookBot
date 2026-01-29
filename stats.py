def count_words(text: str):
    text_list = text.split()
    return len(text_list)

def count_char(text: str):
    count_dict = {}
    for c in text:
        c = c.lower()
        if c not in count_dict:
            count_dict[c] = 1
        else:
            count_dict[c] += 1
    return count_dict

def sorted_list(char_dict: dict):
    def sort_on(dict: dict):
        return dict["num"]
    dict_list = []
    for char, count in char_dict.items():
        item = {"char" : char, "num" : count}
        dict_list.append(item)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list