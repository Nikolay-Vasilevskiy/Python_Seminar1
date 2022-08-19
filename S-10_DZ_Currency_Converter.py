# Конвертер валют:
#Приложение для вывода текущего курса валют (валюты выбирайте любые).
#  Постарайтесь сделать конвертер валют (Например, ввел в рублях, получил в $).
#  Было бы классно обернуть все в графический интерфейс.

item_2 = True
item_3 = False

usd_item = "USD"
usd_usd_rate = 1

eur_item = "EUR"
usd_eur_rate = 0.86

uah_item = "UAH"
usd_uah_rate = 26.23

chf_item = "CHF"
usd_chf_rate = 0.91

rub_item = "RUB"
usd_rub_rate = 71.88

byn_item = "BYN"
usd_byn_rate = 2.46
#


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

currency_convertor = item_2

if currency_convertor:
    print("Вас приветствует конвертор валют. Доступные валюты: EUR, UAH, CHF, RUB, BYN.")
    currency_usd = usd_item
while True:
    target_currency = input("Выберите валюту: ")
    if target_currency not in ["EUR", "eur", "UAH", "uah", "CHF", "chf", "RUB", "rub", "BYN", "byn"]:
        print("Валюта не поддерживается. Введете допустимый индекс (EUR, UAH, CHF, RUB, BYN)")
    else:
        target_currency_amount = input("Введите сумму: ")
        currency_result = 0
        if not is_number(target_currency_amount):
            print("Вы ввели не число")
            once_more = input("Хотите продолжить? (Y/N): ")
            if once_more == "Y" or once_more == "y":
                continue
            else:
                print("Спасибо! До свидания!")
                break

        elif float(target_currency_amount) <= 0:
            print("Вы ввели не положительное число")
            once_more = input("Хотите продолжить? (Y/N): ")
            if once_more == "Y" or once_more == "y":
                continue
            else:
                print("Спасибо! До свидания!")
                break

        if float(target_currency_amount) > 0:
            if target_currency == "EUR" or target_currency == "eur":
                currency_result = float(target_currency_amount) / usd_eur_rate
                print(target_currency_amount, eur_item, "=", round(currency_result, 2), usd_item)
                once_more = input("Хотите продолжить? (Y/N): ")
                if once_more == "Y" or once_more == "y":
                    continue
                else:
                    print("Спасибо! До свидания!")
                    break
            elif target_currency == "UAH" or target_currency == "uah":
                currency_result = float(target_currency_amount) / usd_uah_rate
                print(target_currency_amount, uah_item, "=", round(currency_result, 2), usd_item)
                once_more = input("Хотите продолжить? (Y/N): ")
                if once_more == "Y" or once_more == "y":
                    continue
                else:
                    print("Спасибо! До свидания!")
                    break
            elif target_currency == "CHF" or target_currency == "chf":
                currency_result = float(target_currency_amount) / usd_chf_rate
                print(target_currency_amount, chf_item, "=", round(currency_result, 2), usd_item)
                once_more = input("Хотите продолжить? (Y/N): ")
                if once_more == "Y" or once_more == "y":
                    continue
                else:
                    print("Спасибо! До свидания!")
                    break
            elif target_currency == "RUB" or target_currency == "rub":
                currency_result = float(target_currency_amount) / usd_rub_rate
                print(target_currency_amount, rub_item, "=", round(currency_result, 2), usd_item)
                once_more = input("Хотите продолжить? (Y/N): ")
                if once_more == "Y" or once_more == "y":
                    continue
                else:
                    print("Спасибо! До свидания!")
                    break
            elif target_currency == "BYN" or target_currency == "byn":
                currency_result = float(target_currency_amount) / usd_byn_rate
                print(target_currency_amount, byn_item, "=", round(currency_result, 2), usd_item)
                once_more = input("Хотите продолжить? (Y/N): ")
                if once_more == "Y" or once_more == "y":
                    continue
                else:
                    print("Спасибо! До свидания!")
                    break
