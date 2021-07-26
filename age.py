drive = input('你有沒有開過車')
if drive != '有' and drive !='沒有':
	print('只能輸入有/沒有')
	raise SystemExit
age = input('請問你幾歲')
age = int(age)
if drive == '有':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('你犯法了')
elif drive == '沒有':
	if age >= 18:
		print('爛草莓')
	else:
		print('滾')

