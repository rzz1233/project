my_dict = {'b': 2, 'a': 1, 'c': 3}
print(my_dict.items())
print(sorted(my_dict.items()))  #列表
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)  # 输出: {'a': 1, 'b': 2, 'c': 3}



