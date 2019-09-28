'''
    var_set = list containing the starting set;
    used = set of currently used elements from var_set;
    curr_subset = current subset;
'''
def power_set(min_index, var_set, curr_subset):
    if(min_index == len(var_set)):
        return
    
    for ii in range(min_index,len(var_set)):
        elem = var_set[ii]
        curr_subset.append(elem)
        yield curr_subset
        yield from power_set(ii+1, var_set, curr_subset)
        del curr_subset[-1]

var_set = [1,2,3,4,5]
curr_subset = []
generator = power_set(0,var_set,curr_subset)

for elem in generator:
    print(elem)
