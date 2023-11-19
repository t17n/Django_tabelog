from django.db import models
from phonenumber_field.modelfields import PhoneNumberField




SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

WEEKDAY_CHOICES = [
    (0, '月曜日'),
    (1, '火曜日'),
    (2, '水曜日'),
    (3, '木曜日'),
    (4, '金曜日'),
    (5, '土曜日'),
    (6, '日曜日'),
    (7, '祝日'),
    (8, '無休'),
]



# 店舗モデル
class Shop(models.Model):
    GENRE_CHOICES = [
        ('和食', '和食'),
        ('洋食', '洋食'),
        ('魚介', '魚介'),
        ('ピザ・パスタ', 'ピザ・パスタ'),
        ('カレー', 'カレー'),     
    ]
    CONDITIONS = [
        ('ベジタリアン', 'ベジタリアン'),
        ('ビーガン', 'ビーガン'),
        ('日本酒', '日本酒'),
        ('個室', '個室'),
        ('座敷', '座敷'),
        ('掘りごたつ', '掘りごたつ'),
        ('食べ放題', '食べ放題'),
        ('飲み放題', '飲み放題'),
        ('駐車場', '駐車場'),
    ]
    name = models.CharField(verbose_name="店名", max_length=50)
    photo = models.ImageField(verbose_name="写真", blank=True, null=True)
    phonenumber = PhoneNumberField(verbose_name="電話番号", region='JP')
    address = models.CharField(verbose_name="住所", max_length=100)
    access = models.CharField(verbose_name="アクセス", max_length=100)
    neareststation = models.CharField(verbose_name="最寄駅", max_length=50)
    shop_reservation = models.BooleanField(verbose_name="予約可")
    privateroom = models.BooleanField(verbose_name="個室有")
    nosmoking = models.BooleanField(verbose_name="禁煙")
    smokingbooth = models.BooleanField(verbose_name="喫煙ブース有")
    condition = models.CharField(verbose_name="こだわり条件", blank=True, max_length=50, choices=CONDITIONS)
    openingdate = models.DateField(verbose_name="開業日")
    seats = models.PositiveIntegerField(verbose_name="席数")
    opening_time = models.TimeField(verbose_name="開店時間")
    closing_time = models.TimeField(verbose_name="閉店時間")
    day_of_week = models.IntegerField(verbose_name="店休日", choices=WEEKDAY_CHOICES)
    sns = models.URLField(max_length=100, blank=True, null=True)
    shop_review = models.CharField(verbose_name="レビュー", max_length=100, blank=True, null=True)
    budget = models.PositiveIntegerField(verbose_name="予算(円)")
    genre = models.CharField(verbose_name="ジャンル", max_length=20, choices=GENRE_CHOICES)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.name



# 会員モデル
class Member(models.Model):
    paid = models.BooleanField(verbose_name="有料会員", null=False)
    name = models.CharField(verbose_name="名前", max_length=50)
    email = models.EmailField(verbose_name="email", max_length=50)
    password = models.CharField(verbose_name="パスワード", max_length=10)
    
    # クレジットカード情報
    cardholder_name = models.CharField(verbose_name="クレジットカード登録名", max_length=100, blank=True, null=True) 
    card_number = models.CharField(verbose_name="カード番号", max_length=16, blank=True, null=True)  # 仮の設定。実際には暗号化が必要です
    expiration_date = models.DateField(verbose_name="有効期限", blank=True, null=True, )
    cvv = models.CharField(verbose_name="パスワード", max_length=4, blank=True, null=True)  # 仮の設定。実際には暗号化が必要です

    favorite_shop = models.CharField(verbose_name="お気に入り", max_length=50, blank=True, null=True)
    review_shop = models.CharField(verbose_name="レビューした店舗", max_length=50, blank=True, null=True)
    m_review = models.TextField(verbose_name="レビュー", blank=True, null=True)
    reservedshop = models.CharField(verbose_name="予約店舗", max_length=50, blank=True, null=True)
    
    created_at = models.DateField(auto_now_add = True, null=True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.name

    

# 売上モデル
class Sales(models.Model):
    members = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name='有料会員')
    money = models.PositiveIntegerField(verbose_name="売上")

    def __str__(self):
        return self.members.name


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
        return self.reserve_shop.name
    
    def __str__(self):
        return self.res_customer.name


# レビューモデル
class Review(models.Model):
    review_shop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name="店舗")
    photo = models.ImageField(verbose_name="写真", blank=True, null=True)
    review_member = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name="レビュー者")
    # reviewer_name = models.CharField(max_length=50)
    # review_shopname = models.CharField(max_length=50)
    score = models.PositiveSmallIntegerField(verbose_name="レビュースコア", choices=SCORE_CHOICES, default=3)
    comment = models.TextField(verbose_name="コメント")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.review_shop.name

# お気に入りモデル
class Favorite(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, verbose_name="店舗")
    customer = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name="登録者")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.shop