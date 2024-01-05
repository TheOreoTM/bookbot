def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    num_words = len(words)
    chars_dict = get_chars_dict(text)
    format_report(total_words=num_words, path=book_path, chars_dict=chars_dict)
    
def get_chars_dict(text):
  chars = {}
  for c in text:
    if not c.isalpha():
      continue
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] = chars[lowered] + 1
    else:
      chars[lowered] = 1

  return chars

def format_report(total_words, path ,chars_dict):
  print(f"--------- Report for {path} ---------")

  padding = " " * len("---------")  

  for c in chars_dict:
    amount = chars_dict[c]

    print(f"{padding} The character '{c}' appears {amount} times")

  print(f"\n{padding} A total of {total_words} were found")
  print("------------------ End report ------------------")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()