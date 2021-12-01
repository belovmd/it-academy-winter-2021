parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')