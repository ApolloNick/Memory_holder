def join_var_into_dict(x, y):
    united_dictionary = dict(zip(x, y))
    return united_dictionary


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
print(join_var_into_dict(coin, code))
