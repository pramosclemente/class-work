word = '-b-a-n-a-n-a-'
def remove_char(string):
    string = list(string)
    string.remove('-')
    return ''.join(string)
print(remove_char(word))