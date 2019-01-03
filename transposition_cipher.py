
def main():
	message = "knowledge is limited, imagination encircles the world"
	key = 5

	crypt_text = Message_Encrypt(key, message)

	print (crypt_text + '|')

def Message_Encrypt(key, message):
	crypt_text = ['']*key
	for column in range(key):

		place = column
		while place < len(message):

			crypt_text[column] += message[place]
			place += key

	return ''.join(crypt_text)

if __name__ == '__main__':
	main()