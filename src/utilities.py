from random import randint, shuffle
from .stories import *
from .models import PresetStory


def array_from_story_string(str):
    story_array = str.split(' ')
    return story_array


def string_from_prompts_array(arr):
    prompts_string = '|'.join(arr)
    return prompts_string


def array_from_prompts_string(str):
    prompts_array = str.split('|')
    return prompts_array


def array_of_random_prompt_tuples(prompts_array):

    available_indices = []

    for i in range(len(prompts_array)):
        if prompts_array[i] != '*':
            available_indices.append(i)

    shuffle(available_indices)

    array_of_tuples = []

    for i in range(len(prompts_array) // 7):
        rand = available_indices[i]
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
    story_array = array_from_story_string(dict['content'])
    prompts_array = array_from_prompts_string(dict['prompts'])
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
    print(array_from_story_string(story_five))
