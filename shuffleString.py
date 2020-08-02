def restoreString(string, indices):
    ans = [0 for _ in string]
    for index, char in enumerate(string):
        ans[indices[index]] = char
    return "".join(ans)

print(restoreString(string, indices))
