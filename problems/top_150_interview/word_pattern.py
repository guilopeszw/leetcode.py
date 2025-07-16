def word_pattern(pattern: str, s: str) -> bool:
    split = s.split()
    if len(pattern) != len(split): # if the lengths are different, they're not a match
        return False
    mapping = {}
    for p, word in zip(pattern, split):
        if p in mapping:
            if mapping[p] != word:
                return False
        else:
            if word in mapping.values():
                return False
            mapping[p] = word
    return True