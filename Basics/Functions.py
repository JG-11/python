
def calculate_btc_to_mxn(amount):
    btc_price = 249930.94

    result = amount * btc_price

    return result


if __name__ == '__main__':
    amount = float(input('Type the amount of Bitcoins: '))

    result = calculate_btc_to_mxn(amount)

    print('{} BTC to MXN = ${} Mexican pesos'.format(amount, result))