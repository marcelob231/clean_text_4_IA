
def cleaning(text):

    stopwords = ['A', 'AS', 'O', 'OS', 'NO', 'NOS', 'NA', 'NAS', 'E', 'SE', "RT"]

    ntext = text.split()

    for word in list(ntext):
        if word in stopwords:
            ntext.remove(word)
        if word.startswith('@'):
            ntext.remove(word)
        if word.startswith('.@'):
            ntext.remove(word)
        if word.startswith('#'):
            ntext.remove(word)
        if word.startswith('.#'):
            ntext.remove(word)
        if word.startswith('HTTP'):
            ntext.remove(word)
        if word.startswith('.HTTP'):
            ntext.remove(word)