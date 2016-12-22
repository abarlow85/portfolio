from django.contrib import admin
from .models import AboutMe, PortfolioApp, Skill, SkillCategory, SocialLink

# Register your models here.

admin.site.site_header = 'Alec\'s Portfolio Content Manager'
admin.site.site_title = 'Portfolio Content Manager | Alec Barlow'
admin.site.index_title = ''

admin.site.disable_action('delete_selected')

class AboutMeAdmin(admin.ModelAdmin):

	def get_readonly_fields(self, request, obj):
		return [] if request.user.is_superuser else [field.name for field in self.model._meta.fields]
	def has_add_permission(self, request):
		return True if request.user.is_superuser else False
	def has_delete_permission(self, request, obj=None):
		return True if request.user.is_superuser else False

class SocialLinkAdmin(admin.ModelAdmin):

	def get_readonly_fields(self, request, obj):
		return [] if request.user.is_superuser else [field.name for field in self.model._meta.fields]
	def has_add_permission(self, request):
		return True if request.user.is_superuser else False
	def has_delete_permission(self, request, obj=None):
		return True if request.user.is_superuser else False


class SkillCategoryAdmin(admin.ModelAdmin):

	def get_readonly_fields(self, request, obj):
		return [] if request.user.is_superuser else [field.name for field in self.model._meta.fields]
	def has_add_permission(self, request):
		return True if request.user.is_superuser else False
	def has_delete_permission(self, request, obj=None):
		return True if request.user.is_superuser else False



class SkillAdmin(admin.ModelAdmin):

	list_display = ('text', 'category')

	def get_readonly_fields(self, request, obj):
		return [] if request.user.is_superuser else [field.name for field in self.model._meta.fields]
	def has_add_permission(self, request):
		return True if request.user.is_superuser else False
	def has_delete_permission(self, request, obj=None):
		return True if request.user.is_superuser else False

class PortfolioAppAdmin(admin.ModelAdmin):

	list_display = ('title', 'rank')

	def has_add_permission(self, request):
		return True if request.user.is_superuser else False
	def has_delete_permission(self, request, obj=None):
		return True if request.user.is_superuser else False
	def get_readonly_fields(self, request, obj):
		return [] if request.user.is_superuser else [field.name for field in self.model._meta.fields]

	
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(PortfolioApp, PortfolioAppAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)

