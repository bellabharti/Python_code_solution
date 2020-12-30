def remove_duplicates(InList):
    InList2 = []
    if InList:
        for item in InList:
            if item not in InList2: # Is item in InList2 already?
                InList2.append(item)
    else:
        return InList
    return InList2
print (remove_duplicates([1,2,2,3,4,4,5,6,6,7,9,7,8]))