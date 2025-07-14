def index_first_occ(haystack: str, needle: str) -> int:
    index = haystack.find(needle)
    return index  # .find() returns -1 if needle is not found and the index otherwise