def longest_common_subsequence(s1, s2):

    s1_len = len(s1)
    s2_len = len(s2)

    lcs = [[None] * (s2_len + 1) for _ in xrange(s1_len + 1)]

    for i in xrange(s1_len + 1):
        for j in xrange(s2_len + 1):

            if i == 0 or j == 0:
                lcs[i][j] = 0

            elif s1[i - 1] == s2[j - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]

            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    # print lcs
    return lcs[s1_len][s2_len]

s1 = "AGGTAB"
s2 = "GXTXAYB"

print longest_common_subsequence(s1, s2)
