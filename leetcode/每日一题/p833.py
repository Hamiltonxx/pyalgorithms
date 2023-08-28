def findReplaceString(s, indices, sources, targets):
    modified = list(s)
    for idx, source, target in zip(indices,sources,targets):
        if s[idx:].startswith(source):
            modified[idx] = target
            for i in range(idx+1, idx+len(source)):
                modified[i]=""
    return "".join(modified)



