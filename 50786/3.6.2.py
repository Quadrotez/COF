result_dict = dict(zip(input().split(), map(int, input().split())))
result_dict['Bob'] = 5

print(dict(sorted(result_dict.items())))
