def solve():
    # 19: find the number of sundays that fell on the first of the month during the twentieth century
    # runtime: O(n) for n ~ # of months
    # ans = 171
    ans = 0
    # 0, 1, 2,..., 6 = mon, tue, wed,..., sun
    # Jan 1st 1901 was a tuesday
    day = 1
    for y in range(1901, 2001):
        for m in range(12):
            ans += day == 6
            day = (day + month_length(m, y)) % 7
    return ans


def month_length(m, y):
    month_lengths = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    return month_lengths[m] + int(m == 1 and y % 4 == 0 and y % 100 != 0)
