def send_email(msg, rcp, sender="university.help@gmail.com"):
    at_pos = rcp.find("@")
    right_domens = (
        (rcp.endswith(".com") or rcp.endswith(".ru") or rcp.endswith(".net")) 
        and
        (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net"))
        
        )
    
    if at_pos == -1 or at_pos == 0 or not(right_domens):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {rcp}") 
        return
    
    if rcp == sender:
        print( "Нельзя отправить письмо самому себе!")
        return
    
    if sender != "university.help@gmail.com":
        print( f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {rcp}.")
        return
    
    print(f"Письмо успешно отправлено с адреса {sender} на адрес {rcp}.")
    



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')