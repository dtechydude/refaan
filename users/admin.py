from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin


#because we used abstract user configuration we must do all this
#class UserAdminConfig(UserAdmin):
   # list_display = ('username', 'email', 'first_name', 'is_active', 'is_staff')

   # fieldsets = (
   #     ('Credential', {'fields': ('username', 'email', 'first_name', 'last_name')}),
   #     ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups')}),
   #     ('Personal', {'fields':('gender', 'state', 'trade', 'date_joined', 'last_login')}),
   # )

   # add_fieldsets = (
   #     (None, {
   #         'classes': ('wide',),
    #        'fields' : ('username', 'email', 'first_name', 'last_name', 'gender', 'state', 'trade', 'password1', 'password2', 'is_active', 'is_staff')}
    #    ),
   # )


#admin.site.register(User, UserAdminConfig)



class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    #fields =
    list_display = ('user', 'phone', 'gender', 'country', 'trade')
    list_filter =  ['country']
    search_fields = ['question_text']

admin.site.register(Profile, ProfileAdmin)





#Customizing the Admin title and headings
admin.site.site_header= 'REFAAN ADMIN AREA'
admin.site.site_title= 'REFAAN MEMBERSHIP PORTAL'
admin.site.index_title= 'Welcome to Refaan admin portal'
