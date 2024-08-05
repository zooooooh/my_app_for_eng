import tkinter as tk
from tkinter import ttk

class UI:
    def __init__(self, master):
        self.master = master

        # Стилизация (оставьте код стилизации здесь)

        # Главное меню
        self.main_menu_frame = ttk.Frame(master, padding=20)
        self.main_menu_frame.pack()

        self.test_button = ttk.Button(self.main_menu_frame, text="Пройти тест")
        self.test_button.grid(row=0, column=0, pady=10)

        self.add_word_button = ttk.Button(self.main_menu_frame, text="Добавить слово")
        self.add_word_button.grid(row=1, column=0, pady=10)

        self.translate_button = ttk.Button(self.main_menu_frame, text="Перевести слово")
        self.translate_button.grid(row=2, column=0, pady=10)

        # Фреймы для других разделов (скрыты по умолчанию)
        self.add_word_frame = ttk.Frame(master, padding=20)
        self.translate_frame = ttk.Frame(master, padding=20)
        self.quiz_frame = ttk.Frame(master, padding=20)

        # Добавить слово
        self.word_label = ttk.Label(self.add_word_frame, text="Слово:")
        self.word_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.word_entry = ttk.Entry(self.add_word_frame, width=20)
        self.word_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.translation_label = ttk.Label(self.add_word_frame, text="Перевод:")
        self.translation_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.translation_entry = ttk.Entry(self.add_word_frame, width=20)
        self.translation_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.add_button = ttk.Button(self.add_word_frame, text="Добавить")
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.back_to_main_button_add = ttk.Button(self.add_word_frame, text="Назад")
        self.back_to_main_button_add.grid(row=3, column=0, columnspan=2, pady=10)

        # Перевод слова
        self.search_label = ttk.Label(self.translate_frame, text="Поиск:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.search_entry = ttk.Entry(self.translate_frame, width=20)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.translate_button = ttk.Button(self.translate_frame, text="Перевести")
        self.translate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.translate_frame, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.back_to_main_button_trans = ttk.Button(self.translate_frame, text="Назад")
        self.back_to_main_button_trans.grid(row=3, column=0, columnspan=2, pady=10)

        # Тест
        self.quiz_num_words_label = ttk.Label(self.quiz_frame, text="Количество слов:")
        self.quiz_num_words_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.quiz_num_words_entry = ttk.Entry(self.quiz_frame, width=5)
        self.quiz_num_words_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.start_quiz_button = ttk.Button(self.quiz_frame, text="Начать тест")
        self.start_quiz_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.quiz_label = ttk.Label(self.quiz_frame, text="")
        self.quiz_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.answer_label = ttk.Label(self.quiz_frame, text="Ваш перевод:")
        self.answer_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.answer_entry = ttk.Entry(self.quiz_frame, width=20, state="disabled")
        self.answer_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.check_answer_button = ttk.Button(self.quiz_frame, text="Проверить")
        self.check_answer_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.back_to_main_button_quiz = ttk.Button(self.quiz_frame, text="Назад")
        self.back_to_main_button_quiz.grid(row=5, column=0, columnspan=2, pady=10)


        # Скрыть все фреймы кроме главного меню
        self.show_main_menu_frame()

    def show_main_menu_frame(self):
        self.add_word_frame.pack_forget()
        self.translate_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.main_menu_frame.pack()

    def show_add_word_frame(self):
        self.main_menu_frame.pack_forget()
        self.translate_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.add_word_frame.pack()

    def show_translate_frame(self):
        self.main_menu_frame.pack_forget()
        self.add_word_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.translate_frame.pack()

    def show_quiz_frame(self):
        self.main_menu_frame.pack_forget()
        self.add_word_frame.pack_forget()
        self.translate_frame.pack_forget()
        self.quiz_frame.pack()

