# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:40:51 2021

@author: vik
"""
import random
import itertools

age_and_genre=['a young _ girl','a young _ boy','a young _ woman','a young _ men','an adult _ woman','an adult _ men','an old _ woman','an old _ man']
clothing=['t-shirt','shirt','sweater','jacket','dress','long coat','swimsuit','sweatshirt','gym clothes','wedding dress','hoodie','uniform','long-sleeve top','coat','sheath dress']
clothing_color=['black','gray','red','brown','blue','purple','white','green','orange','yellow']
hair_color=['blonde','brown','black','red','blue','purple','white','green','gray']
skin_color=['white','brown','black']

age_genre_and_skin_color = []
for i in range(len(age_and_genre)):
    for j in range(len(skin_color)):
        age_genre_and_skin_color.append(age_and_genre[i].replace('_', skin_color[j]))
        
#l = ["{x} {y} {z}".format(x=x,y=y,z=z) for x,y,z in itertools.product(list1, list2, list3)]
#lst = [' '.join(p) for p in product(age_genre_and_skin_color, list2, list3)]
#from itertools import product

lst = [f"{w} with {x} hair wearing a {y} {z}" for w,x,y,z in itertools.product(age_genre_and_skin_color, hair_color, clothing_color, clothing)]
random.shuffle(lst)

from pprint import pprint
#pprint(lst)
pprint(len(lst))

with open('sentences2audio.txt', 'a') as my_file:
    for l in lst[:1200]:
        my_file.write(f"{l}\n")

new_list = []
with open('sentences2audio.txt') as my_doc:
    for line in my_doc.readlines():
        new_list.append(line.strip('\n'))

#pprint(new_list)
pprint(len(new_list))
        
with open('sb_train.transcription.txt', 'a') as my_file:
    for n in range(len(lst[:1000])):
        my_file.write(f"<s> {lst[n]} </s> (file-{n+1})\n")
        
with open('sb_test.transcription.txt', 'a') as my_file:
    for n in range(len(lst[1000:1200])):
        my_file.write(f"{lst[n+1000]} (file-{n+1001})\n")
        
print('done lml')
