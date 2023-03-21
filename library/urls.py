from django.urls import path
from . import views
app_name='library'
urlpatterns=[
    path('',views.index , name='index'),
    path('books/', views.BookListView.as_view(),name='books'),
    path('books/<int:id>/', views.detail, name='book-detail'),
    path('author/<int:id>/',views.author_list, name='author'),
]