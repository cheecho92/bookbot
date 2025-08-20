def word_count(text):
    words = (len(text.split()))
    return words

def character_count(text):
    text_lower = text.lower()
    chars = {}
    for char in set(text_lower):
        count = 0
        for letter in text_lower:
            if char == letter:
                count+= 1
            chars[char] = count
    return chars

def sort_on(num):
    return num['num']

def sort_dict(items):
    
    dict_list = []
    for key,value in items.items():
        empty_dict = {'char': key, 'num': value}
        dict_list.append(empty_dict)
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list