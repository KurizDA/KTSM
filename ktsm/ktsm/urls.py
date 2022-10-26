from django.contrib import admin
from django.urls import path
from review.views import VideoEmotionChartDataListAPI, VideoQuestionDataListAPI, VideoDataMaker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/make_data/<int:request_video_id>/', VideoDataMaker.makeData),
    path('review/make_user_data/<string:request_user_id>/', VideoDataMaker.make_user_data),
    path('review/emotion_chart_data/<int:request_video_id>/', VideoEmotionChartDataListAPI.as_view(), name="result01"),
    path('review/question_data/<int:request_video_id>/', VideoQuestionDataListAPI.as_view())
]
