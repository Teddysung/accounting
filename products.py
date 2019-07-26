product = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	rate = input('請給分: ')
	product.append([name, price, rate])
print(product)
for p in product:
	print(p[0], '的價格是', p[1])
with open('product.csv', 'w',) as f:
	f.write('商品,價格,評分\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n') 
