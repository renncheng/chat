# python test for chat2--LINE format

def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
	

def convert(lines):
	new = []
	persion = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		data_split = line.split(' ')
		time = data_split[0]
		name = data_split[1]
		if name == 'Allen':
			if data_split[2] == '貼圖':
				allen_sticker_count += 1
			elif data_split[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in data_split[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if data_split[2] == '貼圖':
				viki_sticker_count += 1
			elif data_split[2] == '圖片':
				viki_image_count += 1
			else:
				for msg in data_split[2:]:
					viki_word_count += len(msg)
	print('allen says= ', allen_word_count, 'words, and sends', allen_sticker_count, 'plots and', allen_image_count, 'images')
	print('viki says= ', viki_word_count, 'words, and sends', viki_sticker_count, 'plots and', viki_image_count, 'images')
	return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE.txt')
	lines = convert(lines)

main()