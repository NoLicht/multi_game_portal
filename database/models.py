from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='games/', blank=True, null=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    description = models.TextField(blank=True)

class Character(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=(('hero','勇者'),('monster','モンスター')))
    hp = models.IntegerField()
    mp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    skill = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image_hd2d = models.ImageField(upload_to='characters/hd2d/', blank=True, null=True)
    favorited_by = models.ManyToManyField(User, blank=True, related_name='favorite_characters')

class Item(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    effect = models.TextField(blank=True)
    image_hd2d = models.ImageField(upload_to='items/hd2d/', blank=True, null=True)
    favorited_by = models.ManyToManyField(User, blank=True, related_name='favorite_items')

class Dungeon(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='dungeons')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    monsters = models.ManyToManyField(Character, blank=True)
    reward_items = models.ManyToManyField(Item, blank=True)
    map_image = models.ImageField(upload_to='dungeons/hd2d/', blank=True, null=True)
    hints = models.TextField(blank=True)
    favorited_by = models.ManyToManyField(User, blank=True, related_name='favorite_dungeons')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page_id = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



# REPO
class Monster(models.Model):
    name = models.CharField(max_length=100)
    DANGER_CHOICES=(
        ('☆☆☆', '☆☆☆'),
        ('★☆☆', '★☆☆'),
        ('★★☆', '★★☆'),
        ('★★★', '★★★'),
    )
    danger_level = models.CharField(
        max_length=3,
        choices=DANGER_CHOICES,
        default='☆☆☆',
        verbose_name='危険度'
    )
    hp = models.IntegerField()
    required_strength = models.CharField(
        max_length=50,
        verbose_name='必要筋力',
        blank=True,
        null=True)
    strategy = models.TextField(verbose_name='対処方法',blank=True, null=True)
    image = models.ImageField(upload_to='monsters/', blank=True, null=True)

    def __str__(self):
        return self.name

class AttackMethod(models.Model):
    monster = models.ForeignKey(Monster, related_name="attacks", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="攻撃名")
    damage = models.CharField(
        max_length=50,
        verbose_name="ダメージ",
        blank=True,  
        null=True
    )

    def __str__(self):
        return f"{self.name}: {self.damage or '未設定'}"

    
class RepoItem(models.Model):
    CATEGORY_CHOICES = (
        ('melee', '近接武器'),
        ('ranged', '遠距離武器'),
        ('throw', '投擲武器'),
        ('trap', '設置武器'),
        ('treasure', '貴重品'),
    )
    RATING_CHOICES = (
        ('☆☆☆', '☆☆☆'),
        ('★☆☆', '★☆☆'),
        ('★★☆', '★★☆'),
        ('★★★', '★★★'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    rating = models.CharField(max_length=3, choices=RATING_CHOICES)
    effect = models.TextField()
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)  # ←並び順用
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name
    
class ShopItem(models.Model):
    CATEGORY_CHOICES = [
        ('upgrade', 'アップグレードパック'),
        ('heal', '回復パック'),
        ('drone', 'ドローン'),
        ('other', 'その他'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='shop_items/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def price_text(self):
        return f"{self.min_price // 1000}k ~ {self.max_price // 1000}k"

class LevelGuide(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    main_image = models.ImageField(upload_to='level_images/', blank=True, null=True)
    sub_image1 = models.ImageField(upload_to='level_images/', blank=True, null=True)
    sub_image2 = models.ImageField(upload_to='level_images/', blank=True, null=True)

    def str(self):
        return self.name

class MapInfo(models.Model):
    title = models.CharField(max_length=100, default="MAP概要")
    description = models.TextField()

    def __str__(self):
        return self.title

class LevelEffect(models.Model):
    level_range = models.CharField(max_length=50)  
    details = models.TextField()

    def __str__(self):
        return self.level_range

class OrbDamage(models.Model):
    tier = models.CharField(max_length=20)  
    damage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tier} - {self.damage}ダメージ"