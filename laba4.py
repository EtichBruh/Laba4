N = int(input('введите n'))
n = range(1,N)
#(1^5 + 2^5 + 3^5 +…+ n^5) +(1^7 + 2^7 + 3^7+…+ n^7) = 2 (1 + 2 + 3 +…+ n)^4
summ1 = 0
summ2 = 0
for i in n:
  summ1 += i**5
  summ2 += i**7
total = summ1 + summ2
print(total)

answer = 2 * sum(n)**4
print(answer)
print(total,' = ',answer)
