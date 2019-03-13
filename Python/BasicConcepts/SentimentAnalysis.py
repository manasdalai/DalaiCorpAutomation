'''
import random

sentiment_data = 'this food teast good'
random.shuffle(sentiment_data)

# 80% for training
train_X, train_y = zip(*sentiment_data[:20000])

# Keep 20% for testing
test_X, test_y = zip(*sentiment_data[20000:])


print("Content-Type: text/plain")
print("")
print("Congratulations, it's a web app!")
'''

# urls.py (In stores app)
from django.conf.urls import url, include
from coffeehouse.stores import views as stores_views

urlpatterns = [
    url(r'^rest/$', stores_views.rest_store, name="rest_index"),
]

# views.py (In stores app)
from django.http import HttpResponse
from coffeehouse.stores.models import Store
import json


def rest_store(request):
    store_list = Store.objects.all()
    store_names = [{"name": store.name} for store in store_list]
    return HttpResponse(json.dumps(store_names), content_type='application/json')

# Sample output
# [{"name": "Corporate"}, {"name": "Downtown"}, {"name": "Uptown"}, {"name": "Midtown"}]
