print('Hello, world!')
name = input('What is your name?\n')
print('Hi, %s.' % name)
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print('iteration {iteration} is{name}'.format(iteration=i, name=name))