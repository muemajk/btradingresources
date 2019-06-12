from btresources.settings.common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =os.environ['SECRET_KEY']

#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '!we0ag^yw*a)3(!vqq3iab%s5enj1#plikv2qo8cp(tzi891ve')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'


ALLOWED_HOSTS = ['75.98.169.74']

