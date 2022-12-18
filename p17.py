def solve():
    # 17: find the total number of alphabetical character in all numbers from 1 through 1000 when written out
    # runtime: O(log10(x)) to write out an integer x
    # ans = 21124
    n = 1000
    ans = 0
    for i in range(1, n + 1):
        ans += len(list(filter(lambda c: ord('a') <= ord(c) <= ord('z'), int_to_english(i))))

    print(ans)


# number to english language conversion
digits = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
tens = (None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
teens_special = ("ten", "eleven", "twelve", "thirteen", "fourteen",
                 "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")


def two_digit_convert(x):
    match x // 10, x % 10:
        case 0, d:
            return digits[d]
        case 1, d:
            return teens_special[d]
        case t, 0:
            return tens[t]
        case t, d:
            return tens[t] + "-" + digits[d]


def three_digit_convert(x):
    match x // 100, x % 100:
        case 0, t:
            return two_digit_convert(t)
        case h, 0:
            return digits[h] + " hundred"
        case h, t:
            return digits[h] + " hundred and " + two_digit_convert(t)


def four_five_and_six_digit_convert(x):
    match x // 1000, x % 1000:
        case 0, t:
            return three_digit_convert(t)
        case h, 0:
            return three_digit_convert(h) + " thousand"
        case h, t:
            return three_digit_convert(h) + " thousand " + ("and " if t // 100 else "") + three_digit_convert(t)


def int_to_english(x):
    return four_five_and_six_digit_convert(x)
