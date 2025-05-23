from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from . models import Course
from . serializers import CourseSerializer
from rest_framework import generics,mixins
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


'''
class CourseList(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


class CourseList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    def get(self,request):
        return self.list(self.request)
    
    def post(self,request):
        return self.create(self.request)
    
class CourseDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    def get(self,request,pk):
        return self.retrieve(self.request,pk)
    
    def put(self,request,pk):
        return self.update(self.request,pk)

    def delete(self,request,pk):
        return self.destroy(self.request,pk)


class CourseList(APIView):
    def get(self,request):
        course=Course.objects.all()
        serializer=CourseSerializer(course,many=True)
        return Response(serializer.data) 
    
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk):
        course=self.get_object(pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    def put(self,request,pk):
        course=self.get_object(pk)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        course=self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''