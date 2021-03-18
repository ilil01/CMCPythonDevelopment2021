Задача 1 (головоломка): Напишите класс Application(tk.Frame) таким образом, чтобы приведённый ниже код создавал приложение с интерфейсной моделью как на картинке (цвета воспроизводить не надо).

![Alt text](http://uneex.org/LecturesCMC/PythonDevelopment2021/04_PublicRepositoryEvents?action=AttachFile&do=get&target=allinone.png)

```python3
class App(Application):
    def createWidgets(self):
        self.message = "Congratulations!\nYou've found a sercet level!"
        self.F1(tk.LabelFrame, "1:0", text="Frame 1")
        self.F1.B1(tk.Button, "0:0/NW", text="1")
        self.F1.B2(tk.Button, "0:1/NE", text="2")
        self.F1.B3(tk.Button, "1:0+1/SEW", text="3")
        self.F2(tk.LabelFrame, "1:1", text="Frame 2")
        self.F2.B1(tk.Button, "0:0/N", text="4")
        self.F2.B2(tk.Button, "0+1:1/SEN", text="5")
        self.F2.B3(tk.Button, "1:0/S", text="6")
        self.Q(tk.Button, "2.0:1.2/SE", text="Quit", command=self.quit)
        self.F1.B3.bind("<Any-Key>", lambda event: showinfo(self.message.split()[0], self.message))

app = App(title="Sample application")
app.mainloop()
```

* Особенности:

1. Конструктором виджета является первое обращение к нему по имени, все последующие обращения по этому имени просто выдают сам объект-виджет
    * Первый параметр — тип виджета
    * Второй параметр — геометрия (см. далее)
    * Остальные параметры — именные параметры для создания виджета данного типа 

2. Виджет A.B встроен в виджет A.
    * Геометрия B указывается относительно A
    * В геометрии также указывается вес (эластичность, weight) рядов и колонок. Это значение наследуется от последнего заданного в данном ряду/колонке виджета (по умолчанию 1)
    * (в примере первые три кнопки встроены в F1, а следующие три — в F2, соответственно задана и геометрия) 
3. Обращение к уже заданному виджету работает как обычно (возвращается сам объект-виджет) 

Задача 2: Реализовать класс InputLabel(tk.Label), для простейшего редактирования строк в виджете Label (такая дешёвая пластиковая имитация Entry). Должно поддерживаться

* Требования и свойства:
    * Разрешённый фокус и рамка фокуса по умолчанию
    * Ввод печатных символов
    * Текстовый курсор
    * Перемещение курсора стрелками и Home/End
    * Перемещение курсора и получение фокуса кликом мыши
    * Удаление символа перед курсором 

![Alt text](http://uneex.org/LecturesCMC/PythonDevelopment2021/04_PublicRepositoryEvents?action=AttachFile&do=get&target=LabelEdit.gif)
