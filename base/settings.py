from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRETS_DIR = BASE_DIR / ".secrets"

with open(SECRETS_DIR / ".django_secret_key") as f:
    SECRET_KEY = f.read().strip()

DEBUG = True

ALLOWED_HOSTS = ["localhost"]


INSTALLED_APPS = [
    # core django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # third party packages
    "django_registration",
    "crispy_forms",
    # user defined apps
    "apps.accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "base.urls"

CRISPY_TEMPLATE_PACK = "bootstrap4"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "base.wsgi.application"


with open(SECRETS_DIR / ".db_user") as f:
    DB_USER = f.read().strip()

with open(SECRETS_DIR / ".db_pass") as f:
    DB_PASS = f.read().strip()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "demo_auth_lite",
        "USER": f"{DB_USER}",
        "PASSWORD": f"{DB_PASS}",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGIN_URL = "login"

LOGOUT_REDIRECT_URL = "login"

LOGIN_REDIRECT_URL = "home"

LANGUAGE_CODE = "en-IN"

TIME_ZONE = "Asia/Calcutta"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

SITE_ID = 1

ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.blabber.xyz"
EMAIL_PORT = 465
EMAIL_USE_SSL = True

EMAIL_HOST_USER = "admin@blabber.xyz"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
with open(SECRETS_DIR / ".email_provider_pass") as f:
    EMAIL_HOST_PASSWORD = f.read().strip()


AUTH_USER_MODEL = "accounts.User"
