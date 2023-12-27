from django.db import models

action = [
    {'id': 1, 'action_name': 'Специальная цена на набор при лечении спазмов!', 'date_action': 'C 15 по 20 ноября 2023 года', 'criterion': 'Закажите набор для лечения спазмов на нашем сайте и получите скидку 25% на весь набор!'},
    {'id': 2, 'action_name': 'Выгодная покупка!', 'date_action': 'С 1 до 7 января 2023 года', 'criterion': 'Преобретите покупку на 1000 рублей и получите купон на покупку "Мульти комплекс витамины группы В"'},
    {'id': 3, 'action_name': 'Красота и уход за собой', 'date_action': 'С 1 декабря 2023 по 31 января 2024', 'criterion': 'Активная косметика с выгодой до 50% только у нас!'},
    {'id': 4, 'action_name': 'Розыгрыш богатств!', 'date_action': 'С 10 января по 20 февраля 2024', 'criterion': 'Участвуй в розыгрыше набора средств для красоты, сканируя чеки покупок в нашей аптеке!'},
]

class action(models.Model):
    action_name = models.CharField(max_length=60)
    date_action = models.CharField(max_length=60)
    criterion = models.CharField(max_length=100)

    def __str__(self):
        return self.action_name


partners = [
    {'id': 1, 'patners_name': 'ЗдравCити', 'organization': 'ЗАО фирма "Центр внедрения "ПРОТЕК"','rating': 4.9},
    {'id': 2, 'patners_name': 'Планета Здоровья', 'organization': 'ООО "Аптека Сервис Плюс"','rating': 4.7},
    {'id': 3, 'patners_name': 'Аптека Апрель', 'organization': 'ООО ФК Апрель','rating': 4.1},
    {'id': 4, 'patners_name': 'Аптека Вита', 'organization': 'ООО "Рона"','rating': 4.3},
    {'id': 5, 'patners_name': 'Здесь Аптека', 'organization': 'ООО "Здравсервис"','rating': 4.5},
]

class partners(models.Model):
    patners_name = models.CharField(max_length=30)
    rating = models.FloatField()
    organization = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")

    def __str__(self):
        return self.patners_name
