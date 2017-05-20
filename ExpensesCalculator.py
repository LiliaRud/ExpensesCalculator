expenses = []

div = 65 * '_'
row = '|%15s|%15s|%15s|%15s|'
def print_results(id='Id', cat='Category', sum='Summ', dates= 'Date'):
    print(row % (id, cat, sum, dates))
    print(div)

def set_id():
    iden = 1
    for expense in expenses:
        if len(expenses) + 1 == expense['id']:
            iden = expenses[len(expenses) - 1]['id'] + 1
        else:
            iden = len(expenses) + 1
    return iden
#=================================================================
def add():
    print(div)
    while True:
        element = { 'id': set_id(), }
        category = input('Enter category: ')
        element['category'] = category
        sum = input('Enter summ: ')
        for s in sum:
            if 58 > ord(s) > 47:
                element['sum'] = float(sum)
            else:
                print('Please, enter a number!')
                return False
        exp_date = input('Enter date (yyyy/mm/dd): ')
        if len(exp_date) == 10:
            if exp_date[4] == '/' and exp_date[7] == '/':
                element['date'] = exp_date
            else:
                print('Please, enter the date in format yyyy/mm/dd!')
                return False
        else:
            print('Please, enter the date in format yyyy/mm/dd!')
            return False
        print('Id of note:', element['id'])
        print('Do you want add something else?')
        action = input('Print \'Y\' or \'N\': ')
        print(div)
        expenses[len(expenses):] = [element]
        if action.upper() == 'N':
            break
        elif action.upper() == 'Y':
            continue
        else:
            print('You make some mistake')
            break
#=================================================================
def remove():
    print(div)
    rem_id = input('Enter the Id which will be deleted: ')
    for expense in expenses:
        if expense['id'] == int(rem_id):
            expenses.remove(expense)
            print('Note was removed')
    print(div)
#=================================================================
def show():
    print(div)
    show_by = input('''Choose the instruction:
    1 - Show all;
    2 - Show by category;
    3 - Show by date;
    4 - Show by amount ascending;
    5 - Show by amount descendingly: ''')
    if show_by ==  '1':
        print_results()
        for expense in expenses:
            print_results(expense['id'], expense['category'], expense['sum'], expense['date'])
    elif show_by == '2':
        choosing = input('Choose category: ')
        print_results()
        for expense in expenses:
            if choosing == expense['category']:
                print_results(expense['id'], expense['category'], expense['sum'], expense['date'])
    elif show_by == '3':
        choosing_date = input('''Choose the instruction:
        1 - Show per year;
        2 - Show per month;
        3 - Show per day: ''')
        if choosing_date == '1':
            year = input('Enter the year: ')
            print_results()
            for expense in expenses:
                if expense['date'][:4] == year:
                    print_results(expense['id'], expense['category'], expense['sum'], expense['date'])
        elif choosing_date == '2':
            year = input('Enter the year: ')
            month = input('Enter the month: ')
            print_results()
            for expense in expenses:
                if expense['date'][:4] == year and expense['date'][5:7] == month:
                    print_results(expense['id'], expense['category'], expense['sum'], expense['date'])
        elif choosing_date == '3':
            year = input('Enter the year: ')
            month = input('Enter the month: ')
            day = input('Enter the day: ')
            print_results()
            for expense in expenses:
                if expense['date'][:4] == year and expense['date'][5:7] == month and expense['date'][8:] == day:
                    print_results(expense['id'], expense['category'], expense['sum'], expense['date'])
        else:
            print('Incorrect inctruction')
    elif show_by == '4':
         expenses_sorted = sorted(expenses, key=lambda expense: expense['sum'])
         print_results()
         for expense in expenses_sorted:
             print_results(expense['id'], expense['category'], expense['sum'], expense['date'])
    elif show_by == '5':
         expenses_sorted = sorted(expenses, key=lambda expense: expense['sum'], reverse=True)
         print_results()
         for expense in expenses_sorted:
             print_results(expense['id'], expense['category'], expense['sum'], expense['date'])
    else:
        print('Incorrect inctruction')
#=================================================================
functions = {
        'add': add,
        'remove': remove,
        'show': show,
      }
while True:
    print('Available actions:')
    for action in functions:
        print('\t' + action)
    print('For exit type \'q\'')
    action = input('Choose action: ')
    if action.lower() in functions:
        functions[action.lower()]()
    elif action.lower() == 'q':
        break
    else:
        print('Incorrect instruction')