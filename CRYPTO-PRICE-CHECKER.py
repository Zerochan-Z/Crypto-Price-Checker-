coin_prices = {
    "bitcoin": 64500.50,
    "ethereum": 3200.75,
    "binance coin": 580.20,
    "solana": 145.85,
    "cardano": 0.45
}

print('Coin\'s list: ' + ','.join([coin.title() for coin in coin_prices.keys()]))
print('-'*80)

while True:
    add_coins = input('Any coins wanna add? (Yes/No) ').lower()
    if add_coins in ['yes','y']:
        new_coins = input('Enter the name of coin: ').lower()
        new_prices = float(input('Enter the price of coin: '))
        coin_prices[new_coins] = new_prices
        print(f'Added "{new_coins.title()}" to your list.')

    elif add_coins in ['no','n']:
        print('Nothing is added.')
        break

    else:
        add_coins = input('Yes/No').lower()

while True:
    print('-'*80)
    question=input('What coin\'s details do you wanna know? \nEnter the name: \nJust type "None" if you have no question to ask\n').lower()
    if question in coin_prices:
        print(f'The prices of {question.title()} is ${coin_prices[question]:,.2f}')

    elif question in ['none','no','quit','exit','end']:
        print('\n\nThanks for using this price-checker. \n\n\n╰(*°▽°*)╯')
        break
    else:
        print(f'Sorry this {question.title()} is not in our database.')
