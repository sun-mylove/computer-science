def kmp_pattern_search(pat, txt):
    M = len(pat)
    N = len(txt)
    pattern_count = 0

    lps = [0] * M
    j = 0

    calc_lps(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            pattern_count += 1
            j = lps[j - 1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return pattern_count


def calc_lps(pat, M, lps):
    len = 0

    lps[0]
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]

            else:
                lps[i] = 0
                i += 1


pat = 'aba'
text = 'abababab'

print kmp_pattern_search(pat, text)
