def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    if "@" not in sender or "@" not in recipient:
        print(f'Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
        return

    if not sender.endswith(('.com', '.ru', '.net')) or not recipient.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <sender> на адрес <recipient>.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.')

send_email('Это сообщение для проверки контакта', 'vik1478@gmail.com')
send_email('Cделать дз!', 'urban.student@mail.ru', sender='urban.student@mail.ru')
send_email('Еще одно письмо', 'urban@test.com', sender='urban_stuent@uni.net')
send_email('Пожалуйста, отправьте дз', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Вы видите это сообщение как лучший студент мира!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
