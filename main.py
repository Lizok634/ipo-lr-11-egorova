
# transport_company_app.py
from transport import *


def create_company(company_name):
    company = TransportCompany(company_name)
    return company


def display_menu():
    print("\nМеню:")
    print("1. Добавить клиента")
    print("2. Добавить транспортное средство")
    print("3. Вывести список клиентов")
    print("4. Вывести список транспортных средств")
    print("5. Оптимизировать распределение грузов")
    print("6. Выход\n")


def get_transport_type():
    print("\nДоступный транспорт: самолет, грузовик")
    transport_type = input("\nВыберите вид транспорта: ").strip()

    if not transport_type.isalpha():
        print("\n_______________________Ошибка_______________________")
        print(f"\n{transport_type} --- некорректное значение, повторите ввод.")
        return get_transport_type()

    transport_type = transport_type.lower()

    if transport_type not in ["самолет", "грузовик"]:
        print("\n_______________________Ошибка_______________________")
        print(f"{transport_type} транспорт не найден, повторите ввод.")
        return get_transport_type()

    return transport_type


def show_client_details(client):
    if client.is_vip:
        print("\n_______VIP_______Client________")
        print(f"""\nИмя клиента: {client.name}
              \nВес груза: {client.cargo_weight}""")
        print("________________________________")

    else:
        print(f"""\nИмя клиента: {client.name}
              \nВес груза: {client.cargo_weight}""")


def show_vehicle_details(vehicle):
    if isinstance(vehicle, Airplane):
        print("\n_____________Самолет_____________")
    else:
        print("\n_____________Грузовик_____________")

    print(vehicle.__str__())
    print(f"\nСписок клиентов чьи грузы загружены:")
    if vehicle.current_load == 0:
        print("""_____________________________
              \nНа транспорт не загружен груз
              \nВыполните 5 пункт меню для загрузки
              \n_____________________________""")
    else:
        print("_____________________________")
        for client in vehicle.clients_list:
            show_client_details(client)
            print("\n_____________________________")


def display_end_stats(total_ops, operations_list, operations_count):
    print(f"""
        Программа завершена.
       """)
    op_count = 1
    print("\nКоличество выполненных операций: ")
    for op_name in operations_list:
        print(f"""
            {op_name} : {operations_count[op_count]}
           """)
        op_count += 1
    return None


def validate_client_name(client_name):
    while not client_name:
        print("___________________________________________")
        print("Ошибка введения имени клиента.")
        print("\nИмя не должно быть пустой строкой")
        print("___________________________________________")
        client_name = input("\nВведите имя клиента: ").strip()
    return client_name


def validate_cargo_weight(cargo_weight_input):
    while True:
        try:
            cargo_weight_input = float(cargo_weight_input)
            if cargo_weight_input <= 0:
                print("___________________________________________")
                print("Ошибка введения веса груза клиента.")
                print(
                    "\nВес груза должен быть положительным числом.\nВведите вес груза корректно.")
                print("___________________________________________")
                cargo_weight_input = input("\nВведите вес груза: ").strip()

            else:
                break

        except ValueError:
            print("___________________________________________")
            print("Ошибка введения веса груза клиента.")
            print("\nНекорректный формат веса груза. Введите число.")
            print("___________________________________________")
            cargo_weight_input = input("\nВведите вес груза: ").strip()
    return cargo_weight_input


def validate_vip_status(vip_status_input):
    while True:
        try:
            vip_status_input = vip_status_input.lower()

            if vip_status_input == "да":
                vip_status_input = True
                break
            elif vip_status_input == "нет":
                vip_status_input = False
                break
            else:
                print("______________________________________")
                print("Ошибка введения вип-статуса клиента.")
                print(f"Некорректное значение {vip_status_input}!")
                print(
                    "\n Решения: \n 1. Введите 'да' если клиент имеет статус VIP\n 2. Введите нет или пропустите пункт в ином случае")
                print("______________________________________")
                vip_status_input = input(
                    "\nЯвляется  vip-клиентом? (да / нет): ").strip()

        except:
            print("______________________________________")
            print("Ошибка введения вип-статуса клиента.")
            print(f"Некорректное значение {vip_status_input}!")
            print(
                "\n Решения: \n 1. Введите 'да' если клиент имеет статус VIP\n 2. Введите нет или пропустите пункт в ином случае")
            print("______________________________________")
            vip_status_input = input(
                "\nЯвляется  vip-клиентом? (да / нет): ").strip()
    return vip_status_input


def validate_vehicle_capacity(capacity_input):
    while True:
        if not capacity_input:
            print("""\n__________________Ошибка__________________
                  \nЗначение грузоподъемности не должно быть пустым.
                  \nЗначение должно быть числом.
                  \nПовторите ввод корректно.\n""")
            capacity_input = input(
                "Введите грузоподъемность(в тоннах): ").strip()
        try:
            capacity_input = float(capacity_input)
            if capacity_input > 0:
                break
            else:
                print("\n__________________________________________________")
                print(
                    "Грузоподъемность должна быть положительным числом.\nПовторите ввод корректно.")
                capacity_input = input(
                    "\nВведите грузоподъемность(в тоннах): ").strip()
        except:
            print("______________________________________")
            print("\nПроизошла ошибка типа данных.\nПовторите ввод корректно.")
            capacity_input = input(
                "\nВведите грузоподъемность(в тоннах): ").strip()
    return capacity_input


