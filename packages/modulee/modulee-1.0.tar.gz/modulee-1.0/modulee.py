

def functionn(phrase:str,letters:str='aeiou')->set:
    """Returns a set of the 'letters' found in 'phrase'. """
    return set(letters).intersection(set(phrase))