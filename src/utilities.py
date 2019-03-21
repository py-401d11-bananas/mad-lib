"""
This Module contains functionality to transform stories with user inputs.

Once a story is selected, the string of the content is split, as is it's array of prompts. The indices are used to find the position of a word, match a corresponding part of speech, and provide the part of speech for the user as prompts. Once the user provides responses to prompts, the indices are used to replace the current words with the user inputs.

"""

from .models import PresetStory
from .stories import *
from random import randint


def array_from_story_string(dict):
    """
    Splits the story string into an array of its words.

    Args
        dict: A story that is a dictionary with 'title', 'content', and 'prompts' keywords.

    Returns
        A list of the words of the content of the story.
    """
    story_array = dict['content'].split(' ')
    return story_array


def array_from_prompts_string(dict):
    prompts_array = dict['prompts'].split('|')
    return prompts_array


def string_from_prompts_array(arr):
    """
    Splits the story string into an array of its words.

    Args
        dict: A story that is a dictionary with 'title', 'content', and 'prompts' keywords.

    Returns
        A list of the words of the content of the story.
    """

    prompts_string = '|'.join(arr)
    return prompts_string




def array_of_random_prompt_tuples(prompts_array):
    array_of_tuples = []
    for word in range(len(prompts_array) // 7):
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

if __name__ == "__main__":
    print(array_from_story_string(story_five))
