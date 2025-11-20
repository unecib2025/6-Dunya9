#1
users = ['admin', 'operator']
new_user = input("Введите имя нового пользователя: ")  # mike
users.append(new_user)
print(users)
#2
users = ['root', 'security']
admin = input("Введите имя администратора: ")  # superuser
users.insert(0, admin)
print(users)
#3
users = ['alice', 'bob', 'charlie']
to_remove = input("Введите имя пользователя для удаления: ")  # alice
users.remove(to_remove)
print(users)
#4
logs = ['Access granted', 'Login failed', 'Connection lost']
last = logs.pop()
print("Последняя запись:", last)
print("Оставшиеся логи:", logs)
Последняя запись: Connection lost
Оставшиеся логи: ['Access granted', 'Login failed']
#5
attempts = ['ok', 'error', 'ok', 'error', 'error']
errors = attempts.count('error')
print("Количество ошибок входа:", errors)
#6
logs = ['Access ok', 'Breach detected', 'System reboot', 'Breach detected']
index = logs.index('Breach detected')
print("Первое обнаружение вторжения на позиции:", index)
#7
threats = [3, 1, 2, 3, 1, 2]
threats.sort()
print(threats)
#8
reports = ['2025-10-01', '2025-10-02', '2025-10-03']
reports.reverse()
print(reports)
#9
logs = ["alert", "spam", "login", "error", "spam", "alert"]

# Удаляем все 'spam'
while "spam" in logs:
    logs.remove("spam")

# Добавляем 'END_LOG' в конец
logs.append("END_LOG")

# Разворачиваем список
logs.reverse()

# Считаем количество 'alert'
alerts = logs.count("alert")

print("Журнал после очистки:", logs)
print("Количество 'alert':", alerts)
Журнал после очистки: ['END_LOG', 'alert', 'error', 'login', 'alert']
Количество 'alert': 2
#10
whitelist = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5']

to_remove = input("Введите IP для удаления: ")  # 192.168.0.2
new_ip = input("Введите новый IP: ")            # 192.168.0.10

whitelist.remove(to_remove)
whitelist.insert(2, new_ip)
whitelist.sort()

print("Обновлённый белый список:", whitelist)
print("Индекс нового IP:", whitelist.index(new_ip))
Обновлённый белый список: ['192.168.0.1', '192.168.0.3', '192.168.0.10', '192.168.0.4', '192.168.0.5']
Индекс нового IP: 2
#11
attempts = ['ok', 'fail', 'fail', 'ok', 'fail']

# Считаем количество неудачных входов
fails = attempts.count('fail')

# Удаляем все 'fail'
while 'fail' in attempts:
    attempts.remove('fail')

# Добавляем 'audit_completed'
attempts.append('audit_completed')

# Разворачиваем
attempts.reverse()

# Находим индекс первого 'ok'
index_ok = attempts.index('ok')

print("Количество неудачных входов:", fails)
print("Итоговый список:", attempts)
print("Первый индекс 'ok':", index_ok)
Количество неудачных входов: 3
Итоговый список: ['audit_completed', 'ok', 'ok']
Первый индекс 'ok': 1