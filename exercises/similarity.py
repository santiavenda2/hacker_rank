from itertools import izip


def word_similarity(a, b):
    similarity = 0
    for c, d in izip(a, b):
        if c == d:
            similarity += 1
        else:
            return similarity
    return similarity


def suffixes(word):
    word_len = len(word)
    return (word[i:] for i in xrange(1, word_len))


def suffix_similarities(word):
    return sum(word_similarity(word, suffix) for suffix in suffixes(word)) + len(word)

if __name__ == '__main__':
    # print word_similarity("aaa", "aaab")
    #
    # print list(suffixes("abc"))

    print suffix_similarities("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

