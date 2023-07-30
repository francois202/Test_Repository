n = int(input("Введите общее кол-во билетов для покупки:"))

list_total = []
for i in range(n):
    age = int(input("Введите возраст гостя:"))
    if age < 18:
        list_total.append(0)
    if 18 <= age < 25:
        list_total.append(990)
    if age >= 25:
        list_total.append(1390)
        
if n > 3:
    sum_list = sum(list_total) * 0.9
else:
    sum_list = sum(list_total)

print("Итоговая стоимость купленных билетов:", sum_list)