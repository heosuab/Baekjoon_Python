multiplier = int(input())
multiplicand = input()

product_1 = multiplier * int(multiplicand[-1])
product_2 = multiplier * int(multiplicand[-2])
product_3 = multiplier * int(multiplicand[-3])

product = product_1 + product_2*10 + product_3*100

print(product_1, product_2, product_3, product, sep='\n')