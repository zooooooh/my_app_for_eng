import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ui
import data
import logic

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        master.title("Словарь")

        # Создаем экземпляр UI
        self.ui = ui.UI(self.master)

        # Инициализируем данные
        self.data = data.Data()

        # Создаем экземпляр логики
        self.logic = logic.Logic(self.data)

        # Связываем кнопки с функциями
        self.ui.add_word_button.config(command=self.add_word)
        self.ui.translate_button.config(command=self.translate_word)
        self.ui.test_button.config(command=self.ui.show_quiz_frame)
        self.ui.start_quiz_button.config(command=self.start_quiz)
        self.ui.check_answer_button.config(command=self.check_answer)

        self.ui.back_to_main_button_add.config(command=self.ui.show_main_menu_frame)
        self.ui.back_to_main_button_trans.config(command=self.ui.show_main_menu_frame)
        self.ui.back_to_main_button_quiz.config(command=self.ui.show_main_menu_frame)

        self.current_quiz_word = None
        self.quiz_index = 0

    def add_word(self):
        word = self.ui.word_entry.get()
        translation = self.ui.translation_entry.get()

        if not word or not translation:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите слово и перевод.")
            return

        if not self.data.add_word(word, translation):
            messagebox.showinfo("Информация", "Слово уже существует в словаре.")
            return

        self.ui.word_entry.delete(0, tk.END)
        self.ui.translation_entry.delete(0, tk.END)

        messagebox.showinfo("Успех", "Слово успешно добавлено!")

    def translate_word(self):
        word = self.ui.search_entry.get()
        translation = self.logic.translate(word)
        if translation:
            self.ui.result_label.config(text=f"Перевод: {translation}")
        else:
            self.ui.result_label.config(text="Слово не найдено")

    def start_quiz(self):
        num_words = int(self.ui.quiz_num_words_entry.get())
        if num_words <= 0:
            messagebox.showwarning("Ошибка", "Количество слов должно быть больше 0.")
            return
        if len(self.data.dictionary) < num_words:
            messagebox.showwarning("Ошибка", f"В словаре меньше {num_words} слов. Добавьте слова для начала теста.")
            return

        self.logic.start_quiz(num_words)
        self.quiz_index = 0
        self.show_next_quiz_word()

    def show_next_quiz_word(self):
        if self.quiz_index < len(self.logic.quiz_words):
            self.current_quiz_word = self.logic.quiz_words[self.quiz_index]
            self.ui.quiz_label.config(text=f"Слово: {self.current_quiz_word}")
            self.ui.answer_entry.config(state="normal")
            self.ui.answer_entry.delete(0, tk.END)  # Очищаем поле ответа
            self.ui.answer_entry.config(state="disabled")
        else:
            self.ui.quiz_label.config(text="Тест завершен!")
            self.ui.answer_entry.config(state="disabled")

    def check_answer(self):
        user_answer = self.ui.answer_entry.get()
        is_correct = self.logic.check_answer(self.current_quiz_word, user_answer)
        if is_correct:
            messagebox.showinfo("Правильно!", "Верный перевод!")
        else:
            messagebox.showwarning("Неверно", f"Правильный перевод: {self.logic.get_translation(self.current_quiz_word)}")
        self.quiz_index += 1
        self.show_next_quiz_word()

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()

