__author__ = 'ankurgupta'

from mention_extraction import extract_mentions
from checks.used_checks import string_match
from checks.used_checks import pronoun_match


def match(mention, candidate, distance, coref_list):
    if string_match(mention, candidate):
        coref_list.append((mention, candidate))
        return True
    if pronoun_match(mention, candidate, distance):
        coref_list.append((mention, candidate))
        return True
    return False

def get_data(input_file):
    fh = open(input_file, 'rt')

    line = fh.readline()
    data = []
    while line:
        data.append(line)
        line = fh.readline()

    return data


def coreference_resolution():
    coref_list = []
    # data = get_data('input.txt')
    mentions = extract_mentions()

    for i in range(len(mentions)):
        j = i - 1
        while j >= 0:
            if match(mentions[i], mentions[j], i - j, coref_list):
                break
            j -= 1

    print "\nCo-references"
    for coref in coref_list:
        print coref

# print 'Running coreference resolution\n\n'
coreference_resolution()
