def anagram_check(keywords):
    anagrams = defaultdict(list)
    for i in keywords:
        histogram=tuple(counter(i).items())
        anagrams[histogram].append(i)
        return list(anagram.values())
    keywords=("banana")
    print(anagram_check(keywords))
