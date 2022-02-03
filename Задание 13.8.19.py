ticket = int(input("Введите количество билетов, которые хотите приобрести на мероприятие: "))

cost = 0

for i in range(ticket):
    age = int(input("Введите возраст: "))
    if age < 18:
        cost = cost + 0
    elif 18 <= age < 25:
        cost = cost + 990
    else: cost = cost + 1390
    if ticket > 3:
        cost = cost * 0.9
print("Сумма к оплате: "+ " " + str(round(cost)) + "")
