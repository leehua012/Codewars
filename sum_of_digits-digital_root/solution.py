def digital_root(n):
    # 1. cast number to string and split
    new = [a for a in str(n)]
    # 2. cast string to number and perform summation
    total = sum([int(new[i]) for i in range (len(new))])
    # 3. recursion if total isn't ones
    if total > 9:
        return digital_root(total)
    else:
        return total
        
