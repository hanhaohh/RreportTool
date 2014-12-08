import sys, os
sys.path.append('/home/jasonhao/lib/python')
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "recengine.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
