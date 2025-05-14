import time as t
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()
engine = create_engine('sqlite:///./data/database.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'UserID'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)

def wait():
    for x in range(3):
        print('.', end='', flush=True)
        t.sleep(0.3)
    print()

def run(username):
    file_name = f"{username}.txt"
    # Создаем файл если его нет
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("Заметки:\n")
    
    while True:
        print("\n" + "="*30)
        print(f"Привет, {username}! Выберите действие:")
        print("1 - Добавить заметку")
        print("2 - Показать все заметки")
        print("3 - Очистить все заметки")
        print("4 - Выйти из аккаунта")
        
        choice = input(">>> ").strip()
        
        if choice == '1':
            # Добавление новой заметки
            note = input("Введите вашу заметку: ")
            if 
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(f"- {note}\n")
            print("Заметка успешно добавлена!")            
        elif choice == '2':
            # Показать все заметки
            with open(file_name, "r", encoding="utf-8") as file:
                print(file.read())
                
        elif choice == '3':
            # Очистка всех заметок
            confirm = input("Вы уверены, что хотите очистить все заметки? (y/n): ").lower()
            if confirm == 'y':
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write("Заметки:\n")
                print("Все заметки очищены!")
            else:
                print("Очистка отменена")
                
        elif choice == '4':
            # Выход из аккаунта
            print("Выход из аккаунта...")
            break
            
        else:
            print("Неверный выбор. Попробуйте еще раз.")

def reg(username, password):
    try:
        new_user = User(username=username.strip(), password=password.strip())
        session.add(new_user)
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        print("Пользователь с таким именем уже существует!")
        return False
    except Exception as e:
        session.rollback()
        print(f"Ошибка регистрации: {e}")
        return False

def log(username, password):
    try:
        user = session.query(User).filter_by(
            username=username.strip(),
            password=password.strip()
        ).first()
        return user is not None
    except Exception as e:
        print(f"Ошибка авторизации: {e}")
        return False

def main():
    while True:
        print("\n" + "="*30)
        command = input('Войдите или зарегистрируйтесь:\n/reg - регистрация\n/log - вход\n>>> ').strip().lower()
        
        if command == '/reg':
            print('Процесс регистрации...')
            wait()
            n = input('Введите ваш логин >>> ').strip()
            p = input('Введите ваш пароль >>> ').strip()
            
            if n and p:
                if reg(n, p):
                    print('Регистрация прошла успешно!')
            else:
                print('Логин и пароль не могут быть пустыми!')
                
        elif command == '/log':
            print('Процесс входа...')
            wait()
            n = input('Введите ваш логин >>> ').strip()
            p = input('Введите ваш пароль >>> ').strip()
            
            if n and p:
                if log(n, p):
                    print('Авторизация успешна!')
                    run(n)
                else:
                    print('Неверный логин или пароль!')
            else:
                print('Логин и пароль не могут быть пустыми!')
                
        else:
            print("Неверная команда. Используйте /reg или /log")

if __name__ == "__main__":
    try:
        main()
    finally:
        session.close()