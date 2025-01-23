from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from pos_app.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pos_app.urls')),  # Include API endpoints from pos_app
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Correct usage
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Correct usage
    path('', home, name='home'),  # Add a home route
]
