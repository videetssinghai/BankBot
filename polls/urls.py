from django.conf.urls import url

from . import views

#url(r'^chat/$', views.chatApp, name='chatApp'),

urlpatterns = [

    url(r'^chatbotResponse/', views.chatbotResponse),
    url(r'^chatbot/', views.chatApp),
    url(r'^signup/', views.signup),

]
