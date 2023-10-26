from django.contrib import admin
from .models import Shop, Member, Sales, Reservation, Review, Favorite

admin.site.register(Shop)
admin.site.register(Member)
admin.site.register(Sales)
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Favorite)


