expenses = []
def set_id ():
    iden = 1
    for expense in expenses:
        if len(expenses) + 1 == expense['id']:
            iden = expenses[len(expenses) - 1]['id'] + 1
        else:
            iden = len(expenses) + 1
    return iden
#=================================================================
def add ():
    while True:
        category = input('Enter category: ')
        sum = input('Enter summ: ')
        exp_date = input('Enter date (yyyy/mm/dd): ')
        expenses[len(expenses):] = [{
            'category': category,
            'sum': sum,
            'date': exp_date,
            'id': set_id(),
        }]
        print('Id of note:', expenses[len(expenses) - 1]['id'])
        print('Do you want add something else?')
        action = input('Print \'Y\' or \'N\': ')
        if action.upper() == 'N':
            break
        elif action.upper() == 'Y':
            continue
        else:
            print('You make some mistake')
            break
#=================================================================
def remove ():
    while True:
        print('For exit type \'q\'')
        action = input('Enter the Id: ')
        if action == 'q':
            break
        else:
            rem_id = int(action)
            for expense in expenses:
                if expense['id'] == rem_id:
                    del expenses[rem_id - 1]
                    print('Note was removed')
                else:
                    print('Incorrect id')
#=================================================================
def show ():
    show_by = input('Show: ')
    row = '|%10s|%10s|%10s|%10s|'
    div = 45 * '_'
    if show_by == 'all':
        print(row % ('Id', 'Category', 'Summ', 'Date'))
        print(div)
        for expense in expenses:
            print(row % (expense['id'], expense['category'], expense['sum'], expense['date']))
            print(div)
    elif show_by == 'category':
        choosing = input('Choose category: ')
        print(row % ('Id', 'Category', 'Summ', 'Date'))
        print(div)
        for expense in expenses:
            if choosing == expense['category']:
                print(row % (expense['id'], expense['category'], expense['sum'], expense['date']))
                print(div)
    elif show_by == 'date':
        choosing = input('Choose date: ')
        print(row % ('Id', 'Category', 'Summ', 'Date'))
        print(div)
        for expense in expenses:
            if choosing == expense['date']:
                print(row % (expense['id'], expense['category'], expense['sum'], expense['date']))
                print(div)
    #!!!!!!!MAKE SORTING!!!!!!!!!
    # elif  show_by == 'asc':
    #     for expense in expenses:

#=================================================================
functions = {
        'add': add,
        'remove': remove,
        'show': show,
      }
#=================================================================
while True:
    print('Available actions:')
    for action in functions:
        print('\t' + action)
    print('For exit type \'q\'')
    action = input('Choose action: ')
    if action in functions:
        functions[action]()
    elif action == 'q':
        break
    else:
        print('Incorrect instruction')
#=================================================================