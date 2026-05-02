import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

class WeatherDiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Diary")
        self.records = []
        self.create_widgets()
        self.load_from_json()

    def create_widgets(self):
        # --- Поля ввода ---
        tk.Label(self.root, text="Дата (ГГГГ-ММ-ДД):").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.date_entry = tk.Entry(self.root, width=20)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Температура (°C):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.temp_entry = tk.Entry(self.root, width=20)
        self.temp_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Описание:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.desc_entry = tk.Entry(self.root, width=20)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Осадки:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.rain_var = tk.StringVar(value="Нет")
        rain_options = ["Да", "Нет"]
        self.rain_menu = ttk.OptionMenu(self.root, self.rain_var, *rain_options)
        self.rain_menu.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # --- Кнопка добавления ---
        add_btn = tk.Button(self.root, text="Добавить запись", command=self.add_record)
        add_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # --- Таблица ---
        self.tree = ttk.Treeview(self.root, columns=("date", "temp", "desc", "rain"), show='headings')
        self.tree.heading("date", text="Дата")
        self.tree.heading("temp", text="Температура")
        self.tree.heading("desc", text="Описание")
        self.tree.heading("rain", text="Осадки")
        self.tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        # Настройка сетки для растягивания таблицы
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # --- Фильтры ---
        tk.Label(self.root, text="Фильтр по дате:").grid(row=6, column=0, padx=5, pady=5, sticky='e')
        self.filter_date = tk.Entry(self.root)
        self.filter_date.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Фильтр по температуре (выше):").grid(row=7, column=0, padx=5, pady=5, sticky='e')
        self.filter_temp = tk.Entry(self.root)
        self.filter_temp.grid(row=7, column=1, padx=5, pady=5)

        filter_btn = tk.Button(self.root, text="Фильтровать", command=self.filter_records)
        filter_btn.grid(row=8, column=0, columnspan=2, pady=10)

        # --- Кнопки JSON ---
        save_btn = tk.Button(self.root, text="Сохранить в JSON", command=self.save_to_json)
        save_btn.grid(row=9, column=0, padx=5)

        load_btn = tk.Button(self.root, text="Загрузить из JSON", command=self.load_from_json)
        load_btn.grid(row=9, column=1, padx=5)

    def add_record(self):
        date = self.date_entry.get().strip()
        temp = self.temp_entry.get().strip()
        desc = self.desc_entry.get().strip()
        rain = self.rain_var.get()

        # Валидация
        if not date or not temp or not desc:
            messagebox.showerror("Ошибка", "Все поля обязательны!")
            return

         # Проверка формата даты ГГГГ-ММ-ДД
         try:
             datetime.strptime(date, '%Y-%m-%d')
         except ValueError:
             messagebox.showerror("Ошибка", "Дата должна быть в формате ГГГГ-ММ-ДД (например:Вот полный рабочий код для приложения **«Weather Diary»** (Дневник погоды) на Python с использованием Tkinter, а также подробные инструкции по настройке Git и созданию README.

---

### Полный рабочий код: `weather_diary.py`
    
    
    
    
    
    
    
    
    
    
    
    
    
