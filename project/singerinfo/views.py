from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
#Singer 모델에 대한 리스트 조회(GET)와 생성(POST)작업
def singer_list_create(request):

    if request.method == 'GET':
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        # 받은 데이터를 바탕으로 SingerSerializer 객체 생성
        serializer = SingerSerializer(data=request.data)
        # 직렬화된 데이터가 유효하면
        if serializer.is_valid(raise_exception=True):
            # 유효한 데이터 저장
            serializer.save()
            return Response(data=serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
# Singer 모델의 특정 객체에 대해 GET, PATCH, DELETE 작업을 수행하도록 처리.
def singer_detail_update_delete(request, singer_id):
    singer = get_object_or_404(Singer, id=singer_id)

    if request.method == 'GET':
        # 특정 Singer 객체 직렬화
        serializer = SingerSerializer(singer)
        # 직렬화된 데이터 Response로 반환
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SingerSerializer(instance=singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        request.delete()
        data = {
            'deleted_singer': singer_id
        }
        return Response(data)

@api_view(['GET', 'POST'])
# Song 모델에 대한 GET, POST 작업을 수행하는 API 엔드포인트 제공
def song_read_create(request, singer_id):
    singer = get_object_or_404(Singer, id=singer_id)

    if request.method == 'GET':
        songs = Song.objects.filter(singer=singer)
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(singer=singer)
        return Response(serializer.data)