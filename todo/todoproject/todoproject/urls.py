
from django.contrib import path, include
from . import views
from views import authView, CustomLoginView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", views.index),

    path("index", views.index),

    path('blogs/', views.blogs, name='blogs'),

    path('accounts/signup', authView, name="authView"),

    path("accounts/", include ("django.contrib.auth.urls")),

    path('login/', CustomLoginView.as_view(), name='login'),

    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('add-todoList/', views.addTodoList, name='add_TodoList'),

    path('urgency-categories', views.urgencyCategories, name='urgency_Categories'),

    path('categories-List/', views.categories, name='categories'),

    path('categories/edit/<int:pk>/', views.edit_category name='edit_category'),

    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),

    path('create-personal-info/', create_personal_info, name='create_personal_info'),

    path('profile/', views.profile_view, name='profile_view'),

    path/'user/<int:user_id>/', views.user_detail, name='user_detail'

    path('edit_personal_info/<int:user_id>/, views.edit_personal_info, name='edit_personal_info'),)
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)