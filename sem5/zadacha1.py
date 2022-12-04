# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# --> 'Я люблю абвЖвау иабв Питон'
# --> 'Я люблю Питон'
# # включений, filter, map


text='Я люблю абв абвЖвау иабв Питон'.split()
rez= [i for i in text if "абв" not in  i]
print(join(rez))

# my_string = 'Я люблю абвЖвау иабв Питон'

# my_li = my_string.split()
# print(my_li)

# my_li = list(filter(lambda el: not "абв" in el, my_li))
# print(my_li)

# my_string = ' '.join(my_li)
# print(my_string)
