import markovify

def get_model(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    return markovify.Text(text, state_size=1)

files = ['male.txt', 'female.txt']


for file in files:
	for i in range(10):
		print(get_model(file).make_sentence())
