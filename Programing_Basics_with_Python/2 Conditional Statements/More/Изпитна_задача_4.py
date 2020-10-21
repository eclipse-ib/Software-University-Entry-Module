# Парички

bitcoin = int(input())
ch_v = float(input())
comis = float(input())


one_lev = 1
one_bitcoin = bitcoin * 1168 * one_lev
one_dollar = one_lev * 1.76
one_ch_v = ch_v * one_dollar * 0.15
one_euro = one_lev * 1.95

sum_in_lev = one_bitcoin + one_ch_v
sum_in_euro = sum_in_lev / one_euro

comis = (comis / 100)*sum_in_euro

final_sum = sum_in_euro - comis

print(final_sum)


