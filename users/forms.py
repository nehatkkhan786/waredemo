from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('email','age', 'is_premium')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('email','age','is_premium')