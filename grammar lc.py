#grammar = ['is','not','am','are','do','did','no','will','never','shall','none','was','nor']
#Given a list grammar, using list comprehension, filter all the negative words that starts with 'n'

grammar = ['is','not','am','are','do','did','no','will','never','shall','none','was','nor']
newgrammar=[x for x in grammar if (x.startswith("n"))]
print(newgrammar)