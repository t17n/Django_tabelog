from django.contrib import admin
from .models import Shop, Member, Sales, Reservation, Review, Favorite
from django.utils.safestring import mark_safe

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'image_tag')
    #  'image', 'image_tag',
    
    def image_tag(self, obj):
        return mark_safe('<img src="/nagoyameshi{}" style="width:100px height:auto;">'.format(obj.image.url))
        # return mark_safe('<img src=f"/nagoyameshi{obj.image.url}" style="width:100px height:auto;">')
    
        
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_shop',)

admin.site.register(Shop, ShopAdmin)
admin.site.register(Member)
admin.site.register(Sales)
admin.site.register(Reservation)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite)