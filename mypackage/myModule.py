def top_n (items, n):
    ''' Return the top n items of an array in descending order.

    Args:
        items(array): list or array like objects
        n(int): number of items to return

    Return:
        array: Top n items in descending order

    Eg:
        top_n([8,3,2,1,7,4], 3)
        [8,7,4]
    '''

    for i in range(n): #keep sorting until we find the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: #if this item is bigger than next item
                items[j], items[j+1]= items[j+1], items[j] #swap the two

    #get two last items
    top_n= item[-n:]
    #return in descending order
    return top_n[::-1]