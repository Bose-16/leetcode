def kth_distinct_string(arr, k):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    distinct =[]
    for i in arr:
        if count[i]==1:
            distinct.append(i)
    print(distinct)
    if len(distinct) >= k:
        return distinct[k-1]
    else:
        return ""
arr = ["d", "b", "c", "b", "c", "a"]
k = 2
result = kth_distinct_string(arr, k)
print(result)
