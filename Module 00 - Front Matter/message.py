def banner(msg):
    length = len(msg)
    size = length + 4

    header = "*" * size
    caption = ['*', msg, '*']

    print('{:^80}'.format(header))
    print('{:^80}'.format(" ".join(caption)))
    print('{:^80}'.format(header))

msg = input('What is your message? ')
banner(msg)