# from django.urls import path
# from .views import (
#     CategoryListView,
#     CategoryDetailView,
#     ProductListView,
#     ProductDetailView,
#     ProductReviewsView,
#     ReviewListView,
#     ReviewDetailView,
#     CategoryViewSet,
#     ProductViewSet,
#     ReviewViewSet
# )
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('categories', CategoryViewSet)
# router.register('products', ProductViewSet)
# router.register('reviews', ReviewViewSet)

# urlpatterns = [
#     path('categories/', CategoryListView.as_view()),
#     path('categories/<int:pk>/', CategoryDetailView.as_view()),

#     path('products/', ProductListView.as_view()),
#     path('products/<int:pk>/', ProductDetailView.as_view()),
#     path('products/reviews/', ProductReviewsView.as_view()),

#     path('reviews/', ReviewListView.as_view()),
#     path('reviews/<int:pk>/', ReviewDetailView.as_view()),
# ]

from django.urls import path

urlpatterns = [
    path('api/v1/posts/', PostListCreateView.as_view()),
    path('api/v1/posts/<int:pk>/', PostDetailView.as_view()),
    path('api/v1/posts/<int:id>/comments/', CommentListView.as_view()),
    path('api/v1/posts/<int:id>/comments/create/', CommentCreateView.as_view()),
]