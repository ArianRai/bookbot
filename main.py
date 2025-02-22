from stats import get_book_text, count_words, count_characters, sort_dicts
import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
	
relative_path = sys.argv[1]
def main():
	file_text = get_book_text(relative_path)
	num_words = count_words(file_text)
	number_of_letters = count_characters(file_text)
	print('============ BOOKBOT ============')
	print('----------- Word Count ----------')
	print(f"Analyzing book found at {relative_path}...")
	print('----------- Character Count ----------')
	print(f"Found {num_words} total words")
	sort_dicts(number_of_letters)
	print("============= END ===============")

main()