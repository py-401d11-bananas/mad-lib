from random import *

story_one = {
    'title': 'The Boy Who Cried Wolf',

    'story': """Once upon a time, there lived a shepherd boy who was bored watching his flock of sheep on the hill. To amuse himself, he shouted, “Wolf! Wolf! The sheep are being chased by the wolf!” The villagers came running to help the boy and save the sheep. They found nothing and the boy just laughed looking at their angry faces. “Don’t cry ‘wolf’ when there’s no wolf boy!”, they said angrily and left. The boy just laughed at them. After a while, he got bored and cried ‘wolf!’ again, fooling the villagers a second time. The angry villagers warned the boy a second time and left. The boy continued watching the flock. After a while, he saw a real wolf and cried loudly, “Wolf! Please help! The wolf is chasing the sheep. Help!” But this time, no one turned up to help. By evening, when the boy didn’t return home, the villagers wondered what happened to him and went up the hill. The boy sat on the hill weeping. “Why didn’t you come when I called out that there was a wolf?” he asked angrily. “The flock is scattered now”, he said. An old villager approached him and said, “People won’t believe liars even when they tell the truth. We’ll look for your sheep tomorrow morning. Let’s go home now”.""",

    'prompts': """*|*|*|*|*|Past Tense Verb|*|Profession|*|*|*|*|Verb Ending in -ing|*|*|*|Animal Plural|*|*|*|*|Verb|*|*|*|*|*|*|Animal Plural|*|*|Past Tense Verb|*|*|*|*|Plural Noun|*|Verb Ending in -ing|*|*|*|*|*|Verb|*|*|*|Past Tense Verb|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|Adjective|*|*|Verb|*|*|*|*|Aniimal|*|*|Past Tense Verb|Adverb|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Verb Ending in -ing|*|Plural Noun|*|*|*|*|Adjective|Plural Noun|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|*|*|*|*|Past Tense Verb|*|Adjective|Animal|*|Past Tense Verb|*|*|*|*|*|Animal|*|Verb Ending in -ing|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Verb|*|*|Plural Noun|Past Tense Verb|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Noun|*|*|*|*|Verb|*|*|Past Tense Verb|*|*|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Adjective Beginning with a Vowel|Noun|Past Tense Verb|*|*|*|*|*|*|Plural Noun|*|*|*|Verb|*|*|*|Verb|*|*|Animal Plural|*|*|*|*|*|*"""
}

story_two = {
    'title': 'The Golden Egg',

    'story': """Once upon a time, a farmer had a goose that laid a golden egg every day. The egg provided enough money for the farmer and his wife for their day-to-day needs. The farmer and his wife were happy for a long time. But one day, the farmer got an idea and thought, “Why should I take just one egg a day? Why can’t I take all of them at once and make a lot of money?” The foolish farmer’s wife also agreed and decided to cut the goose’s stomach for the eggs. As soon as they killed the bird and opened the goose’s stomach, to find nothing but guts and blood. The farmer, realizing his foolish mistake, cries over the lost resource!""",

    'prompts': """*|*|*|*|*|Profession|*|*|Animal|*|Past Tense Verb|*|Adjective|Noun|*|*|*|Noun|Past Tense Verb|*|Plural Noun|*|*|Profession|*|*|*|*|*|*|*|*|Profession|*|*|*|*|*|*|*|*|*|*|*|*|*|Profession|*|*|Noun Beginning with a Vowel|*|*|*|*|*|Verb|*|*|Noun|*|*|*|*|*|Verb|*|*|*|*|*|*|*|*|*|*|*|*|Adjective|*|*|*|Past Tense Verb|*|Past Tense Verb|*|Verb|*|*|Body Part|*|*|*|*|*|*|*|Past Tense Verb|*|Animal|*|Past Tense Verb|*|*|*|*|*|*|*|Plural Noun|*|*|*|*|Verb Ending in -ing|*|Adjective|*|*|*|*|Adjective|*"""
}

story_three = {
    'title': 'The Wet Pants',

    'story': """A nine-year-old boy was sitting at his desk in class, when suddenly, his pants felt wet, and there was a puddle at his feet. His heart almost skipped a beat, as he got worried that his classmates would see that and make fun of him. He quickly wanted to do something, and saw the teacher and his classmate Susie walking towards him. Susie was carrying a bowl of goldfish. As they came closer, the boy thought that the teacher noticed his wet pants, and suddenly Susie trips and drops the fishbowl in his lap. While thanking God for helping him, he pretends to get angry with Susie and yells at her. Everyone in the class thinks it is Susie’s fault that the boy’s pants got wet. The teacher helps the boy change into dry clothes, and the class continues. Later that evening, the boy asks Susie, “You did that on purpose, didn’t you?” “I wet my pants once too”, whispers Susie.""",

    'prompts': """*|*|*|*|Verb Ending in -ing|*|*|Noun|*|*|*|*|*|Plural Noun|*|*|*|*|*|*|Noun|*|*|*|*|Body Part|*|Past Tense Verb|*|*|*|*|*|*|*|*|Plural Noun|*|*|*|*|*|*|*|*|*|Adverb|Past Tense Verb|*|*|*|*|Past Tense Verb|*|Profession|*|*|Noun|Susie|Verb Ending in -ing|*|*|*|*|Verb Ending in -ing|*|Noun|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Profession|Past Tense Verb|*|Adjective|*|*|Adverb|Susie|Verb Ending in -s|*|Verb Ending in -s|*|Noun|*|*|*|*|Verb Ending in -ing|*|*|Verbing Ending in -ing|*|*|Verb Ending in -s|*|*|*|*|Susie|*|Verb Ending in -s|*|*|*|*|*|Noun|Verb Ending in -s|*|*|*|*|*|*|*|Plural Noun|*|*|*|Profession|Verb Ending in -s|*|*|Verb|*|Adjective|*|*|*|Noun|*|*|*|*|*|*|Verb Ending in -s|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|Plural Noun|*|*|Verb Ending in -s|*"""
}


def split_story(dict):
    return dict['story'].split(' ')


def join_prompts(arr):
    return '|'.join(arr)


def split_prompts(dict):
    return dict['prompts'].split('|')


def create_random_prompts(prompts_array):
    tuples = []
    for word in range(len(prompts_array) // 10):
        rand = randint(0, len(prompts_array)-1)
        while prompts_array[rand] == '*':
            rand = randint(0, len(prompts_array)-1)
        else:
            tuples.append((rand, prompts_array[rand]))

    return tuples


def replace_words(story_array, tuples_array):
    for tuple in tuples_array:
        story_array[tuple[0]] = tuple[1]
    return story_array


def join_story(arr):
    return ' '.join(arr)


def whole_process(dict):
    story_array = split_story(dict)
    prompts_array = split_prompts(dict)
    tuples_array = create_random_prompts(prompts_array)
    replaced_array = replace_words(story_array, tuples_array)
    return join_story(replaced_array)


print(whole_process(story_one))
