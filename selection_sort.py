# Selection sort

# It has an O(n^2) time complexity,

songs = [["Love song", 1983], ["Funny song", 1988], ["Sad song", 1876],
         ["Top song", 2154], ["Dramatic sond", 1327], ["Millitary song", 2000]]


# here we have a list of songs, with different number of listenings
# I will sort this list from top-listened to less-listened song

def find_top_song(list):  # first i will find which song has the most listenings and return it's index
    index = 0
    top = 0
    for num in range(len(list)):
        if list[num][1] > top:
            top = list[num][1]
            index = num
        else:
            pass
    return index


def selection_sort(items):  # this function is sorting the list
    sorted_items = []  # creating an empty list
    while items:
        sorted_items.append(items[find_top_song(songs)])  # adding an item with most listenings, to our new list
        items.pop(find_top_song(songs))  # deleting an item from a given list
    return sorted_items  # returning sorted list


print(selection_sort(songs))
