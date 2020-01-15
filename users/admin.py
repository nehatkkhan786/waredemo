from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ('email','age', 'is_staff', 'is_premium', 'is_active',)
	list_filter = ('email','is_staff', 'is_premium', 'is_active',)
	fieldsets = (
		(None, {'fields':('email', 'is_premium', 'password',)}),
		('Permissions', {'fields':('is_staff', )}),

		)
	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields':('email','age', 'is_premium', 'password1', 'password2',  'is_active', 'is_staff')
			}),


		)
	search_fields = ('email', )
	ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)