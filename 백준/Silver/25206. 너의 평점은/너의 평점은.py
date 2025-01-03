grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum_score = 0
sum_credit = 0
for i in range(20):
    subject, credit, got = input().split()
    credit = float(credit)
    if got != 'P':
        sum_score += grade[got] * credit
        sum_credit += credit
print(sum_score / sum_credit)