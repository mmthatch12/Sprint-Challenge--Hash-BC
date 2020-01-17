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
    final = []
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    for w in range(length):
        # print(limit - weights[w])
        if hash_table_retrieve(ht, limit - weights[w]):
            # print('above if')
            final = [w, weights.index(limit - weights[w])]
            # if w > limit - weights[w]:
            #     final[0] = w 
            #     final[1] = limit - weights[w]
            #     return final
            # else:
            #     final[0] = limit - weights[w]
            #     final[1] = w
            #     return final
    if len(final):
        return final
    else:
        return None
        # else:
        #     print('straight to else')
        #     return None

# print(get_indices_of_item_weights([4,6,10,15,16],5,21))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


