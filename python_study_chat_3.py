# python test for chat3--LINE format

lines = []
with open ('LINE2.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	msg = s[1]
	print('Time= ', time)
	print('Nmae= ', name)
	print(msg)
	