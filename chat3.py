
lines = []
with open('3.txt', 'r', encoding='utf-8-sig')as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split('\t')
	time = s[0][:7]
	name = s[0][7:]
	print(time)
	print(name)
