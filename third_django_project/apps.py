from django.contrib.admin.apps import AdminConfig


class BookAdminConfig(AdminConfig):
    default_site = "third_django_project.admin.ThirdAppAdminSite"
