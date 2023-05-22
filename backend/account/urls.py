from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = 'account'


urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),

    path('password-change/', include([
        path('',
             auth_views.PasswordChangeView.as_view(),
             name='password_change'),
        path('done/',
             auth_views.PasswordChangeDoneView.as_view(),
             name='password_change_done'),
    ])),

    path('password-reset/', include([
        path('',
             auth_views.PasswordResetView.as_view(),
             name='password_reset'),
        path('done/',
             auth_views.PasswordResetDoneView.as_view(),
             name='password_reset_done'),
    ])),
]