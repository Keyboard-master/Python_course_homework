# �������:
# ��� ��������� ������ ����� ���������� ��������� ���������, ������������ ������ ����� ����� � ��� ���,
# � ������ ������ ��������� ���������� ���� ��� ������ ��������, ��� �� ����� ��������� ����, ��� ����� ������.
#
# ��� ������ �� ��� ������ �� ������, �� ���, ��� ������� ������ ���������� � ������� ���������� ������ �������.
#
# ���� ������ ��������� ������ ������, � ��������� �������� ������, ������� ������ ������������.
# ����������� ���������, ��� �� ��������� ��� ��������, ���������� ���� ������� ���� ��������� ����� �������� ������!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money == 0:
        person['money'] -= money
        return '�� ����� {} ������.'.format(money)
    else:
        return '�� ����� ����� ������������ �������!'


def process_user_choice(choice, person):
    if choice == '1':
        print(check_account(person))
    elif choice == '2':
        count = float(input('����� � ������:'))
        print(withdraw_money(person, count))


def start():
    card_number, pin_code = input('������� ����� ����� � ��� ��� ����� ������:').split()

    card_number = int(card_number)
    pin_code = int(pin_code)
    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = int(input('�������� �����:\n'
                               '1. ��������� ������\n'
                               '2. ����� ������\n'
                               '3. �����\n'
                               '---------------------\n'
                               '��� �����:'))
            if choice == 3:
                break
            process_user_choice(choice, person)
    else:
        print('����� ����� ��� ��� ��� ������� �� �����!')

start()