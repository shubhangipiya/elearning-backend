from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    list_filter = ('email', 'user_name', 'user_type', 'is_active')
    ordering = ('-email',)
    list_display = ('email', 'id', 'user_name', 'phone_number', 'user_type',
                    'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'user_type')}),
        ('Permissions', {'fields': ('is_active',)}),

    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'user_type', 'password1', 'password2', 'is_active')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
