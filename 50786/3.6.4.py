result_dict = dict(zip(input().split(), map(int, input().split())))
if 'Bob' not in result_dict:
    print("Bob is missing")
elif result_dict['Bob'] > 3:
    print("Fine")
else:
    print("Help")
