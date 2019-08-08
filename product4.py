import os

def check(filename):
	return os.path.isfile(filename)
	#boolean
def found():
	print('檔案:可惡，被你找到了!')
	#words
def read_file(filename):
	product = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price, rate = line.strip().split(',')
			product.append([name, price, rate])
	print(product)
	return product
def input22(product):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入價格: ')
		rate = input('請給分: ')
		product.append([name, price, rate])
	print(product)
	return product
def print_out(product):
	for p in product:
		print(p[0], '的價格是', p[1], '評分是', p[2])
def write_to_file(filename, product):
	with open(filename, 'w') as f:
		f.write('商品,價格,評分\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n')

def cannot_find():
	product = []
	print('檔案:哈哈你找不到我吧，因為我不存在........')
	print('我:誰理你啊，我再創一個!!!')
	return product
#input
#write_to_file
b = check('product.csv')
if b:
	found()
	product = read_file('product.csv')
	product = input22(product)
	print_out(product)
	write_to_file('product.csv', product)
else:
	product = cannot_find()
	product = input22(product)
	print_out(product)
	write_to_file('product.csv', product)
