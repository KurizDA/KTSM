from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import VideoEmotionChartData, VideoQuestionData, LiveChatData
from rest_framework.views import APIView
from .serializers import VideoEmotionChartDataSerializer, VideoQuestionDataSerializer
from . import chat_json_maker
from . import time_pos_neg
from . import bot

class VideoEmotionChartDataListAPI(APIView):
    def get(self, request, request_video_id):
        queryset = VideoEmotionChartData.objects.filter(video_id=request_video_id)
        print(queryset)
        serializer = VideoEmotionChartDataSerializer(queryset, many=True)
        return Response(serializer.data)

class VideoQuestionDataListAPI(APIView):
    def get(self, request, request_video_id):
        queryset = VideoQuestionData.objects.filter(video_id=request_video_id)
        print(queryset)
        serializer = VideoQuestionDataSerializer(queryset, many=True)
        return Response(serializer.data)

class VideoDataMaker():
    def makeData(request, request_video_id):
        queryset = VideoEmotionChartData.objects.filter(video_id=request_video_id)
        if not queryset.exists():
            chat_json_maker.make_json(request_video_id)
            time_pos_neg.json_file_insert(request_video_id)
            return HttpResponse('data making success')
        else:
            return HttpResponse('exist data')
    
    def makeUserData(request, request_user_id):
        collector = bot.Bot()
        collector.run()
        returm HttpResponse('collector activated')



