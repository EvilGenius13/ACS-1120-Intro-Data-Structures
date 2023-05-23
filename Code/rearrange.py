import random
import sys

def rearrange_words(*words):
    shuffled_words = list(words)
    random.shuffle(shuffled_words)
    rearranged_words = ' '.join(shuffled_words)
    return rearranged_words

if __name__ == '__main__':
    """
    In the context of the script, args = sys.argv[1:] is used to extract the command-line arguments 
    provided by the user, excluding the script name itself. sys.argv[1:] slices the list sys.argv starting from index 1, 
    effectively removing the script name from the arguments.
    """
    args = sys.argv[1:]
    rearrange = rearrange_words(*args)
    print(rearrange)