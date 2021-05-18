import random

r = random.randint(1, 100)
while True:
	num = input('請輸入 1 ～ 100 之間的數字: ')
	num = int(num)
	if num == r:
		print('恭喜你猜對了！')
		break
	elif num > r:
		print('數字還要再小一點～')
	else:
		print('數字還要再大一點～')
