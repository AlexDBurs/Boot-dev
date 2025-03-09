from main import *

#Saca el txt
path_to_file = r'book\Frankestein.txt'
with open(path_to_file, encoding = 'utf8') as f:
        file_contents = f.read()

#Arma el dict
word_list = file_contents.lower().split()
letter_dict = {}
for word in word_list:
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

def letter_dict_list_sorter_key(dict):
     return dict['num']

letter_dict_list = []
for key in letter_dict:
    if key.isalpha():
        letter_dict_list.append({'name':key, 'num':letter_dict[key]})

letter_dict_list.sort(reverse = True, key = letter_dict_list_sorter_key)

print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")
for dict1 in letter_dict_list:
    print(f"{dict1['name']}: {dict1['num']}")
print("============= END ===============")
