salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
general_deficit = 0

for month in range(months):
    if month > 0:
        spend *= (1 + increase)

    shortfall = spend - salary
    if shortfall > 0:
        general_deficit += shortfall

whole_money = round(general_deficit)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", whole_money)
