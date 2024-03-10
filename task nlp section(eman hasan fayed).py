import nltk
text = input("Enter the text: ")
print("Choose one of the following options:")
print("1-Print tokenized words")
print("2-Print tokenized sentences")
print("3-Print output using split function")
choice_number = input("Enter number: ")
if choice_number == '1':
    tokenized_words = nltk.word_tokenize(text)
    print(tokenized_words)
elif choice_number == '2':
    tokenized_sentences = nltk.sent_tokenize(text)
    print(tokenized_sentences)
elif choice_number == '3':
    split_output = text.split()
    print(split_output)
else:
    print("Please enter a valid choice number.")
