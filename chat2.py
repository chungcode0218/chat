#讀取原始LINE對話紀錄，轉成較好閱讀之形式

#讀取檔案
def read_file(filename):
	lines=[]
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines
#格式轉換
def convert(lines):
	person = None
	word_count_1 = 0
	word_count_2 = 0
	sticker_count_1 = 0
	sticker_count_2 = 0
	image_count_1 = 0
	image_count_2 = 0
	for line in lines:
		s = line.split('\t')
		time = s[0]
		name = s[1]
		if name == '蔣將':
			if s[2] == '貼圖':
				sticker_count_1 += 1
			elif s[2] == '圖片':
				image_count_1 += 1
			else:
				for m in s[2:]:
					word_count_1 += len(m)
		elif name == '鍾隆一':
			if s[2] == '貼圖':
				sticker_count_2 += 1
			elif s[2] == '圖片':
				image_count_2 += 1
			else:
				for m in s[2:]:
					word_count_2 += len(m)
	print('蔣將說了', word_count_1, '個字，並傳了', sticker_count_1, '個貼圖、', image_count_1, '張圖片')
	print('鍾隆一說了', word_count_2, '個字，並傳了', sticker_count_2, '個貼圖、', image_count_2, '張圖片')
		#print(s[1])
#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')
			
#主程式
def main():
	lines = read_file('Linechat.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()
