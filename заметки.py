# Функция для создания новой заметки
def create_note():
    # Запросить у пользователя заголовок и текст заметки
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    # Сгенерировать уникальный ID для заметки
    note_id = len(notes) + 1
    # Создать словарь с данными заметки
    note = {"id": note_id, "title": title, "text": text}
    # Добавить заметку в список заметок
    notes.append(note)
    print(f"Заметка с ID {note_id} создана")
    
    
# Функция для вывода списка всех заметок
def list_notes():
    # Если список заметок пуст, вывести сообщение об этом
    if not notes:
        print("Список заметок пуст")
    else:
        # Вывести заголовок и ID каждой заметки
        for note in notes:
            print(f"{note['id']}: {note['title']}")
            
            
# Функция для просмотра одной заметки по ID
def view_note():
    # Запросить у пользователя ID заметки
    note_id = int(input("Введите ID заметки: "))
    # Найти заметку с заданным ID
    for note in notes:
        if note["id"] == note_id:
            # Вывести заголовок и текст заметки
            print(f"{note['title']}\n{note['text']}")
            break
    else:
        # Если заметка не найдена, вывести сообщение об этом
        print("Заметка не найдена")
        
        
# Функция для удаления заметки по ID
def delete_note():
    # Запросить у пользователя ID заметки
    note_id = int(input("Введите ID заметки: "))
    # Найти заметку с заданным ID и удалить ее из списка заметок
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            del notes[i]
            print(f"Заметка с ID {note_id} удалена")
            break
    else:
        # Если заметка не найдена, вывести сообщение об этом
        print("Заметка не найдена")
        
        
# Список заметок (изначально пуст)
notes = []

# Основной цикл программы
while True:
    # Вывести меню команд
    print("Меню команд:")
    print("1. Создать новую заметку")
    print("2. Просмотреть список всех заметок")
    print("3. Просмотреть одну заметку по ID")
    print("4. Удалить заметку по ID")
    print("5. Выход")
    
    # Запросить у пользователя номер команды
    command = input("Введите номер команды: ")
    
    # Обработать выбранную команду
    if command == "1":
        create_note()
    elif command == "2":
        list_notes()
    elif command == "3":
        view_note()
    elif command == "4":
        delete_note()
    elif command == "5":
        # Выход из программы
        break
    else:
        # Вывести сообщение об ошибке при вводе некорректной команды
        print("Некорректная команда")