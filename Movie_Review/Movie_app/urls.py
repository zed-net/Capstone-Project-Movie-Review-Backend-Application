from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet,)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'all-movies', views.AllMoviesViewSet, basename='AllMovies')

def root_info(request):
    return JsonResponse({
        "message": "Welcome to the Movie Review API",
        "login_url": "/api/login/",
        "register_url": "/api/signup/",
        "movies_url": "/api/movies/",
        "reviews_url": "/api/reviews/",
        "all_movies_url": "/api/all-movies/",
    })


urlpatterns = [
    path('', root_info,name='root'),   # root goes to login
    path('api/', include(router.urls)),
    path("api/signup/", RegisterView.as_view(), name="signup"),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
]
