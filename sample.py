from random import *

story = """Albert Einstein, the son of MaleCelebrity and FemaleCelebrity, was born in Ulm, Germany, in 1879. In 1902, he had a job as assistant Noun in the Swiss patent office and attended the University of Zurich. There he began studying atoms, molecules, and PluralNoun. He developed the theory of Adjective relativity, which expanded the phenomena of sub-atomic PluralNoun and Adjective magnetism. In 1921, he won the Nobel prize for PluralNoun and was director of theoretical physics at the Kaiser Wilhelm Noun in Berlin. In 1933, when Hitler became Chancellor of Germany, Einstein came to America to take a post at Princeton Institute for PluralNoun, where his theories helped America devise the first atomic bomb. There is no question about it: Einstein was one of the most brilliant PluralProfession of our time."""

split_story = story.split(' ')

index_array = ['Male Name', '*', '*', 'Noun', '*', 'Male Celebrity', '*', 'Female Celebrity,', '*', 'Past Tense Verb', '*', '*', 'Country,', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'Adjective', 'Noun', '*', '*', 'Adjective', 'Adjective', 'Noun', '*', 'Past Tense Verb', '*', 'Noun', '*', '*', '*', '*', 'Past Tense Verb', 'Verb Ending in -ing', '*', '*', '*', '*', '*', 'Past Tense Verb', '*', 'Noun', '*', 'Adjective', '*', '*', 'Past Tense Verb', '*', 'Plural Noun', '*', 'Adjective', 'Plural Noun', 'and', 'Adjective', '*', '*', '*', '*', 'Past Tense Verb', '*', '*', 'Noun', '*', 'Plural Noun', '*', '*', 'Job Title', '*', 'Adjective', 'Noun', '*', '*', '*', '*', 'Noun', '*', '*', '*', '*', '*', 'Male Name', 'Past Tense Verb', 'Job Title', '*', '*', 'Male Name', 'Past Tense Verb', '*', 'Country', '*', 'Verb', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'Plural Noun', 'Past Tense Verb', 'Country', 'Verb', '*', '*', 'Adjective', '*', '*', '*', '*', 'Noun', '*', '*', 'Male Name', '*', '*', '*', '*', '*', 'Adjective', 'Plural Profession', '*', '*', '*']


prompts = []

for word in range(10):
    rand = randint(0, len(index_array)-1)
    while index_array[rand] == '*':
        rand = randint(0, len(index_array)-1)
    else:
        prompts.append((rand, index_array[rand]))

# print(new_story)

# print(split_story)
# print(index_array)

# print(len(split_story))
# print(len(index_array))

for tuple in prompts:
    split_story[tuple[0]] = tuple[1]

new_story = ' '.join(split_story)

print(prompts)

print(new_story)
