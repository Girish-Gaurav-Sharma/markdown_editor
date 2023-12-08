formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]

msg_1 = '''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done'''
msg_2 = '''Unknown formatting type or command'''
msg_3 = '''The number of rows should be greater than zero'''
text = ''


def header_1_():
    global text
    while True:
        level = input('Level: ')
        if level in ['1', '2', '3', '4', '5', '6']:
            level = int(level)
            break
        else:
            print('The level should be within the range of 1 to 6')
    txt = input('Text: ')
    text = text + '\n' + "#" * level + ' ' + txt + '\n'

    print(f'{text}')
    return True


def header_2_():
    global text
    while True:
        level = input('Level: ')
        if level in ['1', '2', '3', '4', '5', '6']:
            level = int(level)
            break
        else:
            print('The level should be within the range of 1 to 6')
    txt = input('Text: ')
    text = "#" * level + ' ' + txt + '\n'

    print(f'{text}')
    return True


def bold_():
    global text
    txt = input('Text: ')
    text = text + '**' + txt + '**'
    print(f'{text}')
    return True


def itallic_():
    global text
    txt = input('Text: ')
    text = text + '*' + txt + '*'
    print(f'{text}')
    return True


def plain_():
    global text
    txt = input('Text: ')
    text = txt
    print(f'{text}')
    return True


def code_():
    global text
    txt = input('Text: ')
    # text = text[:-1]
    text = text + '`' + txt + '`'
    print(f'{text}')
    return True


def link_():
    global text
    txt_1 = input('Label: ')
    txt_2 = input('URL: ')
    # text = text[:-1]
    text = text + '[' + txt_1 + ']' + '(' + txt_2 + ')'
    print(f'{text}')
    return True


def new_():
    global text
    text = text + '\n'
    print(f'{text}')
    return True


def listt_():
    global text
    while True:
        rows = input('Number of rows: ')
        if int(rows) > 0:
            rows = int(rows)
            break
        else:
            print(msg_3)
            continue
    store = []
    for i in range(1, rows + 1):
        el = input(f'Row #{i}: ')
        store.append(el)

    if choice == "ordered-list":
        store = list(map(lambda x: str(store.index(x) + 1) + '.' + " " + x, store))
        txt = '\n'.join(store)
        text = text + txt + '\n'
        print(f'{text}')
    elif choice == "unordered-list":
        store = list(map(lambda x: '-' + " " + x, store))
        txt = '\n'.join(store)
        text = text + txt + '\n'
        print(f'{text}')


if __name__ == '__main__':
    while True:
        choice = input("Choose a formatter: ")
        if choice in formatters:
            if choice == 'header':
                if text == '':
                    header_2_()
                    continue
                else:
                    header_1_()
                    continue
            elif choice == 'bold':
                bold_()
                continue
            elif choice == 'plain':
                plain_()
                continue
            elif choice == 'inline-code':
                code_()
                continue
            elif choice == 'new-line':
                new_()
                continue
            elif choice == 'link':
                link_()
                continue
            elif choice == 'italic':
                itallic_()
                continue
            elif choice in ["ordered-list", "unordered-list"]:
                listt_()
                continue

        elif choice == '!help':
            print(msg_1)

        elif choice == '!done':
            with open('output.md', 'w') as f:
                f.write(text)
            break

        elif choice not in formatters:
            print(msg_2)






