from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^chatbotResponse/', views.chatbotResponse),
    url(r'^chatbot/', views.chatApp),
    url(r'^signup/', views.Registration.as_view()),
    url(r'^login/', views.login_page.as_view()),
    url(r'^logout/', views.logout_page),
    url(r'^Home/', views.Home),

]
