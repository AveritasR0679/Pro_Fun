MAX_TWEET_LENGTH = 50
HASHTAG_SYMBOL = '#'
MENTION_SYMBOL = '@'
UNDERSCORE = '_'
SPACE = ' '

def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False

    """
    return 1 <= len(text) <= MAX_TWEET_LENGTH

def contains_hashtag(val_tweet: str, word: str) -> bool:
    """Return True if and only if val_tweet contains the hash symbol with
    the tweet word, word, that follows subsequently; return False otherwise.

    >>> contains_hashtag('I like #csc108', 'csc108')
    True
    >>> contains_hashtag('I like #csc108', 'csc')
    False
    """
    return word + SPACE in clean(val_tweet) + SPACE
        
def is_mentioned(val_tweet: str, word: str) -> bool:
    return MENTION_SYMBOL + word + SPACE in clean(val_tweet) + SPACE

def add_mention_exclusive(val_tweet: str, word: str) -> str:
    if is_valid_tweet(val_tweet + SPACE + MENTION_SYMBOL + word) and \
       (MENTION_SYMBOL + word + SPACE) in val_tweet:
        return val_tweet + SPACE + MENTION_SYMBOL + word
    else:
        return val_tweet

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str
