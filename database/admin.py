from django.contrib import admin

# REPO
from adminsortable2.admin import SortableAdminMixin
from .models import Monster, RepoItem, Dungeon, AttackMethod, ShopItem, MapInfo, LevelEffect, OrbDamage, LevelGuide


# 攻撃方法のインライン
class AttackMethodInline(admin.TabularInline):
    model = AttackMethod
    extra = 1

# モンスター管理
@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name', 'danger_level', 'hp', 'required_strength', 'show_attacks')
    inlines = [AttackMethodInline]

    def show_attacks(self, obj):
        return ", ".join([f"{a.name}({a.damage})" for a in obj.attacks.all()])
    show_attacks.short_description = '攻撃方法とダメージ'

# REPOアイテム管理
@admin.register(RepoItem)
class RepoItemAdmin(SortableAdminMixin, admin.ModelAdmin): 
    list_display = ('name', 'category', 'rating', 'effect')
    list_filter = ('category', 'rating')
    search_fields = ('name',)

# ショップアイテム管理
@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_text', 'category', 'available')
    list_filter = ('category', 'available')
    search_fields = ('name', 'description')

# ダンジョン管理
@admin.register(Dungeon)
class DungeonAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    filter_horizontal = ('monsters', 'reward_items')

@admin.register(MapInfo)
class MapInfoAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(LevelEffect)
class LevelEffectAdmin(admin.ModelAdmin):
    list_display = ("level_range",)
    search_fields = ("level_range", "details")

@admin.register(OrbDamage)
class OrbDamageAdmin(admin.ModelAdmin):
    list_display = ("tier", "damage")
    search_fields = ("tier",)

@admin.register(LevelGuide)
class LevelGuideAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'short_description')
    search_fields = ('name', 'description')
    readonly_fields = ('thumbnail',)
    list_display_links = ('name',)

    def thumbnail(self, obj):
        if obj.main_image: 
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px;" />',
                obj.main_image.url
            )
        return "画像なし"
    thumbnail.short_description = "画像"

    def short_description(self, obj):
        return (obj.description[:40] + '…') if obj.description else ""
    short_description.short_description = "説明"