from django.contrib import admin
from .models import Shop, Member, Sales, Reservation, Review, Favorite, Condition
from django.utils.safestring import mark_safe

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'image')
    #  'image', 'image_tag',
    
    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))
        # return mark_safe('<img src=f"{obj.image.url}" style="width:100px height:auto;">')
    
        
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_shop',)

admin.site.register(Shop, ShopAdmin)
admin.site.register(Member)
admin.site.register(Sales)
admin.site.register(Reservation)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite)
admin.site.register(Condition)