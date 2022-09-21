from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField



# Create your models here.

STATUS = (
	('active','Active'),
	('deactive','Deactive')
)

GAME_TYPE = (
	('offline','Offline'),
	('online','Online')
)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class Game_Category(models.Model):
	name = models.CharField(max_length=150, verbose_name="Nomi")
	slug = AutoSlugField(populate_from='name')
	status = models.CharField(max_length=15, choices=STATUS, default='active', verbose_name="Holati")
	created_at = models.DateTimeField(auto_now=True)

	objects = models.Manager()
	active = ActiveManager()

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		ordering=('-created_at',)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('software:game_list_by_category', args=[self.slug])


class Software_Category(models.Model):
	name = models.CharField(max_length=150, verbose_name="Nomi")
	slug = AutoSlugField(populate_from='name')
	status = models.CharField(max_length=15, choices=STATUS, default='active', verbose_name="Holati")
	created_at = models.DateTimeField(auto_now=True)

	objects = models.Manager()
	active = ActiveManager()

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		ordering=('-created_at',)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('software:software_list_by_category', args=[self.slug])


class Platform(models.Model):
	name = models.CharField(max_length=150, verbose_name="Nomi")
	slug = AutoSlugField(populate_from='name')
	status = models.CharField(max_length=15, choices=STATUS, default='active', verbose_name="Holati")
	created_at = models.DateTimeField(auto_now=True)

	objects = models.Manager()
	active = ActiveManager()

	class Meta:
		ordering=('-created_at',)

	def __str__(self):
		return self.name


class Software(models.Model):
	platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name="Platforma")
	software_category = models.ForeignKey(Software_Category, on_delete=models.CASCADE, verbose_name="Kategorya")
	name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
	slug = AutoSlugField(populate_from='name')
	creator = models.CharField(max_length=200, verbose_name="Yaratuvchi")
	version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Versia")
	requarment = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tavsia qilingan sistema")
	size = models.CharField(max_length=50, verbose_name="Hajmi")
	about = models.TextField(verbose_name="Ilova haqida")
	screenshot = models.ImageField(upload_to='photos/software_photo/%Y/%m/%d/', blank=True, null=True, verbose_name="Skrinshot")
	file_64x = models.FileField(upload_to='files/software/64x/%Y/%m/%d/',blank=True, null=True, verbose_name="Ilova fayli(64x)")
	file_32x = models.FileField(upload_to='files/software/32x/%Y/%m/%d/',blank=True, null=True, verbose_name="Ilova fayli(32x)")
	seen_count = models.PositiveIntegerField(default=0, verbose_name="ko'rishlar soni")
	like_count = models.PositiveIntegerField(default=0, verbose_name="like lar soni")
	dislike_cont = models.PositiveIntegerField(default=0, verbose_name="dislike lar soni")
	download_count = models.PositiveIntegerField(default=0, verbose_name="yuklashlar soni")


	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan vaqti")

	# tags = TaggableManager()
	objects = models.Manager()
	active = ActiveManager()
	
	class Meta:
		ordering=('-created_at',)

	def get_tags(self):
		return self.tags.names()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('software:software_detail', args=[self.id, self.slug])
	

class SoftwarePhoto(models.Model):
	software = models.ForeignKey(Software, default=None, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Dastur")
	screenshot = models.ImageField(upload_to='photos/software_photo/%Y/%m/%d/', blank=True, null=True, verbose_name="Skrinshot")
	created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan vaqti")

	def __str__(self):
			return self.software.name

	class Meta:
		ordering=('-created_at',)


class Game(models.Model):
	platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name="Platforma")
	game_category = models.ForeignKey(Game_Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
	name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
	slug = AutoSlugField(populate_from='name', verbose_name="Slug")
	created_year = models.DateField(verbose_name="Yaratilgan vaqti")
	genre = models.CharField(max_length=30, verbose_name="Janri")
	creator = models.CharField(max_length=70, verbose_name="Yaratuvchi")
	interface_lang = models.CharField(max_length=100, blank=True, null=True, verbose_name="O'yin tili")
	voice_lang  = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ovoz tili")

	# minimum ---------------------------->
	system = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sistema")
	processor  = models.CharField(max_length=70, blank=True, null=True, verbose_name="Protsesor")
	ram = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tezkor hotira")
	video_card = models.CharField(max_length=50, blank=True, null=True, verbose_name="Video karta")
	hard_disk = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qattiq disk")
	# recommendet ------------------------>
	system_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sistema 2")
	processor_2  = models.CharField(max_length=70, blank=True, null=True, verbose_name="Protsesor 2")
	ram_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tezkor hotira 2")
	video_card_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Video karta 2")
	hard_disk_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qattiq disk 2")
	# ------------------------------------>
	
	trailer = models.FileField(upload_to="videos/game_trailer/%Y/%m/%d/", blank=True, null=True, verbose_name="Trailer videosi")
	screenshot = models.ImageField(upload_to='photos/game_photo/%Y/%m/%d/', blank=True, null=True, verbose_name="Skrinshot")
	size = models.CharField(max_length=50, verbose_name="Hajmi")
	file_64x = models.FileField(upload_to='files/game/64x/%Y/%m/%d/', blank=True, null=True, verbose_name="O'yin fayli(64x)")
	file_32x = models.FileField(upload_to='files/game/32x/%Y/%m/%d/', blank=True, null=True, verbose_name="O'yin fayli(32x)")
	about = models.TextField(verbose_name="O'yin haqida")
	installation = models.CharField(max_length=150, blank=True, null=True, verbose_name="O'rnatish")
	# tag = 
	website = models.CharField(max_length=200, blank=True, null=True, verbose_name="Websayt")
	game_type = models.CharField(max_length=20, choices=GAME_TYPE, verbose_name="O'yin turi") # offline/online
	version = models.CharField(max_length=20, verbose_name="Versia")
	
	seen_count = models.PositiveIntegerField(default=0, verbose_name="ko'rishlar soni")
	like_count = models.PositiveIntegerField(default=0, verbose_name="like lar soni")
	dislike_cont = models.PositiveIntegerField(default=0, verbose_name="dislike lar soni")
	download_count = models.PositiveIntegerField(default=0, verbose_name="yuklashlar soni")


	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan vaqti")

	# tags = TaggableManager()
	objects = models.Manager()
	active = ActiveManager()
	
	class Meta:
		ordering=('-created_at',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('software:game_detail', args=[self.id, self.slug])
	
	def total_likes(self):
		return self.likes.count()

	def total_views(self):		
		return self.views.count()


class GamePhoto(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True, verbose_name="O'yin")
	screenshot = models.ImageField(upload_to='photos/game_photo/%Y/%m/%d/', blank=True, null=True, verbose_name="Skrinshot")
	created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan vaqti")

	class Meta:
		ordering=('-created_at',)

	def __str__(self):
			return self.game.name


class Comment(models.Model):
	name = models.CharField(max_length=120, verbose_name="Ism familya")
	# email = models.EmailField(verbose_name="email manzil")
	software = models.ForeignKey(Software, on_delete=models.CASCADE, related_name="comments", verbose_name="Post")
	body = models.TextField(verbose_name="Izoh")
	created_at = models.DateTimeField(auto_now_add	 = True, verbose_name="Vaqti")
	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")

	objects = models.Manager()
	active = ActiveManager()

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		info = f"{self.name} - {self.software}"
		return info









