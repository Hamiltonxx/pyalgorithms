from bisect import bisect
def num_samller_frequency(queries, words):
    f = lambda word: word.count(min(word))
    words = sorted(map(f, words))
    return [len(words) - bisect(words, f(query)) for query in queries]