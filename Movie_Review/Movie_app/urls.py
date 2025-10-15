from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from django.http import JsonResponse


router = DefaultRouter()
router.register(r'Add_movies', views.MovieViewSet,)
router.register(r'Reviews', views.ReviewViewSet)
router.register(r'Available_movies', views.AllMoviesViewSet, basename='AllMovies')

def root_info(request):
    return JsonResponse({
        "message": "Welcome to my Movie Review API",
        "Api home": "/api/",
        "New_users can_register_at": "/api/signup/",
        "Add_movies_url": "/api/Add_movies/",
        "Reviews_url": "/api/Reviews/",
        "Available_movies_url": "/api/all-movies/",
    })


urlpatterns = [
    path('', root_info,name='root'),   # root goes to login
    path('api/', include(router.urls)),
    path("api/signup/", RegisterView.as_view(), name="signup"),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    
]
