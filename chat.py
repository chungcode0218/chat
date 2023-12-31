#讀取原始FB對話紀錄，轉成較好閱讀之形式

def read_file(filename):
	lines=[]
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
		return lines
#格式轉換
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')
			

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
