from textblob import TextBlob

sentence = TextBlob('Use 4 spaces, per indentation level.')
sentence.words
# sentence.words[2].singularize()
# sentence.words[-1].pluralize()

print(sentence.words[3])
print(sentence.words.pluralize())
