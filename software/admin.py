from django.contrib import admin
from .models import Game, GamePhoto, Software, SoftwarePhoto, Game_Category, Platform, Software_Category, Comment

# Register your models here.

@admin.register(Game_Category)
class Game_Category_Admin(admin.ModelAdmin):
	list_display = ('name','status','created_at')
	

@admin.register(Software_Category)
class Software_Category_Admin(admin.ModelAdmin):
	list_display = ('name','status','created_at')


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
	list_display = ('name','status','created_at')
	


#--------------------------------------->
"""
Admin panelda ikkita modelning admin panelini birga ko'rsatrish uchun shablon
"""
class SoftwarePhotoAdmin(admin.StackedInline):
	model=SoftwarePhoto

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
	list_display = ('name','slug','platform','software_category','creator','version','size','created_at')
	list_filter = ('platform','software_category','status','created_at')
	search_fields = ('name','about')

	inlines = [SoftwarePhotoAdmin]

	class Meta:
		model = Software
#--------------------------------------->



class GamePhotoAdmin(admin.StackedInline):
	model = GamePhoto

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('name','platform','game_category','creator','version','size','game_type','status','created_at')
	list_filter = ('platform','game_category','status','created_at')
	search_fields = ('name','about')

	inlines = [GamePhotoAdmin]

	class Meta:
		model = Game


# @admin.register(Comment)
# class  CommentAdmin(admin.ModelAdmin):
# 	list_display = ('name','software','created_at','status')
# 	list_filter = ('created_at','status')
# 	search_fields = ('name', 'body', 'software')




