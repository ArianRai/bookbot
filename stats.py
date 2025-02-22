def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def count_words(text):
	words = text.split()
	num_words = len(words)
	return num_words

def count_characters(text):
	word_count = {}
	for letter in text:
		lower_letter = letter.lower()
		if lower_letter in word_count:
			word_count[lower_letter] += 1
		else:
			word_count[lower_letter] = 1
	return word_count

def sort_on(dict):
    return dict["count"]

def sort_dicts(dict):
	dicts_list = []
	for key in dict:
		if not key.isalpha():
			continue
		dicts_list.append({"letter": key, "count": dict[key]})
	dicts_list.sort(reverse=True, key=sort_on)
	for dict in dicts_list:
		print(f"{dict["letter"]}: {dict["count"]}")