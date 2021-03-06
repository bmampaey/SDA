from django.contrib import admin
from web_account.models import User


class FirstLetterListFilter(admin.SimpleListFilter):
	title = 'First letter'
	
	# Parameter for the filter that will be used in the URL query.
	parameter_name = 'email'
	
	def lookups(self, request, model_admin):
		'''List the first letter of existing users email adresses'''
		qs = model_admin.get_queryset(request)
		return set((obj.email[0].upper(), obj.email[0].upper()) for obj in qs)

	def queryset(self, request, queryset):
		if self.value() is not None:
			return queryset.filter(email__istartswith=self.value())
		else:
			return queryset

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	'''Admin class for the web account User model'''
	list_display = ['email', 'name', 'last_login']
	list_filter = [FirstLetterListFilter]
