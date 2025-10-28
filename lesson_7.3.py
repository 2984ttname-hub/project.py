def common_elements():
    list1 = [i for i in range(100) if i % 3 == 0]
    list2 = [i for i in range(100) if i % 5 == 0]

    set1 = set(list1)
    set2 = set(list2)
    common = set1 & set2
    return common

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print("ОК")
