import random
def get_random(floor, ceil):
    return random.randrange(floor, ceil + 1)
def shuffle(list):
    for i in range(0, len(list) - 1):
        j = get_random(0, len(list) - 1)
        if j != i:
            list[i], list[j] = list[j], list[i]
sample_list = [1, 2, 3, 4, 5]
print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)
