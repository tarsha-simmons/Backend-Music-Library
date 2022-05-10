# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zr)d9j-*6fqz#m0q*(!4f0v7+mtke=zi=-6==&r-jpq)g9j5ca'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}

