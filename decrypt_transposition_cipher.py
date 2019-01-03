
import math

def main():
	message = "keim,ginlhrndsi ioceelog tinnis dwelema r wl idatecto"
	key = 5

	decrypt_text = decrypt_message(key, message)
	print (decrypt_text + '|')

def my_ceil(num):
    result = int(num)
    return result if result == num or num < 0 else result+1

def decrypt_message(my_key, my_message):
	len_msg = len(my_message)
	#num_columns = math.ceil(len(my_message)/my_key)

	c = (len_msg/my_key)
	num_columns = my_ceil(c)

	num_rows = my_key

	num_boxes = (num_columns * num_rows) - len(my_message)

	decrypt_text = [''] * num_columns

	column = 0
	row = 0

	for symbol in my_message:
		decrypt_text[column] += symbol
		column += 1

		if (column == num_columns) or (column == num_columns-1 and row >= num_rows-num_boxes):
			column = 0
			row += 1
	return ''.join(decrypt_text)

if __name__ == '__main__':
	main()

