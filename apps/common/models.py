from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django_resized import ResizedImageField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    body = RichTextUploadingField(verbose_name="Текст")
    image = ResizedImageField(upload_to="news", verbose_name="Изображение")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]
        

class Gallery(BaseModel):
    image = models.ImageField(upload_to="gallery", verbose_name="Изображение")
    youtube_link = models.CharField(max_length=255, verbose_name="Ссылка на видео", blank=True, null=True)
    order = models.PositiveIntegerField(verbose_name="Порядок", default=1)
    
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
        ordering = ["order"]
        

class Service(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название")
    icon = models.FileField(upload_to="services", verbose_name="Иконка")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class HotelStar(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

class Hotel(BaseModel):    
    name = models.CharField(max_length=255, verbose_name="Название")
    logo = models.FileField(upload_to="hotels", verbose_name="Логотип")
    star = models.PositiveIntegerField(verbose_name="Количество звезд", choices=HotelStar.choices)
    distance = models.PositiveIntegerField(verbose_name="Расстояние до мечети")
    image1 = models.ImageField(upload_to="hotels", verbose_name="Изображение 1")
    image2 = models.ImageField(upload_to="hotels", verbose_name="Изображение 2", blank=True, null=True)
    image3 = models.ImageField(upload_to="hotels", verbose_name="Изображение 3", blank=True, null=True)
    image4 = models.ImageField(upload_to="hotels", verbose_name="Изображение 4", blank=True, null=True)
    image5 = models.ImageField(upload_to="hotels", verbose_name="Изображение 5", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class Transport(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    subtitle = models.CharField(max_length=255, verbose_name="Подзаголовок")
    body = models.TextField(verbose_name="Текст")
    image1 = models.ImageField(upload_to="transport", verbose_name="Изображение 1")
    image2 = models.ImageField(upload_to="transport", verbose_name="Изображение 2", blank=True, null=True)
    image3 = models.ImageField(upload_to="transport", verbose_name="Изображение 3", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"
    

class Tarif(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    body = models.TextField(verbose_name="Текст")
    start_time = models.DateField(verbose_name="Дата начала")
    end_time = models.DateField(verbose_name="Дата окончания")
    days_in_Makkah = models.PositiveIntegerField(verbose_name="Количество дней в Мекке")
    days_in_Madinah = models.PositiveIntegerField(verbose_name="Количество дней в Медине")
    Makkah_hotel = models.ForeignKey(Hotel, verbose_name="Отель в Мекке", related_name="makkah_hotel", on_delete=models.SET_NULL, null=True)
    Madinah_hotel = models.ForeignKey(Hotel, verbose_name="Отель в Медине", related_name="madinah_hotel", on_delete=models.SET_NULL, null=True)
    transport = models.ForeignKey(Transport, verbose_name="Транспорт", on_delete=models.SET_NULL, null=True)
    order = models.PositiveIntegerField(verbose_name="Порядок", default=1)
    price = models.PositiveIntegerField(verbose_name="Цена", default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
        ordering = ["order"]
        

class TarifPricing(BaseModel):
    tarif = models.ForeignKey(Tarif, verbose_name="Тариф", on_delete=models.CASCADE,
                              related_name="prices")
    people_count = models.PositiveIntegerField(verbose_name="Количество человек")
    price = models.PositiveIntegerField(verbose_name="Цена")
    order = models.PositiveIntegerField(verbose_name="Порядок", default=1)
    
    def __str__(self):
        return f"{self.tarif.title} - {self.people_count} человек"
    
    class Meta:
        verbose_name = "Цена тарифа"
        verbose_name_plural = "Цены тарифов"
        ordering = ["order"]
    
    
class TarifService(BaseModel):
    tarif = models.ForeignKey(Tarif, verbose_name="Тариф", on_delete=models.CASCADE, related_name="services")
    service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(verbose_name="Порядок", default=1)
    
    def __str__(self):
        return f"{self.tarif.title} - {self.service.name}"
    
    class Meta:
        verbose_name = "Услуга тарифа"
        verbose_name_plural = "Услуги тарифов"
        ordering = ["order"]
        

class Application(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    month = models.CharField(max_length=255, verbose_name="Месяц")
    people_count = models.PositiveIntegerField(verbose_name="Количество человек")
    tarif = models.ForeignKey(Tarif, verbose_name="Тариф", on_delete=models.SET_NULL, null=True)

    
    def __str__(self):
        return f"{self.name} - {self.tarif.title}"
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]


class Slide(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = ResizedImageField(upload_to="slides", verbose_name="Изображение")
    order = models.PositiveIntegerField(verbose_name="Порядок", default=1)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ["order"]
