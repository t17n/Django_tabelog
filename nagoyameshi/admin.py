from django.contrib import admin
from .models import Shop, Reservation, Sales, Review, Favorite, Condition, Genre, Member, DayOfWeek
from django.utils.safestring import mark_safe


# adminカスタマイズ
from django.contrib.auth.admin import UserAdmin

@admin.register(Member)
class MemberAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("name", "email", "password")})
    )



class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    
    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))
    
        
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_shop',)

admin.site.register(Shop, ShopAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Sales)
admin.site.register(Reservation)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite)
admin.site.register(Condition)
admin.site.register(Genre)
admin.site.register(DayOfWeek)