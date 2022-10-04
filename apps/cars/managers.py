from django.db.models import Manager


class CarManager(Manager):
    def get_by_price_gt(self, price: int):
        return self.filter(price__gt=price)
