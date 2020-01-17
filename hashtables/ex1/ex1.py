#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    for w in range(length):
        if hash_table_retrieve(ht, weights[w]-limit):
            if w > weights[w]-limit:
                return [w, weights[w]-limit]
            else:
                return [weights[w]-limit, w]
        else:
            return None

print(get_indices_of_item_weights([4,6,10,15,16],5,21))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


