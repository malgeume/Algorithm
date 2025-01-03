max_num = 11
min_num = 0
while 1:
    num = int(input())
    if num == 0:
        break
    ans = input()
    if ans == "too high":
        if max_num > num:
            max_num = num
    elif ans == "too low":
        if min_num < num:
            min_num = num
    else:
        if min_num < num < max_num:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        max_num = 11
        min_num = 0