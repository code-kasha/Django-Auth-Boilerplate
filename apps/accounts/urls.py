from django.urls import path


from apps.accounts import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("", views.UserHome.as_view(), name="home"),
    path("register/", views.Register.as_view(), name="register"),
    path("register/complete/", views.RegisterComplete.as_view(), name="django_registration_complete"),
    path("register/closed/", views.RegisterClosed.as_view(), name="django_registration_disallowed"),
    path(
        "activation/<str:activation_key>/",
        views.ActivateUser.as_view(),
        name="django_registration_activate",
    ),
    path(
        "activate/complete/",
        views.ActivationComplete.as_view(),
        name="django_registration_activation_complete",
    ),
    path(
        "change_password/",
        views.ChangePassword.as_view(),
        name="change_password",
    ),
    path("reset_password/", views.ResetPassword.as_view(), name="reset_password"),
    path("reset_password_sent/", views.ResetPasswordDone.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.ResetPasswordConfirm.as_view(), name="password_reset_confirm"),
    path("reset_password_complete", views.ResetPasswordComplete.as_view(), name="password_reset_complete"),
]
