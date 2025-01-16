from django.urls import path, include

urlpatterns = [
    path('snippets/', include('snippets.urls')),
    path('users/', include('users.urls')),
]