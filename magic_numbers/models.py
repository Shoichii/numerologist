from django.db import models

# Create your models here.

class User(models.Model):
    telegram_id = models.BigIntegerField(verbose_name='Телеграм ID')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    seals = models.BigIntegerField(null=True, blank=True, verbose_name='Количество печатей')

    def __str__(self):
        return str(self.telegram_id)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class UserNumbers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    life_path_number = models.IntegerField(verbose_name='Число жизненного пути')
    birthday_number = models.IntegerField(verbose_name='Число дня рождения')
    expression_number = models.IntegerField(verbose_name='Число экспрессии')
    spirit_awake_number = models.IntegerField(verbose_name='Число духовного пробуждения')
    personality_number = models.IntegerField(verbose_name='Число личности')

    def __str__(self):
        return self.user.name
    
    class Meta:
        verbose_name = 'Число'
        verbose_name_plural = 'Числа'

class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_time = models.DateTimeField(verbose_name='Время и Дата')
    question = models.TextField(verbose_name='Вопрос', null=True, blank=True)
    answer = models.TextField(verbose_name='Ответ', null=True, blank=True)
    answer_pics = models.ManyToManyField('AnswerPic', verbose_name='Картинки ответа', blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

class AnswerPic(models.Model):
    pic_consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, verbose_name='Консультация')
    pic_id = models.TextField(verbose_name='Картинка')

    def __str__(self):
        return str(self.consultation)
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    action = models.TextField(verbose_name='Действие')
    money = models.IntegerField(verbose_name='Количество рублей')

    def __str__(self):
        return self.action
    
    class Meta:
        verbose_name = 'Действие'
        verbose_name_plural = 'Действия'