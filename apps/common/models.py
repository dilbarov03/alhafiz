from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст новости")
    image = models.ImageField(upload_to="news", verbose_name="Изображение")
    
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



        
    
    
