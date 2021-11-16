from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.CarsView.as_view()),
    path('Cars',views.CarListView.as_view()),
    path('Cars/<int:pk>',views.CarDetailView.as_view()),
    path('Carsupdate/<int:pk>',views.CarUpdateView.as_view()),
    path('Carsdelete/<int:pk>',views.CarDeleteView.as_view())
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
