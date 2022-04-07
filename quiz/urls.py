from django.conf.urls import url
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, job_category
from django.urls import path



urlpatterns = [ 
    path('', view=index, name='index'),    
    path('quizzes/',view=QuizListView.as_view(),name='quiz_index'),
    path('category/',view=CategoriesListView.as_view(),name='quiz_category_list_all'),
    path('category/(?P<category_name>[\w|\W-]+)/',view=ViewQuizListByCategory.as_view(),name='quiz_category_list_matching'),
    path('progress/',view=QuizUserProgressView.as_view(), name='quiz_progress'),
    path('marking/',view=QuizMarkingList.as_view(),name='quiz_marking'),
    path('marking/(?P<pk>[\d.]+)/',view=QuizMarkingDetail.as_view(),name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
    path('(?P<slug>[\w-]+)/', view=QuizDetailView.as_view(),name='quiz_start_page'),
    path('(?P<quiz_name>[\w-]+)/take/',view=QuizTake.as_view(),name='quiz_question'),
    path("job-cat/<str:category>/", job_category, name="job-category"),

]