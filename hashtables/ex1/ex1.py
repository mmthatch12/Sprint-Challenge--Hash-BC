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
        ht.hash_table_insert(weights[i], i)
    for wei in range(length):
        if ht.hash_table_retrieve(ht, weights[wei]-limit):
            if wei > weights[weights[wei]-limit]:
                return [wei, weights[weights[wei]-limit]]
            else:
                return [weights[weights[wei]-limit], wei]
        else:
            return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
