def empirical_pmf(samples):
    ans = []
    ht = {}
    n = len(samples)
    for num in samples:
        if num in ht:
            ht[num] += 1
        else:
            ht[num] = 1
    
    for k, v in ht.items():
        ans.append((k, float(v/n)))

    return ans