def validate_max_altitude(altitude_input):
    while True:
        try:
            altitude_input = float(altitude_input)
            if (altitude_input) <= 0:
                print("""Максимальная высота полета должен быть положительным числом.\n
                Повторите ввод корректно.""")
                altitude_input = input(
                    "Максимальная высота полета(в метрах): ").strip()
            else:
                break
        except:
            print(
                "\n__________________ Ошибка введения данных высоты __________________ ")
            print("""Максимальная высота полета должен быть положительным числом.\n
                Повторите ввод корректно.""")
            print(
                "____________________________________________________________________")
            altitude_input = input(
                "\nМаксимальная высота полета(в метрах): ").strip()
    return altitude_input


def validate_refrigerator_availability(refrigerator_input):
    while True:
        try:
            refrigerator_input = refrigerator_input.lower()
            if refrigerator_input == "да":
                refrigerator_input = True
                break
            elif refrigerator_input == "нет":
                refrigerator_input = False
                break
            else:
                print("\n_________________Ошибка__________________")
                print(
                    """Ответ должен быть 'да' либо 'нет'.\nПовторите ввод корректно.\n""")
                refrigerator_input = input(
                    "Есть ли в наличии холодильник (да / нет): ").strip()
        except:
            print("_________________Ошибка__________________")
            print(
                """Ответ должен быть 'да' либо 'нет'.\nПовторите ввод корректно.\n""")
            refrigerator_input = input(
                "Есть ли в наличии холодильник (да / нет): ").strip()
    return refrigerator_input


total_operations = 0
operation_list = [
    "Добавить клиента",
    "Добавить транспортное средство",
    "Вывести список клиентов",
    "Вывести список транспортных средств",
    "Оптимизировать распределение грузов",
    "Выход"
]

# Словарь для подсчета количества каждой операции.
operation_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

company_name = input("Введите название компании: ").strip()
company = create_company(company_name)
print("Компания успешно добавлена")

while True:
    display_menu()
    # Получение номера действия от пользователя.
    choice = input("\nВведите номер пункта: ")
    try:
        choice = int(choice)
    except:
        print("""\n_______________Ошибка________________
              \nПровторите ввод корректно (введите число)\n""")
        choice = input("\nВведите номер пункта: ")

    if choice == 1:
        total_operations += 1
        operation_count[1] += 1

        client_name = validate_client_name(
            input("\nВведите имя клиента: ").strip())
        cargo_weight = validate_cargo_weight(
            input("Введите вес груза: ").strip())
        vip_status = input(
            "Является  vip-клиентом? (да / нет): ").strip()

        if not vip_status:
            company.add_client(
                Client(client_name, cargo_weight))
        else:
            vip_status = validate_vip_status(vip_status)
            company.add_client(
                Client(client_name, cargo_weight, vip_status))

        print("Запись клиента успешно добавлена!")

    elif choice == 2:
        total_operations += 1
        operation_count[2] += 1
        transport_type = get_transport_type()

        if transport_type == "самолет":
            altitude = validate_max_altitude(input(
                "Максимальная высота полета(в метрах): ").strip())
            company.add_vehicle(Airplane(altitude))

        else:
            refrigerator = validate_refrigerator_availability(input(
                "Есть ли в наличии холодильник (да / нет): ").strip())
            company.add_vehicle(Van(refrigerator))

        vehicle_capacity = validate_vehicle_capacity(input(
            "Введите грузоподъемность(в тоннах): ").strip())

        company.vehicles[-1].capacity = vehicle_capacity
        print("Транспорт успешно добавлен.")

    elif choice == 3:
        total_operations += 1
        operation_count[3] += 1
        if len(company.clients) == 0:
            print(f"""У компании {
                  company_name} пока что нет клиентов :( Станьте первым!""")
        else:
            client_counter = 1
            print(f"\nКлиенты компании {company_name}: ")

            for client in company.clients:
                print(
                    f"\n------------------{client_counter} клиент------------------")
                show_client_details(client)
                client_counter += 1
            print("\n--------------------------------------------")

    elif choice == 4:
        total_operations += 1
        operation_count[4] += 1
        if len(company.vehicles) == 0:
            print(
                f"\nКомпания {company_name} не имеет траспорта :(\nДобавьте транспорт.")
        else:
            for vehicle in company.vehicles:
                show_vehicle_details(vehicle)

    elif choice == 5:
        total_operations += 1
        operation_count[5] += 1
        if len(company.vehicles) == 0:
            print("\nПожалуйста добавьте транспорт.\nСписок транспорта пуст")
        elif len(company.clients) == 0:
            print("\nПожалуйста, добавьте клиентов.\nСписок клиентов пуст")
        else:
            company.optimize_cargo_distribution()
            print("Оптимизация прошла успешно.")

    elif choice == 6:
        # Увеличение счетчика.
        operation_count[6] += 1
        # Вывод статистики и завершение программы.
        display_end_stats(total_operations, operation_list, operation_count)
        break

    else:
        print("Неизвестное значение пункта, повторите ввод.")
