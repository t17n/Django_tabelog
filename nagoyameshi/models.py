from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser



SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

WEEKDAY_CHOICES = [
    ('月曜日', '月曜日'),
    ('火曜日', '火曜日'),
    ('水曜日', '水曜日'),
    ('木曜日', '木曜日'),
    ('金曜日', '金曜日'),
    ('土曜日', '土曜日'),
    ('日曜日', '日曜日'),
    ('祝日', '祝日'),
    ('無休', '無休'),
]

class Condition(models.Model):
    kodawari = models.CharField(verbose_name="こだわり条件", max_length=50,)
    def __str__(self):
        return(self.kodawari)
    
class Genre(models.Model):
    genre = models.CharField(verbose_name="ジャンル", max_length=50,)
    def __str__(self):
        return(self.genre)

class DayOfWeek(models.Model):
    day_of_week = models.CharField(verbose_name="店休日", max_length=50,)
    def __str__(self):
        return(self.day_of_week)
    
# 店舗モデル
class Shop(models.Model):
    '''
    GENRE_CHOICES = [
        ('和食', '和食'),
        ('洋食', '洋食'),
        ('魚介', '魚介'),
        ('ピザ・パスタ', 'ピザ・パスタ'),
        ('カレー', 'カレー'),
    ]
    '''
    name = models.CharField(verbose_name="店名", max_length=50)
    image = models.ImageField(verbose_name="写真", blank=True, default="media_local/noImage.png", upload_to="media_local")
    phonenumber = PhoneNumberField(verbose_name="電話番号", region='JP', default="01-2345-6789")
    address = models.CharField(verbose_name="住所", max_length=100, default="名古屋市")
    access = models.CharField(verbose_name="アクセス", max_length=100, default="徒歩5分")
    neareststation = models.CharField(verbose_name="最寄駅", max_length=50, default="名古屋駅")
    condition = models.ManyToManyField("Condition", verbose_name="こだわり条件")
    openingdate = models.DateField(verbose_name="開業日", default="1990-11-11")
    seats = models.PositiveIntegerField(verbose_name="席数", default="20")
    opening_time = models.TimeField(verbose_name="開店時間", default="7:00")
    closing_time = models.TimeField(verbose_name="閉店時間", default="22:00")
    day_of_week = models.ManyToManyField("DayOfWeek", verbose_name="定休日")
    budget_min = models.PositiveIntegerField(verbose_name="予算(安)", default="1000")
    budget_max = models.PositiveIntegerField(verbose_name="予算(高)", default="10000")
    genre = models.ManyToManyField("Genre", verbose_name="ジャンル")
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return(self.name)


# 会員モデル
class Member(AbstractUser):
    # paid = models.BooleanField(verbose_name="有料会員",)
    name = models.CharField(verbose_name="名前", max_length=50,)
    email = models.EmailField(verbose_name="email", max_length=50,)
    password = models.CharField(verbose_name="パスワード", max_length=128)
    
    # クレジットカード情報
    cardholder_name = models.CharField(verbose_name="クレジットカード登録名", max_length=100, blank=True, null=True) 
    card_number = models.CharField(verbose_name="カード番号", max_length=16, blank=True, null=True)  # 仮の設定。実際には暗号化が必要です
    expiration_date = models.DateField(verbose_name="有効期限", blank=True, null=True, )
    cvv = models.CharField(verbose_name="cvv", max_length=4, blank=True, null=True)  # 仮の設定。実際には暗号化が必要です

    # favorite_shop = models.CharField(verbose_name="お気に入り", max_length=50, blank=True, null=True)
    # review_shop = models.CharField(verbose_name="レビューした店舗", max_length=50, blank=True, null=True)
    # m_review = models.TextField(verbose_name="レビュー", blank=True, null=True)
    # reservedshop = models.CharField(verbose_name="予約店舗", max_length=50, blank=True, null=True)
    
    created_at = models.DateField(auto_now_add = True, null=True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return str(self.name)
    


    

# 売上モデル
class Sales(models.Model):
    members = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name="有料会員",)
    money = models.PositiveIntegerField(verbose_name="売上", default="300")

    def __str__(self):
        return str(self.members.name)


# 予約モデル
class Reservation(models.Model):
    reserve_shop = models.ForeignKey(Shop, on_delete=models.PROTECT, verbose_name="店舗")
    res_customer = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name="予約者")
    # name = models.CharField(max_length=50) 
    day = models.DateTimeField(verbose_name="予約日時")
    numpeople = models.IntegerField(verbose_name="予約人数")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.reserve_shop.name)
    
    def __str__(self):
        return str(self.res_customer.name)


# レビューモデル
class Review(models.Model):
    review_shop = models.ForeignKey("Shop", on_delete=models.CASCADE, related_name="reviews", verbose_name="店舗")
    photo = models.ImageField(verbose_name="写真", blank=True, null=True)
    review_member = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name="レビュー者")
    score = models.PositiveSmallIntegerField(verbose_name="レビュースコア", choices=SCORE_CHOICES, default=3)
    comment = models.TextField(verbose_name="コメント")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.review_shop.name)

# お気に入りモデル
class Favorite(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, verbose_name="店舗")
    customer = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name="登録者")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.customer)