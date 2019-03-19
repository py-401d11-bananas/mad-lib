from random import *

# story_one = """Albert Einstein, the son of MaleCelebrity and FemaleCelebrity, was born in Ulm, Germany, in 1879. In 1902, he had a job as assistant Noun in the Swiss patent office and attended the University of Zurich. There he began studying atoms, molecules, and PluralNoun. He developed the theory of Adjective relativity, which expanded the phenomena of sub-atomic PluralNoun and Adjective magnetism. In 1921, he won the Nobel prize for PluralNoun and was director of theoretical physics at the Kaiser Wilhelm Noun in Berlin. In 1933, when Hitler became Chancellor of Germany, Einstein came to America to take a post at Princeton Institute for PluralNoun, where his theories helped America devise the first atomic bomb. There is no question about it: Einstein was one of the most brilliant PluralProfession of our time. ['Male Name', '*', '*', 'Noun', '*', 'Male Celebrity', '*', 'Female Celebrity,', '*', 'Past Tense Verb', '*', '*', 'Country,', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'Adjective', 'Noun', '*', '*', 'Adjective', 'Adjective', 'Noun', '*', 'Past Tense Verb', '*', 'Noun', '*', '*', '*', '*', 'Past Tense Verb', 'Verb Ending in -ing', '*', '*', '*', '*', '*', 'Past Tense Verb', '*', 'Noun', '*', 'Adjective', '*', '*', 'Past Tense Verb', '*', 'Plural Noun', '*', 'Adjective', 'Plural Noun', 'and', 'Adjective', '*', '*', '*', '*', 'Past Tense Verb', '*', '*', 'Noun', '*', 'Plural Noun', '*', '*', 'Job Title', '*', 'Adjective', 'Noun', '*', '*', '*', '*', 'Noun', '*', '*', '*', '*', '*', 'Male Name', 'Past Tense Verb', 'Job Title', '*', '*', 'Male Name', 'Past Tense Verb', '*', 'Country', '*', 'Verb', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'Plural Noun', 'Past Tense Verb', 'Country', 'Verb', '*', '*', 'Adjective', '*', '*', '*', '*', 'Noun', '*', '*', 'Male Name', '*', '*', '*', '*', '*', 'Adjective', 'Plural Profession', '*', '*', '*']"""

# story_two = """Elizabeth, the Tudor Noun of England, was probably the Superlative-Adjective ruler the British ever had. Elizabeth was the daughter of Henry the Eighth and Ane Boleyn. Later, Anne had her Noun chopped off by Henry. Elizabeth was born in 1533 and became queen when she was 25. She was a Adjective Protestant and persecuted the Adjective Catholics Adverb. In 1588, the Armada attacked England. But the English fleet, commanded by Celebrity and Different   Celebrity, defeated them. Elizabeth ruled for 45 years, and during her reign England prospered and produced Shakespeare, Francis Bacon, and Name of Person. Elizabeth never married, which is why she is sometimes called the Adjective.Queen."""

story_three = {
    'title': 'The Boy Who Cried Wolf',

    'story': """Once upon a time, there lived a shepherd boy who was bored watching his flock of sheep on the hill. To amuse himself, he shouted, “Wolf! Wolf! The sheep are being chased by the wolf!” The villagers came running to help the boy and save the sheep. They found nothing and the boy just laughed looking at their angry faces. “Don’t cry ‘wolf’ when there’s no wolf boy!”, they said angrily and left. The boy just laughed at them. After a while, he got bored and cried ‘wolf!’ again, fooling the villagers a second time. The angry villagers warned the boy a second time and left. The boy continued watching the flock. After a while, he saw a real wolf and cried loudly, “Wolf! Please help! The wolf is chasing the sheep. Help!” But this time, no one turned up to help. By evening, when the boy didn’t return home, the villagers wondered what happened to him and went up the hill. The boy sat on the hill weeping. “Why didn’t you come when I called out that there was a wolf?” he asked angrily. “The flock is scattered now”, he said. An old villager approached him and said, “People won’t believe liars even when they tell the truth. We’ll look for your sheep tomorrow morning. Let’s go home now”.""",

    'prompts': """*|*|*|*|*|Past Tense Verb|*|Profession|*|*|*|*|Verb Ending in -ing|*|*|*|Animal Plural|*|*|*|*|Verb|*|*|*|*|*|*|Animal Plural|*|*|Past Tense Verb|*|*|*|*|Plural Noun|*|Verb Ending in -ing|*|*|*|*|*|Verb|*|*|*|Past Tense Verb|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|Adjective|*|*|Verb|*|*|*|*|Aniimal|*|*|Past Tense Verb|Adverb|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Verb Ending in -ing|*|Plural Noun|*|*|*|*|Adjective|Plural Noun|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|*|*|*,|*|Past Tense Verb|*|Adjective|Animal|*|Past Tense Verb|*|*|*|*|*|Animal|*|Verb Ending in -ing|*|*|*|*|*|*,|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Verb|*|*|Plural Noun|Past Tense Verb|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Noun|*|*|*|*|Verb|*|*|Past Tense Verb|*|*|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Adjective Beginning with a Vowel|Noun|Past Tense Verb|*|*|*|*|*|*|Plural Noun|*|*|*|Verb|*|*|*|Verb|*|*|Animal Plural|*|*|*|*|*|*"""
}

