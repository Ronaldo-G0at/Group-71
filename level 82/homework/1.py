def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first

def string_to_array(s):
    return s.split(' ')


def reverse_words(text):
    text_re = list(reversed(text))
    text = ''.join(text_re)
    text1 = text.split(' ')
    text1.reverse()
    text = ' '.join(text1)
    return text