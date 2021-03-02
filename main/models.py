from django.db import models


class Product(models.Model):
    '''Модель продуктов'''

    CATEGORIES = (
        ('Laptops','Laptops'),
        ('Smarphones','Smarphones'),
    )    
    product_name = models.CharField(
        max_length=50,
        verbose_name='Название продукта'
    )

    price = models.IntegerField(
        verbose_name='Цена'
    )

    product_photo = models.ImageField(
        upload_to = ''
    )

    categorie = models.CharField(
        verbose_name='Категории',
        max_length=50,
        choices=CATEGORIES,default=CATEGORIES[0][0]
    )

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ('product_name',)

    def __str__(self):
        '''Описание объекта Feedback'''
        return f'{self.product_name}'
