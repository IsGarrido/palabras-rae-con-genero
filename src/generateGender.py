import os
import re

words = []
base_dir = "data\\rae\\"

for file in os.listdir(base_dir):
    if file.endswith(".txt") and not file.startswith('dict'):
        file = open(base_dir + file, "r", encoding="utf-8")
        for line in file:
            words.append(line.rstrip())
cleanWords = sorted(set([re.sub('[0-9- ]', '', word) for word in words]))
withComma = [word for word in cleanWords if ',' in word]

genderized = []
for word in withComma:
    male = re.search(r'(\w*),(\w*)',word)[1]
    suffix = re.search(r'(\w*),(\w*)',word)[2]
    try:
        if suffix != 'a':
            bondingPoint = abs(re.search(suffix[0], male[::-1]).start()-len(male)+1)
            prefix = male[:bondingPoint]
            female = prefix+suffix
            genderized.append(male + "\t" + female)
        else:
            if male.endswith('o'):
                female = male[:-1] + suffix
                genderized.append(male + "\t" + female)
            else:
            	female = male + suffix
            	genderized.append(male + "\t" + female)
    except:
        print(male)
words = sorted(set(genderized))
with open('../rae-generos.txt', mode='wt', encoding='utf-8') as file:
    file.write('\n'.join(words))
