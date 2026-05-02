import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class MovieLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Library")
        self.movies = []
        self.create_widgets()
        self.load_from_json()

    def create_widgets(self):
        # --- Поля ввода ---
        tk.Label(self.root, text="Название:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.title_entry = tk.Entry(self.root, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Жанр:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.genre_entry = tk.Entry(self.root, width=30)
        self.genre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Год выпуска:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.year_entry = tk.Вот полный рабочий код приложения «Movie Library» на Python с использованием Tkinter, JSON и валидацией ввода.

### Файл: `movie_library.py`
def create_widgets(self):
    # --- Поля ввода ---
    tk.Label(self.root, text="Название:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
    self.title_entry = tk.Entry(self.root, width=30)
    self.title_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(self.root, text="Жанр:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
    self.genre_entry = tk.Entry(self.root, width=30)
    self.genre_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(self.root, text="Год выпуска:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
    self.year_entry = tk.Entry(self.root, width=30)
    self.year_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(self.root, text="Рейтинг (0-10):").grid(row=3, column=0, padx=5, pady=5, sticky='e')
    self.rating_entry = tk.Entry(self.root, width=30)
    self.rating_entry.grid(row=3, column=1, padx=5, pady=5)

    # --- Кнопка добавления ---
    add_btn = tk.Button(self.root, text="Добавить фильм", command=self.add_movie)
    add_btn.grid(row=4, column=0, columnspan=2, pady=10)

    # --- Таблица ---
    self.tree = ttk.Treeview(self.root, columns=("title", "genre", "year", "rating"), show='headings')
    self.tree.heading("title", text="Название")
    self.tree.heading("genre", text="Жанр")
    self.tree.heading("year", text="Год")
    self.tree.heading("rating", text="Рейтинг")
    self.tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    # Настройка сетки для растягивания таблицы
    self.root.grid_rowconfigure(5, weight=1)
    self.root.grid_columnconfigure(1, weight=1)

    # --- Фильтры ---
    tk.Label(self.root, text="Фильтр по жанру:").grid(row=6, column=0, padx=5, pady=5, sticky='e')
    self.genre_filter = tk.Entry(self.root)
    self.genre_filter.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(self.root, text="Фильтр по году:").grid(row=7, column=0, padx=5, pady=5, sticky='e')
    self.year_filter = tk.Entry(self.root)
    self.year_filter.grid(row=7, column=1, padx=5, pady=5)

    filter_btn = tk.Button(self.root, text="Фильтровать", command=self.filter_movies)
    filter_btn.grid(row=8, column=0, columnspan=2, pady=10)

    # --- Кнопки JSON ---
    save_btn = tk.Button(self.root, text="Сохранить в JSON", command=self.save_to_json)
    save_btn.grid(row=9, column=0, padx=5)

    load_btn = tk.Button(self.root, text="Загрузить из JSON", command=self.load_from_json)
    load_btn.grid(row=9, column=1, padx=5)

def add_movie(self):
    title = self.title_entry.get().strip()
    genre = self.genre_entry.get().strip()
    year = self.year_entry.get().strip()
    rating = self.rating_entry.get().strip()

    # Валидация
    if not title or not genre or not year or not rating:
        messagebox.showerror("Ошибка", "Все поля обязательны!")
        return
    
    if not year.isdigit():
        messagebox.showerror("Ошибка", "Год должен быть числом!")
        return

    try:
        rating_val = float(rating)
        if not (0 <= rating_val <= 10):
            raise ValueError
        rating_str = f"{rating_val:.1f}"
        if rating_str.endswith('.0'):
            rating_str = str(int(rating_val))
        rating = rating_str
        
        # Добавление в таблицу
        self.tree.insert('', 'end', values=(title, genre, year, rating))
        
        # Очистка полей
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
        
        self.title_entry.focus()
        
        # Сохраняем в список для JSON
        self.movies.append({
            "title": title,
            "genre": genre,
            "year": year,
            "rating": rating
        })
        
        messagebox.showinfo("Успех", "Фильм добавлен!")
        
    except ValueError:
        messagebox.showerror("Ошибка", "Рейтинг должен быть числом от 0 до 10!")

def filter_movies(self):
    genre_filter_text = self.genre_filter.get().strip().lower()
    year_filter_text = self.year_filter.get().strip()
    
    for row in self.tree.get_children():
        values = self.tree.item(row)['values']
        
        genre_match = (not genre_filter_text) or (genre_filter_text in values[1].lower())
        
        if year_filter_text.isdigit():
            year_match = values[2] == year_filter_text
        else:
            year_match = True  # Если фильтр не число — не фильтруем по году

        if genre_match and year_match:
            self.tree.item(row, tags='')
            self.tree.tag_configure('', elide=False)  # Показать
        else:
            self.tree.item(row, tags='hidden')
            self.tree.tag_configure('hidden', elide=True)  # Скрыть

def save_to_json(self):
    try:
        with open('movies.json', 'w', encoding='utf-8') as f:
            json.dump(self.movies, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Успех", "Данные сохранены в movies.json")
        
        # Обновляем список фильмов из таблицы (на случай изменений без кнопки Добавить)
        self.movies = []
        for row in self.tree.get_children():
            values = self.tree.item(row)['values']
            self.movies.append({
                "title": values[0],
                "genre": values[1],
                "year": values[2],
                "rating": values[3]
            })
            
        with open('movies.json', 'w', encoding='utf-8') as f:
            json.dump(self.movies, f, ensure_ascii=False, indent=4)
            
        messagebox.showinfo("Успех", "Данные синхронизированы и сохранены в movies.json")
        
        
        
        
        
        


def load_from_json(self):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