story_four = {
    'title': 'The Golden Egg',

    'story': """Once upon a time, a farmer had a goose that laid a golden egg every day. The egg provided enough money for the farmer and his wife for their day-to-day needs. The farmer and his wife were happy for a long time. But one day, the farmer got an idea and thought, “Why should I take just one egg a day? Why can’t I take all of them at once and make a lot of money?” The foolish farmer’s wife also agreed and decided to cut the goose’s stomach for the eggs. As soon as they killed the bird and opened the goose’s stomach, to find nothing but guts and blood. The farmer, realizing his foolish mistake, cries over the lost resource!""",

    'prompts': """*|*|*|*,|*|Profession|*|*|Animal|*|Past Tense Verb|*|Adjective|Noun|*|*|*|Noun|Past Tense Verb|*|Plural Noun|*|*|Profession|*|*|*|*|*|*|*|*|Profession|*|*|*|*|*|*|*|*|*|*|*|*|*|Profession|*|*|Noun Beginning with a Vowel|*|*|*|*|*|Verb|*|*|Noun|*|*|*|*|*|Verb|*|*|*|*|*|*|*|*|*|*|*|*|Adjective|*|*|*|Past Tense Verb|*|Past Tense Verb|*|Verb|*|*|Body Part|*|*|*|*|*|*|*|Past Tense Verb|*|Animal|*|Past Tense Verb|*|*|*|*|*|*|*|Plural Noun|*|*|*|*|Verb Ending in -ing|*|Adjective|*|*|*|*|Adjective|*"""
}

story_five = ('The Wet Pants', """A nine-year-old boy was sitting at his desk in class, when suddenly, his pants felt wet, and there was a puddle at his feet. His heart almost skipped a beat, as he got worried that his classmates would see that and make fun of him. He quickly wanted to do something, and saw the teacher and his classmate Susie walking towards him. Susie was carrying a bowl of goldfish. As they came closer, the boy thought that the teacher noticed his wet pants, and suddenly Susie trips and drops the fishbowl in his lap. While thanking God for helping him, he pretends to get angry with Susie and yells at her. Everyone in the class thinks it is Susie’s fault that the boy’s pants got wet. The teacher helps the boy change into dry clothes, and the class continues. Later that evening, the boy asks Susie, “You did that on purpose, didn’t you?” “I wet my pants once too”, whispers Susie.""")


arr = ['*', '*', '*', '*,', '*', 'Profession', '*', '*', 'Animal', '*', 'Past Tense Verb', '*', 'Adjective', 'Noun', '*', '*', '*', 'Noun', 'Past Tense Verb', '*', 'Plural Noun', '*', '*', 'Profession', '*', '*', '*', '*', '*', '*', '*', '*', 'Profession', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'Profession', '*', '*', 'Noun Beginning with a Vowel', '*', '*', '*', '*', '*', 'Verb', '*', '*', 'Noun', '*', '*', '*', '*', '*', 'Verb', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'Adjective', '*', '*', '*', 'Past Tense Verb', '*', 'Past Tense Verb', '*', 'Verb', '*', '*', 'Body Part', '*', '*', '*', '*', '*', '*', '*', 'Past Tense Verb', '*', 'Animal', '*', 'Past Tense Verb', '*', '*', '*', '*', '*', '*', '*', 'Plural Noun', '*', '*', '*', '*', 'Verb Ending in -ing', '*', 'Adjective', '*', '*', '*', '*', 'Adjective', '*']


def split_story(dict):
    return dict['story'].split(' ')


def join_story(arr):
    return '|'.join(arr)


# def split_prompts(dict):
#     return


# def create_prompts()

# prompts = []

# for word in range(10):
#     rand = randint(0, len(index_array)-1)
#     while index_array[rand] == '*':
#         rand = randint(0, len(index_array)-1)
#     else:
#         prompts.append((rand, index_array[rand]))

# print(new_story)

# print(split_story)
# print(index_array)

# print(len(split_story))
# print(len(index_array))

# for tuple in prompts:
#     split_story[tuple[0]] = tuple[1]

# new_story = ' '.join(split_story)

# print(prompts)

# print(new_story)

print(split_story(story_four))

print(join_story(arr))
