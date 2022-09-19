from django.contrib import admin


class ThirdAppAdminSite(admin.AdminSite):
    site_title = "ThirdApp Admin Site"
    site_header = "Welcome to the ThirdApp Amin Interface"
    index_title = "ThirdApp index"
