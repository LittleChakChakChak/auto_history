from django.db import models


# Кузов ------------------------------------------------------
class Body(models.Model):
    name = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузова'


# Привод ------------------------------------------------------
class Drive(models.Model):
    name = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Привод'
        verbose_name_plural = 'Привода'


# КПП ------------------------------------------------------
class Transmission(models.Model):
    name = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Трансмисия'
        verbose_name_plural = 'Трансмисии'


# Двигатель ------------------------------------------------------
class Engine(models.Model):
    name = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'


# Страны ------------------------------------------------------
class Country(models.Model):
    name = models.CharField('Наименование', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


# Марка ------------------------------------------------------
class Brend(models.Model):
    name = models.CharField('Наименование', max_length=150)
    creator = models.CharField('Создатель', max_length=250)
    logo = models.ImageField('Логотип')
    about_brand = models.TextField('О марке')
    number_fans = models.PositiveIntegerField('Количество фанатов')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


# Модель ------------------------------------------------------
class Model(models.Model):
    name = models.CharField('Наименование', max_length=150)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


# Автомобиль ------------------------------------------------------
class Car(models.Model):
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year_release = models.DateField('Год выпуска')
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    body = models.ForeignKey(Body, on_delete=models.CASCADE)
    rating = models.FloatField('Рейтинг', max_length=4)
    features = models.TextField('Особенности')

    def __str__(self):
        return self.brend + '' + self.model + '' + self.body + '' + self.year_release

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


# Фотографии ------------------------------------------------------
class Photo(models.Model):
    сar = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo_auto = models.ImageField('Фото')

    def __str__(self):
        return self.car + '' + self.photo_auto

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


# Ссылка на подбор ------------------------------------------------------
class Link_selection(models.Model):
    link = models.URLField('Ссылка')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка на подбор'
        verbose_name_plural = 'Ссылки на подборы'


# Пользователь ------------------------------------------------------
class User(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Почта')
    number = models.PositiveIntegerField('Телефон')
    city = models.CharField('Город', max_length=300)
    personal_car = models.CharField('Личный автомобиль', max_length=100)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# Пароль ------------------------------------------------------
class Password(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField('Имя', max_length=50)


# Любимая марка ------------------------------------------------------
class Favorite_brand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brend, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.brand

    class Meta:
        verbose_name = 'Любимая марка'
        verbose_name_plural = 'Любимые марки'


# Понравившая машина ------------------------------------------------------
class Like_car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.car

    class Meta:
        verbose_name = 'Понравившая машина'
        verbose_name_plural = 'Понравившие машины'


# Статья ------------------------------------------------------
class Articles(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    text = models.TextField('Текст')
    date_publication = models.DateTimeField('Дата публикации')
    estimation = models.FloatField('Оценка', max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car + ' ' + self.date_publication + ' ' + self.user

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# Комментарии ------------------------------------------------------
class Сomment(models.Model):
    articles = models.OneToOneField(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Текст')
    date_comment = models.DateTimeField('Дата комментария')

    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарии'
