#Given a list lib, using list comprehension store all the books that was published after 2010
#library = [('book1',2002),('book2',2012),('book3',2007),('book4',2015),('book5',2005),('book6',2018)]

library = [('book1',2002),('book2',2012),('book3',2007),('book4',2015),('book5',2005),('book6',2018)]
books=[(book,year) for book,year in library if year>2010]
print(books)