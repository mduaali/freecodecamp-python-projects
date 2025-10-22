def add_expense(expenses, amount, category):
    # add a new expense dictionary to the list
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    # loop through all expenses and print them
    for expense in expenses:
        print(f'amount: {expense["amount"]}, category: {expense["category"]}')
    
def total_expenses(expenses):
    # calculate total amount spent using a lambda and sum
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    # filter expenses by a specific category using a lambda
    return list(filter(lambda expense: expense['category'] == category, expenses))
    

def main():
    expenses = []
    
    while True:
        # display menu options
        print('\nexpense tracker')
        print('1. add an expense')
        print('2. list all expenses')
        print('3. show total expenses')
        print('4. filter expenses by category')
        print('5. exit')
       
        choice = input('enter your choice: ')

        if choice == '1':
            # add a new expense
            amount = float(input('enter amount: '))
            category = input('enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # print all expenses
            print('\nall expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            # print total expenses
            print('\ntotal expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            # filter expenses by category
            category = input('enter category to filter: ')
            print(f'\nexpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            # exit the program
            print('exiting the program.')
            break

main()
