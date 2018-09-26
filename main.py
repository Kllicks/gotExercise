from got import characters

# instead of repeating code. write a function: 
def first_Letter_Count(letter):
    count = 0
    for person in characters:
        if person['name'][0] == letter:
            count = count + 1
    return count   

# How many characters names start with "A"?
 
# count = 0
# for person in characters:
#     if person['name'] != '' and person['name'][0] == "A":
#         count = count + 1
# print(count)

starts_with_a = first_Letter_Count('A')
print(starts_with_a)

# How many characters names start with "Z"?

# count = 0
# for person in characters:
#     if person['name'] != '' and person['name'][0] == "Z":
#         count = count + 1
# print(count)

starts_with_z = first_Letter_Count('Z')
print(starts_with_z)

# How many characters are dead?
def how_many_dead():
    count = 0
    for person in characters:
        if person['died'] != '':
            count = count + 1
    return count 

dead_count = how_many_dead()
print('%d characters are dead' % (dead_count))  

# Who has the most titles?
title_lengths = []
for person in characters:
    # get the length of the 'title' key
    num_titles = len(person['titles'])
    title_lengths.append(num_titles)
record_for_most_titles = max(title_lengths)
print(record_for_most_titles)

index_of_record = title_lengths.index(record_for_most_titles)
# print(index_of_record)
person_with_title_record = characters[index_of_record]
print(person_with_title_record['name'])


# How many are Valyrian?
def how_many_valyrians():
    count = 0
    for culture in characters:
        if culture['culture'] == 'Valyrian':
            count += 1
    return count
valyrian_count = how_many_valyrians()
print('%d characters are Valyrian' % (valyrian_count))

# What actor plays "Hot Pie" (and don't use IMDB)?

    # print(person['playedBy'][0]) the [0] will remove printed brackets
for person in characters:
    if person['name'] == 'Hot Pie':
        # print('heres hot pie')
        # print(person)
        print(person['playedBy'][0])
        break

# How many characters are *not* in the tv show?
# no_show = []
# for person in characters:
#     num_shows = len(person['tvSeries'])
#     if num_shows == 0:
#         no_show.append(num_shows)
# print(no_show)

# Produce a list characters with the last name "Targaryen"
for person in characters:
    name1 = person['name']
    name2 = name1.split(' ')
    for i in name2:
        if i == 'Targaryen':
            print(person['name'])


# Create a histogram of the houses (it's the "allegiances" key)