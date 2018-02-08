"""
build_tree(data)
    if data.shape[0] == 1: return[leaf, data.y, NA, NA]
    if all data.y same: return[leaf, data.y, NA, NA]
    else
        determine best feature i to split on
        SplitVal = data[:,i].median()
        lefttree = build_tree(data[data[:,i]<=SplitVal])
        righttree = build_tree(data[data[:,i]>SplitVal])
        root = [i, SplitVal, 1, lefttree.shape[1]+1]
        return(append(root, lefttree, righttree))
"""
