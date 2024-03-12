sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
        dict_ex=input('Enter a word in English or EXIT: ')
        if dict_ex=='EXIT':
            print('Bye!')
            break
        elif dict_ex in sample_dict:
            print('Translation:',sample_dict[dict_ex])
        else:
            print('No match!')


temp_list = [1, 2, 3]
for i in range(len(temp_list)):
    temp_list.insert(i+1, 0)
print(temp_list)
