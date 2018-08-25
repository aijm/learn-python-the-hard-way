def scan(sentence):
    """
    split sentence into words, and search words in the
    existing lexicon.
    arguments: sentence of string
    return:  a list of tuple [(type1, word1),(type2, word2),...]
    """

    lexicon = {
        'north': 'direction',
        'south': 'direction',
        'east': 'direction',
        'west': 'direction',
        'down': 'direction',
        'up': 'direction',
        'left': 'direction',
        'right': 'direction',
        'back': 'direction',
        'go': 'verb',
        'stop': 'verb',
        'kill': 'verb',
        'eat': 'verb',
        'the': 'stop',
        'in': 'stop',
        'of': 'stop',
        'from': 'stop',
        'at': 'stop',
        'it': 'stop',
        'door': 'noun',
        'bear': 'noun',
        'princess': 'noun',
        'cabinet': 'noun'
    }

    result = []

    words = sentence.split()
    for word in words:
        # use str.lower() to handle capitalization
        type = lexicon.get(word.lower())
        # if word is in lexicon, then get the type
        if type is not None:
            result.append((type, word))
        else:
            try:
                # if word in a number, then use token number
                number = int(word)
                result.append(('number', number))
            except ValueError:
                # nosense word use token error
                result.append(('error', word))

    return result



