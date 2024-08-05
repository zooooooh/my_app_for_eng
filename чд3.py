import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import random


class DictionaryApp:
    def __init__(self, master):
        self.master = master
        master.title("Словарь")

        # Стилизация
        style = ttk.Style()
        style.theme_use("clam")  # Можно использовать другие темы: "classic", "alt", "default", "xpnative"

        # Цвета
        background_color = "#f0f0f0"  # Светло-серый фон
        button_color = "#4CAF50"  # Зеленый цвет кнопок
        button_hover_color = "#45a049"  # Темнее зеленый при наведении
        text_color = "black"  # Черный текст

        # Шрифты
        title_font = ("Arial", 16, "bold")
        label_font = ("Arial", 12)
        entry_font = ("Arial", 12)

        # Настройка стилей
        style.configure("TButton", background=button_color, foreground="white", font=('Helvetica', 12, 'bold'))
        style.map("TButton",
                  foreground=[('pressed', 'white'), ('active', 'white')],
                  background=[('pressed', button_hover_color), ('active', button_hover_color)])
        style.configure("TEntry", foreground=text_color, font=entry_font)
        style.configure("TLabel", foreground=text_color, font=label_font)
        #  Создайте стиль для Ⓝttk.FrameⓃ с фоном
        style.configure("My.TFrame", background=background_color)

        # Главное меню
        self.main_menu_frame = ttk.Frame(master, padding=20, style="My.TFrame")  # Используйте стиль
        self.main_menu_frame.pack(fill="both", expand=True)

        self.title_label = ttk.Label(self.main_menu_frame, text="Словарь", font=title_font, background=background_color)
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.test_button = ttk.Button(self.main_menu_frame, text="Пройти тест", command=self.show_quiz_frame)
        self.test_button.grid(row=1, column=0, padx=20, pady=10)

        self.add_word_button = ttk.Button(self.main_menu_frame, text="Добавить слово", command=self.show_add_word_frame)
        self.add_word_button.grid(row=2, column=0, padx=20, pady=10)

        self.translate_button = ttk.Button(self.main_menu_frame, text="Перевести слово", command=self.show_translate_frame)
        self.translate_button.grid(row=3, column=0, padx=20, pady=10)

        # Фреймы для других разделов (скрыты по умолчанию)
        self.add_word_frame = ttk.Frame(master, padding=20, background=background_color)
        self.translate_frame = ttk.Frame(master, padding=20, background=background_color)
        self.quiz_frame = ttk.Frame(master, padding=20, background=background_color)

        # Добавить слово
        self.word_label = ttk.Label(self.add_word_frame, text="Слово:", background=background_color)
        self.word_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.word_entry = ttk.Entry(self.add_word_frame, width=20)
        self.word_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.translation_label = ttk.Label(self.add_word_frame, text="Перевод:", background=background_color)
        self.translation_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.translation_entry = ttk.Entry(self.add_word_frame, width=20)
        self.translation_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.add_button = ttk.Button(self.add_word_frame, text="Добавить", command=self.add_word)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.back_to_main_button_add = ttk.Button(self.add_word_frame, text="Назад", command=self.show_main_menu_frame)
        self.back_to_main_button_add.grid(row=3, column=0, columnspan=2, pady=10)

        # Перевод слова
        self.search_label = ttk.Label(self.translate_frame, text="Поиск:", background=background_color)
        self.search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.search_entry = ttk.Entry(self.translate_frame, width=20)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.translate_button = ttk.Button(self.translate_frame,text="Перевести", command=self.translate_word)
        self.translate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.translate_frame, text="", background=background_color)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.back_to_main_button_trans = ttk.Button(self.translate_frame, text="Назад", command=self.show_main_menu_frame)
        self.back_to_main_button_trans.grid(row=3, column=0, columnspan=2, pady=10)

        # Тест
        self.quiz_num_words_label = ttk.Label(self.quiz_frame, text="Количество слов:", background=background_color)
        self.quiz_num_words_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.quiz_num_words_entry = ttk.Entry(self.quiz_frame, width=5)
        self.quiz_num_words_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.start_quiz_button = ttk.Button(self.quiz_frame, text="Начать тест", command=self.start_quiz)
        self.start_quiz_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.quiz_label = ttk.Label(self.quiz_frame, text="", background=background_color)
        self.quiz_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.answer_label = ttk.Label(self.quiz_frame, text="Ваш перевод:", background=background_color)
        self.answer_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.answer_entry = ttk.Entry(self.quiz_frame, width=20, state="disabled")
        self.answer_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.check_answer_button = ttk.Button(self.quiz_frame, text="Проверить", command=self.check_answer)
        self.check_answer_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.back_to_main_button_quiz = ttk.Button(self.quiz_frame, text="Назад", command=self.show_main_menu_frame)
        self.back_to_main_button_quiz.grid(row=5, column=0, columnspan=2, pady=10)

        # Скрыть все фреймы кроме главного меню
        self.show_main_menu_frame()

    def show_main_menu_frame(self):
        self.add_word_frame.pack_forget()
        self.translate_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.main_menu_frame.pack(fill="both", expand=True)

    def show_add_word_frame(self):
        self.main_menu_frame.pack_forget()
        self.translate_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.add_word_frame.pack(fill="both", expand=True)

    def show_translate_frame(self):
        self.main_menu_frame.pack_forget()
        self.add_word_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.translate_frame.pack(fill="both", expand=True)

    def show_quiz_frame(self):
        self.main_menu_frame.pack_forget()
        self.add_word_frame.pack_forget()
        self.translate_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)

    # ... остальной код функций (add_word, translate_word, start_quiz, check_answer) ...

    def add_word(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()

        if not word or not translation:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите слово и перевод.")
            return

        with open("dictionary.txt", "r", encoding="utf-8") as file:
            for line in file:
                key, value = line.strip().split(":")
                if key == word:
                    messagebox.showinfo("Информация", "Слово уже существует в словаре.")
                    return

        with open("dictionary.txt", "a", encoding="utf-8") as file:
            file.write(f"{word}:{translation}\n")

        self.word_entry.delete(0, tk.END)
        self.translation_entry.delete(0, tk.END)

        messagebox.showinfo("Успех", "Слово успешно добавлено!")

    def translate_word(self):
        word = self.search_entry.get()

        with open("dictionary.txt", "r", encoding="utf-8") as file:
            for line in file:
                key, value = line.strip().split(":")
                if key == word:
                    self.result_label.config(text=f"Перевод: {value}")
                    return

        self.result_label.config(text="Слово не найдено")

    def start_quiz(self):
        global current_word, quiz_words, quiz_index, correct_answers
        quiz_index = 0
        correct_answers = 0
        quiz_words = []

        try:
            num_words = int(self.quiz_num_words_entry.get())
            if num_words <= 0:
                messagebox.showwarning("Ошибка", "Количество слов должно быть больше 0.")
                return
        except ValueError:
            messagebox.showwarning("Ошибка", "Введите числовое значение для количества слов.")
            return

        with open("dictionary.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) < num_words:
                messagebox.showwarning("Ошибка", f"В словаре меньше {num_words} слов. Добавьте слова для начала теста.")
                return
            quiz_words = random.sample(lines, num_words)

        current_word = quiz_words[quiz_index].strip().split(":")[0]
        self.quiz_label.config(text=f"Слово: {current_word}")
        self.answer_entry.config(state="normal")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus_set()

    def check_answer(self):
        global quiz_index, correct_answers
        user_answer = self.answer_entry.get()
        correct_answer = quiz_words[quiz_index].strip().split(":")[1]

        if user_answer.lower() == correct_answer.lower():
            correct_answers += 1
            messagebox.showinfo("Правильно!", "Верный перевод!")
        else:
            messagebox.showwarning("Неверно", f"Правильный перевод: {correct_answer}")

        quiz_index += 1
        if quiz_index < len(quiz_words):
            current_word = quiz_words[quiz_index].strip().split(":")[0]
            self.quiz_label.config(text=f"Слово: {current_word}")
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Конец теста", f"Вы прошли тест! Правильных ответов: {correct_answers} из {len(quiz_words)}.")
            self.quiz_label.config(text="")
            self.answer_entry.config(state="disabled")

root = tk.Tk()
app = DictionaryApp(root)
root.mainloop()


