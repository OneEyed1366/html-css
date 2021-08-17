from django import forms
from auth_app.models import User
from auth_app.forms import UserEditForm

class UserAdminEditForm(UserEditForm):
    class Meta:
        model = User
        fields = '__all__'
