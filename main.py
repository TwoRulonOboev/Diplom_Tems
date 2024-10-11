import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import MarianMTModel, MarianTokenizer

# Функция для перевода текста построчно
def translate_text_lines(text, source_lang, target_lang):
    # Загрузка модели MarianMT для перевода
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Разбиение текста на строки
    lines = text.splitlines()

    translated_lines = []

    # Перевод каждой строки
    for line in lines:
        if line.strip():  # Пропуск пустых строк
            inputs = tokenizer(line, return_tensors='pt', padding=True, truncation=True)
            translated = model.generate(**inputs)
            translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
            translated_lines.append(translated_text)
        else:
            translated_lines.append('')  # Сохранение пустых строк

    # Объединение переведённых строк обратно в текст
    return "\n".join(translated_lines)

# Функция для обработки загруженного файла
def process_file():
    # Открытие диалогового окна для выбора файла
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not file_path:
        return

    # Чтение содержимого файла
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Получение выбранных языков
    source_lang = source_lang_var.get()
    target_lang = target_lang_var.get()

    if not source_lang or not target_lang:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите исходный и целевой языки!")
        return
    
    # Перевод текста построчно
    translated_text = translate_text_lines(text, source_lang, target_lang)

    # Запись переведенного текста в новый файл
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        messagebox.showinfo("Успех", "Текст успешно переведен и сохранен!")

# Создание окна
root = tk.Tk()
root.title("Переводчик текста")

# Метка и выпадающий список для выбора исходного языка
tk.Label(root, text="Исходный язык:").grid(row=0, column=0, padx=10, pady=10)
source_lang_var = tk.StringVar(root)
source_lang_menu = tk.OptionMenu(root, source_lang_var, "en", "fr", "de", "ru", "es", "it")
source_lang_menu.grid(row=0, column=1, padx=10, pady=10)

# Метка и выпадающий список для выбора целевого языка
tk.Label(root, text="Целевой язык:").grid(row=1, column=0, padx=10, pady=10)
target_lang_var = tk.StringVar(root)
target_lang_menu = tk.OptionMenu(root, target_lang_var, "en", "fr", "de", "ru", "es", "it")
target_lang_menu.grid(row=1, column=1, padx=10, pady=10)

# Кнопка для загрузки и обработки файла
process_button = tk.Button(root, text="Загрузить и перевести файл", command=process_file)
process_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Запуск главного цикла приложения
root.mainloop()
