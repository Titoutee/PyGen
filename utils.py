def flatten(bi_l): # flattens a 2d array
    res = []
    for x in bi_l:
        for y in x:
            res.append(y)
    return res