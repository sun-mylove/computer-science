
def build_sub_strings(s, k):
    sub_strings = []

    for i in xrange(str_len - k + 1):
        sub_strings.append(s[i:i + k])

    return sub_strings


def is_palindrome(sub):
    l = len(sub)

    for b in xrange(l):
        e = l - 1 - b

        if b <= e and sub[b] != sub[e]:
            return False

    return True


def palindromic_sub_strings(s):
    global str_len
    str_len = len(s)

    count = 0
    all_palindromic_subs = []

    for k in xrange(1, str_len + 1):
        subs = build_sub_strings(s, k)

        for sub in subs:
            if is_palindrome(sub):
                count += 1
                all_palindromic_subs.append(sub)

    return count, all_palindromic_subs


print palindromic_sub_strings('geek')
