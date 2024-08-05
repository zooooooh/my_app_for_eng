import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

kivy.require('1.11.0')  # Замените версию на актуальную, если необходимо

class DictionaryApp(App):
    def build(self):
        self.dictionary = {}  # Словарь для хранения слов

        # Главный экран
        main_layout = BoxLayout(orientation='vertical')

        # Добавление слов
        add_layout = BoxLayout(orientation='vertical', padding=10)
        add_layout.add_widget(Label(text="Добавить слово:"))
        self.word_input = TextInput(multiline=False)
        add_layout.add_widget(self.word_input)
        add_layout.add_widget(Label(text="Перевод:"))
        self.translation_input = TextInput(multiline=False)
        add_layout.add_widget(self.translation_input)
        add_layout.add_widget(Button(text="Добавить", on_press=self.add_word))
        main_layout.add_widget(add_layout)

        # Перевод слов
        translate_layout = BoxLayout(orientation='vertical', padding=10)
        translate_layout.add_widget(Label(text="Введите слово:"))
        self.search_input = TextInput(multiline=False)
        translate_layout.add_widget(self.search_input)
        translate_layout.add_widget(Button(text="Перевести", on_press=self.translate_word))
        self.translation_output = Label(text="")
        translate_layout.add_widget(self.translation_output)
        main_layout.add_widget(translate_layout)

        # Редактирование/Удаление
        edit_delete_layout = BoxLayout(orientation='vertical', padding=10)
        edit_delete_layout.add_widget(Label(text="Слово для редактирования/удаления:"))
        self.edit_word_input = TextInput(multiline=False)
        edit_delete_layout.add_widget(self.edit_word_input)
        edit_delete_layout.add_widget(Button(text="Редактировать", on_press=self.edit_word))
        edit_delete_layout.add_widget(Button(text="Удалить", on_press=self.delete_word))
        main_layout.add_widget(edit_delete_layout)

        # Викторина
        quiz_layout = BoxLayout(orientation='vertical', padding=10)
        quiz_layout.add_widget(Label(text="Количество слов в тесте:"))
        self.quiz_num_words_input = TextInput(multiline=False, input_filter='int')
        quiz_layout.add_widget(self.quiz_num_words_input)
        quiz_layout.add_widget(Button(text="Начать тест", on_press=self.start_quiz))
        self.quiz_question_label = Label(text="")
        quiz_layout.add_widget(self.quiz_question_label)
        self.quiz_answer_input = TextInput(multiline=False, state='disabled')
        quiz_layout.add_widget(self.quiz_answer_input)
        quiz_layout.add_widget(Button(text="Проверить", on_press=self.check_quiz_answer, state='disabled'))
        main_layout.add_widget(quiz_layout)

        return main_layout

    def add_word(self, instance):
        word = self.word_input.text.strip()
        translation = self.translation_input.text.strip()
        if word and translation:
            self.dictionary[word] = translation
            self.word_input.text = ""
            self.translation_input.text = ""
            self.show_popup("Успешно!", "Слово добавлено в словарь.")
        else:
            self.show_popup("Ошибка", "Введите слово и его перевод.")

    def translate_word(self, instance):
        word = self.search_input.text.strip()
        if word in self.dictionary:
            self.translation_output.text = self.dictionary[word]
        else:
            self.translation_output.text = "Слово не найдено."

    def edit_word(self, instance):
        word = self.edit_word_input.text.strip()
        if word in self.dictionary:
            new_translation = self.translation_input.text.strip()
            if new_translation:
                self.dictionary[word] = new_translation
                self.edit_word_input.text = ""
                self.show_popup("Успешно!", "Слово отредактировано.")
            else:
                self.show_popup("Ошибка", "Введите новый перевод.")
        else:
            self.show_popup("Ошибка", "Слово не найдено.")

    def delete_word(self, instance):
        word = self.edit_word_input.text.strip()
        if word in self.dictionary:
            del self.dictionary[word]
            self.edit_word_input.text = ""
            self.show_popup("Успешно!", "Слово удалено.")
        else:
            self.show_popup("Ошибка", "Слово не найдено.")

    def start_quiz(self, instance):
        num_words = int(self.quiz_num_words_input.text)
        if num_words > len(self.dictionary) or num_words <= 0:
            self.show_popup("Ошибка", "Некорректное количество слов.")
            return

        self.quiz_words = list(self.dictionary.keys())[:num_words]
        self.quiz_index = 0
        self.quiz_question_label.text = "Вопрос 1/{}".format(num_words)
        self.quiz_answer_input.text = ""
        self.quiz_answer_input.state = 'normal'
        self.quiz_question_label.text = "Переведите слово: {}".format(self.quiz_words[self.quiz_index])
        self.quiz_answer_input.text = ""
        self.check_quiz_answer.state = 'normal'
        self.show_popup("Викторина", "Тест начался! Переведите слово: {}".format(self.quiz_words[self.quiz_index]))

    def check_quiz_answer(self, instance):
        answer = self.quiz_answer_input.text.strip()
        correct_answer = self.dictionary[self.quiz_words[self.quiz_index]]
        if answer.lower() == correct_answer.lower():
            self.show_popup("Правильно!", "Ваш ответ верный.")
        else:
            self.show_popup("Неверно", "Правильный ответ: {}".format(correct_answer))
        self.quiz_index += 1
        if self.quiz_index < len(self.quiz_words):
            self.quiz_question_label.text = "Вопрос {}/{}".format(self.quiz_index + 1, len(self.quiz_words))
            self.quiz_question_label.text = "Переведите слово: {}".format(self.quiz_words[self.quiz_index])
            self.quiz_answer_input.text = ""
        else:
            self.quiz_answer_input.state = 'disabled'
            self.check_quiz_answer.state = 'disabled'
            self.quiz_question_label.text = "Тест завершен!"

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None),
                      size=(300, 150))
        popup.open()

if __name__ == '__main__':
    DictionaryApp().run()
