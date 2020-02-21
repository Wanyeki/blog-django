from django.urls import path
from . import views
app_name='message'
urlpatterns = [
    path('',views.ArticlesView.as_view(),name="articles"),
    path('add',views.add_article,name="add"),
    path('edit/<int:article_id>',views.edit_article,name="edit"),
    path('delete/<int:article_id>',views.delete_article,name="delete"),
    path('<int:article_id>',views.show,name="show"),
    path('<int:article_id>/comment',views.comment,name="comment"),
    path('<int:article_id>/edit/<int:comment_id>',views.edit_comment,name="edit_comment"),
    path('<int:article_id>/delete/<int:comment_id>',views.delete_comment,name="delete_comment"),
]
