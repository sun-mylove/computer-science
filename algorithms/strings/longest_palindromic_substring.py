
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

    ans_found = False
    answer = 1
    answer_substring = ""

    for k in xrange(str_len, 1, -1):
        subs = build_sub_strings(s, k)

        for sub in subs:
            if is_palindrome(sub):
                answer = len(sub)
                answer_substring = sub
                ans_found = True
                break

        if ans_found:
            break

    return answer, answer_substring

print palindromic_sub_strings('abaaa')
