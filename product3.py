product = []
import os
if os.path.isfile('product.csv'):
	print('檔案:可惡，被你找到了!')
	with open('product.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price, rate = line.strip().split(',')
			product.append([name, price, rate])
	print(product)
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
	with open('product.csv', 'w') as f:
		f.write('商品,價格,評分\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n')
else:
	print('檔案:哈哈你找不到我吧，因為我不存在........')
	print('我:誰理你啊，我再創一個!!!')
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
	with open('product.csv', 'w') as f:
		f.write('商品,價格,評分\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n')