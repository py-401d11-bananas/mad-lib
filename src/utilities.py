"""
This Module contains functionality to transform stories with user inputs.

Once a story is selected, the string of the content is split, as is it's array of prompts. The indices are used to find the position of a word, match a corresponding part of speech, and provide the part of speech for the user as prompts. Once the user provides responses to prompts, the indices are used to replace the current words with the user inputs.

"""

from .models import PresetStory
from .stories import *
from random import randint


# ========= Used in App ================


def array_from_story_string(str):
    """
    Splits a story string into an array of its words.

    Args
        str: A string of a story.

    Returns
        A list of the words of the content of the story.
    """

    story_array = str.split(' ')
    return story_array


def array_from_prompts_string(str):
    """
    Splits a string of prompts into a list.

    Args
        str: A story that is a dictionary with 'title', 'content', and 'prompts' keywords.

    Returns
        A list of the prompts of the story.
    """

    prompts_array = str.split('|')
    return prompts_array


def string_from_prompts_array(arr):
    """
    Concatinates a list of prompts into a string.

    Used in development to separate prompts with a bar.

    Args
        arr: An array of prompts.

    Returns
        A concatinated string.
    """

    prompts_string = '|'.join(arr)
    return prompts_string


def array_of_random_prompt_tuples(prompts_array):
    """
    Creates a list of pairs of indexes and corresponding prompts.

    Args
        arr: An array of prompts.

    Returns
        A list of tuples.
    """

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
    """
    Creates a list of pairs of indexes and corresponding parts of speech.

    Args
        arr: The array of words of a story.
        arr: An array of tuples of indexes and prompts.

    Returns
        The story converted with the responspes to the prompts.
    """

    for tuple in tuples_array:
        story_array[tuple[0]] = tuple[1]
    return story_array


def string_from_array(arr):
    """
    Concatinates the revised story into a string.

    Args
        arr: An array of words of a revised story.

    Returns
        A string with the new story.
    """

    string = ' '.join(arr)
    return string


def send_prompts_to_form(dict):
    """
    Sends a selection of tuples to the prompts form.

    Args
        dict: A dict that contains the tuples as key:value pairs.

    Returns
        An array of tuples.
    """
    story_array = array_from_story_string(dict['content'])
    prompts_array = array_from_prompts_string(dict['prompts'])
    tuples_array = array_of_random_prompt_tuples(prompts_array)
    return tuples_array


# ========= Used in Development ================


def whole_process(dict):
    """
    Runs the word replacement process in the file.

    Used for development.

    Args
        dict: A dict of the story where the keys of 'title', 'content', and 'prompts' are held as strings.

    Returns
        Story transformed using user responses.
    """

    story_array = array_from_story_string(dict)
    prompts_array = array_from_prompts_string(dict)
    tuples_array = array_of_random_prompt_tuples(prompts_array)
    replaced_array = replace_words(story_array, tuples_array)
    return string_from_array(replaced_array)


def prompt_user_in_terminal(dict):
    """
    Runs the word replacement process in the terminal.

    Used for development.

    Args
        dict: A dict of the story where the keys of 'title', 'content', and 'prompts' are held as strings.

    Returns
        Story transformed using user responses.
    """

    story_array = array_from_story_string(dict)
    prompts_array = array_from_prompts_string(dict)
    tuples_array = array_of_random_prompt_tuples(prompts_array)
    new_tuple_array = []
    for tuple in tuples_array:
        new_tuple_array.append((tuple[0], input(str(tuple[1]) + ': ').upper()))
    replaced_array = replace_words(story_array, new_tuple_array)
    return string_from_array(replaced_array)


def convert_dict_to_model_instance(dict):
    """
    Adds pre-fabricated stories to the PresetStory database.

    Used for development.

    Args
        dict: A dict of the story where the keys of 'title', 'content', and 'prompts' are held as strings.

    Returns
        A new item in the PresetStory database.
    """

    story = PresetStory(
        title=dict['title'],
        content=dict['content'],
        prompts=dict['prompts']
    )
    return story


if __name__ == "__main__":
    print(array_from_story_string(story_five))
