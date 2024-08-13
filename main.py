# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f"сформирован отчет: {self.title} - {self.content}")


from abc import ABC, abstractmethod

# Определяем абстрактный класс Formatted, который будет основой для различных форматов отчета.
class Formatted(ABC):
    # Абстрактный метод format, который должен быть реализован в подклассах.
    @abstractmethod
    def format(self, report):
        pass

# Класс TextFormatted реализует форматирование отчета в текстовом формате.
class TextFormatted(Formatted):
    # Метод format выводит заголовок и содержимое отчета в текстовом виде.
    def format(self, report):
        print(report.title)
        print(report.content)

# Класс HTMLFormatted реализует форматирование отчета в HTML формате.
class HTMLFormatted(Formatted):
    # Метод format выводит заголовок и содержимое отчета в формате HTML.
    def format(self, report):
        print(f"<H1>{report.title}</H1>")
        print(f"<p>{report.content}</p>")

# Класс Report представляет собой отчет с заголовком, содержимым и форматом.
class Report():
    # Метод init инициализирует объект отчета с заголовком, содержимым и форматом.
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    # Метод docPrinter выводит отформатированный отчет, используя указанный формат.
    def docPrinter(self):
        self.formatted.format(self)

# Создаем экземпляр Report с текстовым форматированием и выводим его.
report = Report("Это заголовок", "это контент, его тут много написано", TextFormatted())
report.formatted.format(report)

