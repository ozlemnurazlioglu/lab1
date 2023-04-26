def common_elements(list1, list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common

list1 = [7,8,9,10,11]
list2 = [12,13,14,15,16]
common = common_elements(list1, list2)
print(common)