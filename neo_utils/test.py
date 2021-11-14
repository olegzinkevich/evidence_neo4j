data = [{"id":1,"token":"Passive","name":"Станислав","surname":"Бочаров","relLevel":"3"},{"id":1,"current_timestamp":"2020-02-24","token":"Passive","relIteration":"2","name":"Станислав","surname":"Бочаров"},{"id":1,"token":"Imperative","name":"Станислав","surname":"Бочаров","relLevel":"3"},{"id":1,"current_timestamp":"2020-02-24","token":"Imperative","relIteration":"5","name":"Станислав","surname":"Бочаров"},{'comment': "jhgjgg"}]


comment = None
for item in data:
    if 'comment' in item:
        comment = item.get('comment')
        data.remove(item)


from itertools import groupby
from operator import itemgetter
groups = groupby(sorted(data, key = itemgetter('token')), key = itemgetter('token'))
data_dict = [list(g) for k, g in groups]
finalMergedRels = []
for x in data_dict:
    # merging two dictionaries
    z = {**x[0], **x[1]}
    finalMergedRels.append(z)

print(finalMergedRels)

for x in finalMergedRels:
    relLevel = x.get('relLevel')
    token = x.get('token')
    client_id = x.get('id')
    iteration = x.get('relIteration')
    timestamp = x.get('current_timestamp')



print(comment)



sentences = [{'sentence':'I [[think]] that it is a good idea. (think - думать)'},
             {'sentence':'I [[am thinking]] of going to study abroad. (think - думать)'         },
             {'sentence':'Your room [[smells]] awful! (smell - иметь запах, нюхать)'},
             {'sentence':'The cat [[is smelling]] the milk. (smell - иметь запах, нюхать)'},
             {'sentence':'I [[see]] what you mean. (see - видеть, видеться, понимать)'},
             {'sentence':'I [[am seeing]] Tom tonight. (see - видеть, видеться, понимать)'},
             {'sentence':'They [[have]] a very big house. (have - иметь)'},
             {'sentence':'What awful noise! Our neighbors [[are having]] a party. (have - иметь)'},
             {'sentence':'I [[love]] oranges. (love  - любить)'},
             {'sentence':'Our children [[are playing]] in the garden now. (play - играть)'},
             {'sentence':'This dress [[fits]] you perfectly. (fit - подходить по размеру, устанавливать)'},
             {'sentence':'Where is Dad? - He [[is fitting]] those new locks now. (fit - подходить по размеру, устанавливать)'},
             {'sentence':'That [[sounds]] wonderful! (sound - звучать)'},
             {'sentence':'I [[am listening]] to you very attentively. I am all ears. Carry on. (listen - слушать)'},
             {'sentence':'I [[promise]] to be back soon. (promise - обещать)'},
             {'sentence':'Right now, Tom [[is writing]] the letter. (write - писать)'},
             {'sentence':'He [[owns]] several large companies. (own -  владеть)'},
             {'sentence':'Somebody [[is knocking]] the door. Could you open it? (knock - стучать)'},
             {'sentence':'I [[know]] the answer. (know - знать)'},
             {'sentence':'He [[is drinking]] too much coffee these days. (drink - пить)'},
             {'sentence':'He [[understands]] me very well. (understand - понимать)'},
             {'sentence':'It is evening. I [[am watching]] a movie now. (watch - смотреть)'},
             {'sentence':'He [[does]] sport every day. (do - делать, заниматься)'},
             {'sentence':'They [[are cooking]] dinner at the moment. (cook - готовить)'},
             {'sentence':'John [[likes]] reading very much. (like - нравиться)'},
             {'sentence':'They [[are doing]] their homework now. (do - делать, заниматься)'},
             {'sentence':'She [[dislikes]] eating fish. (dislike - не любить)'},
             {'sentence':'Hush! The kids [[are sleeping]] (sleep - спать)'},
             {'sentence':'Unfortunately, my husband [[hates]] dancing. (hate - ненавидеть)'},
             {'sentence':'Pete [[is training]] to participate in the Olympics this month. (train - тренироваться)'},
             {'sentence':'This diet [[consists]] of mainly fruit and vegetables. (consist - состоять)'},
             {'sentence':'I don’t feel well. I [[am going]] to bed. (go - идти)'}]

from random import shuffle
# randomizing in place
shuffle(sentences[:24])
print(len(sentences))
