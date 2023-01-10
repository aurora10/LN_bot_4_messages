list1 = ["Alex", "John", "Bill", "Tom", ]

list2 = ["Connect", "Follow", "Connect", "Connect"]

#res = [item for item in zip(list1, list2) if 'Follow' not in item[1]]


size = len(list1)
res = []
for i in range(size):
    if list2[i] == "Connect":
        res.append( (list1[i]) )
print(res)
