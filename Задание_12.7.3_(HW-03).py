per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму вклада под проценты:'))

deposit = [money * item * 0.01 for item in per_cent.values()]

print(deposit)

print('Максимальная сумма, которую вы можете заработать —', max(deposit))