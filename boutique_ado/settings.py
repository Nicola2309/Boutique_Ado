"""
Django settings for boutique_ado project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'so8j6v=erh99sfk46=dc0-09hr*3k5sz8qh2(peu$hk4q#nmdx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # These below are imported from
    # https://django-allauth.readthedocs.io/en/latest/installation.html

    # The contrib.sites app and the site _id setting we added Are used by
    # the social account app to create the proper callback URLs
    #  when connecting via social media accounts
    'django.contrib.sites',
    # This below is allauth itself
    'allauth',
    # This below allows the user to login with username and password
    'allauth.account',
    # This allows the user to login by social media accounts
    'allauth.socialaccount',
    'home',
    'products',
    'bag',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boutique_ado.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # required by allauth jimmy, it allows allauth-django
                # to access HTTP request object in our templates.
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bag.contexts.bag_contents',
            ],
        },
    },
]

# These below are imported from
# https://django-allauth.readthedocs.io/en/latest/installation.html
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`.
    # Allauth doesn't handle the superuser login so the function
    # gets deferred to django with this BACKEND function
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail.
    # Allows users to login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Since by default allauth will send confirmation emails to any new accounts
# we need to temporarily log those emails to the console so we can get
# the confirmation links.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

"""
The group of variables below is pasted from here
https://github.com/ckz8780/boutique_ado_v1/blob/ea7fe2688a0d97db4e469b672d5cb35e5835ff69/boutique_ado/settings.py
"""
# The account authentication method is what tells allauth that we want to allow
# authentication using either usernames or emails.
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# These three email settings below make it so that
# an email is required to register for the site,
# verifying your email is mandatory so we know users are using a real email,
# and they're gonna be required to enter their email twice
#  on the registration pageto make sure that they haven't made any typos.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# Minimum username length of 4 characters
ACCOUNT_USERNAME_MIN_LENGTH = 4
# specifying a login url to redirect after logging in,
# so this operation uses 2 variables, one for the login
# and one for the redirection to that login
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'boutique_ado.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
