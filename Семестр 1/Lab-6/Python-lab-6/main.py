class Book:
    className = "Book"

    def __init__(self, count_pages, ttr_page, count_img):
        self.count_pages = count_pages
        self.ttr_page = ttr_page
        self.count_img = count_img

    def ttr(self):
        ttr = (self.count_pages * self.ttr_page) / (60 * 60)
        return ttr

    def info(self):
        print(f"{self.className}:")
        print(f"Кол-во страниц: {self.count_pages}")
        print(f"Кол-во картинок: {self.count_img}")
        print(f"Время чтения в часах: {self.ttr()}")


class Phonebook(Book):
    className = "Phonebook"

    def __init__(self, count_pages, ttr_page, count_img, count_numbers):
        super().__init__(count_pages, ttr_page, count_img)
        self.count_pages = count_pages
        self.ttr_page = ttr_page
        self.count_img = count_img
        self.count_numbers = count_numbers

    def count_numbers_on_page(self):
        count_numbers_on_page = self.count_pages / self.count_numbers
        return count_numbers_on_page

    def ttr(self):
        ttr = super().ttr()
        return ttr

    def info(self):
        super().info()
        print(f"Чтение одного номера(сек): {self.count_numbers}")
        print(f"Кол-во номеров на странице: {self.count_numbers_on_page()}")


class Encyclopedia(Book):
    className = "Encyclopedia"

    def __init__(self, count_pages, ttr_page, count_image, sphere):
        super().__init__(count_pages, ttr_page, count_image)
        self.count_pages = count_pages
        self.ttr_page = ttr_page
        self.count_image = count_image
        self.sphere = sphere

    def ttr(self):
        ttr = super().ttr()
        return ttr

    def info(self):
        super().info()
        print(f"Предметная тема: {self.sphere}")


x = Book(345, 360, 44)
y = Phonebook(800, 180, 0, 5)
z = Encyclopedia(1200, 600, 200, "Space")
x.ttr()
y.ttr()
z.ttr()
x.info()
y.info()
z.info()
