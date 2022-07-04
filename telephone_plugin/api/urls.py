from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.APIRootView = views.TelephoneNetBoxPluginRootView

router.register(r'numbers', views.NumberViewSet)

app_name = "telephony_netbox_plugin-api"
urlpatterns = router.urls