from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('file/', views.file, name='file'),
    path('text/', views.text, name='text'),
    path('compare/', views.compare, name='compare'),
    path('docs/', views.docs, name='docs'),
    path('text-test-result/', views.result, name='result'),
    path('file-test-result/', views.fileTestResult, name='fileTestResult'),
    path('text-similarity-analysis/', views.textSimilarityAnalysis, name='textSimilarityAnalysis'),
    path('file-similarity-analysis/', views.fileSimilarityAnalysis, name='twofilecompare1'),
    
]