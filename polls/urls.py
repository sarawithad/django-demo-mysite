from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]




# # notes:

# https://docs.djangoproject.com/en/1.11/intro/tutorial03/

# urls re-written to above url calls b/c models now take an argument. Current models:
 
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)




# Example:

# detail(request=<HttpRequest object>, question_id='34')

# The question_id='34' part comes from (?P<question_id>[0-9]+). Using parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the view function; ?P<question_id> defines the name that will be used to identify the matched pattern; and [0-9]+ is a regular expression to match a sequence of digits (i.e., a number).



# Note that the name of the matched pattern in the regexes of the second and third patterns has changed from <question_id> to <pk>.

# app_name = 'polls'
# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]



# Django generic views = IndexView, DetailView



# Original urls content:

# from django.conf.urls import include, url
# from django.contrib import admin

#     url(r'^$', views.index, name='index'),
# ]

# urlpatterns = [
#     url(r'^polls/', include('polls.urls')),
#     url(r'^admin/', admin.site.urls),
# ]


# The include() function allows referencing other URLconfs. Note that the regular expressions for the include() function doesn’t have a $ (end-of-string match character) but rather a trailing slash. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

# The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.