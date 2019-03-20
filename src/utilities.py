from random import randint
from .stories import *
from .models import PresetStory


def array_from_story_string(dict):
    story_array = dict['content'].split(' ')
    return story_array


def string_from_prompts_array(arr):
    prompts_string = '|'.join(arr)
    return prompts_string


def array_from_prompts_string(dict):
    prompts_array = dict['prompts'].split('|')
    return prompts_array


def array_of_random_prompt_tuples(prompts_array):
    array_of_tuples = []
    for word in range(len(prompts_array) // 20):
        rand = randint(0, len(prompts_array)-1)
        while prompts_array[rand] == '*':
            rand = randint(0, len(prompts_array)-1)
        else:
            array_of_tuples.append((rand, prompts_array[rand]))

    return array_of_tuples


def replace_words(story_array, tuples_array):
    for tuple in tuples_array:
        story_array[tuple[0]] = tuple[1]
    return story_array


def string_from_array(arr):
    string = ' '.join(arr)
    return string


def whole_process(dict):
    story_array = array_from_story_string(dict)
    prompts_array = array_from_prompts_string(dict)
    tuples_array = array_of_random_prompt_tuples(prompts_array)
    replaced_array = replace_words(story_array, tuples_array)
    return string_from_array(replaced_array)


def prompt_user_in_terminal(dict):
    story_array = array_from_story_string(dict)
    prompts_array = array_from_prompts_string(dict)
    tuples_array = array_of_random_prompt_tuples(prompts_array)
    new_tuple_array = []
    for tuple in tuples_array:
        new_tuple_array.append((tuple[0], input(str(tuple[1]) + ': ').upper()))
    replaced_array = replace_words(story_array, new_tuple_array)
    return string_from_array(replaced_array)


def send_prompts_to_form(dict):
    story_array = array_from_story_string(dict)
    prompts_array = array_from_prompts_string(dict)
    tuples_array = array_of_random_prompt_tuples(prompts_array)
    return tuples_array


def convert_dict_to_model_instance(dict):
    story = PresetStory(
        title=dict['title'],
        content=dict['content'],
        prompts=dict['prompts']
    )
    return story

if __name__ == "__main__":
    print(array_from_story_string(story_four))

    arr = ['*', 'Animal', '*', '*', 'Plural Animal', 'Past Tense Verb', '*', '*', '*', '*', '*', '*', '*', '*', 'The', 'mother', 'dog', 'told', 'the', 'pups,', 'do', 'not', 'go', 'near', 'the', 'well', 'or', 'play', 'around', 'it.', 'One', 'of', 'the', 'pups', 'wondered', 'why', 'they', 'shouldn’t', 'go', 'to', 'the', 'well', 'and', 'decided', 'to', 'explore', 'it.', 'He', 'went', 'to', 'the', 'well.', 'Climbed', 'up', 'the', 'wall', 'and', 'peeked', 'inside.', 'In', 'there,', 'he', 'saw', 'his', 'reflection', 'and', 'thought', 'it', 'was', 'another', 'dog.', 'The', 'pup', 'saw', 'that', 'the', 'other', 'dog', 'in', 'the', 'well', '(his', 'reflection)', 'was', 'doing', 'whatever', 'he', 'was', 'doing,', 'and', 'got', 'angry', 'for', 'imitating', 'him.', 'He', 'decided', 'to', 'fight', 'with', 'the', 'dog', 'and', 'jumped', 'into', 'the', 'well,', 'only', 'to', 'find', 'no', 'dog', 'there.', 'He', 'barked', 'and', 'barked', 'and', 'swam', 'until', 'the', 'farmer', 'came', 'and', 'rescued', 'him.', 'The', 'pup', 'had', 'learned', 'his', 'lesson.']