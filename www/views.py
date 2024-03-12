from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from www.models import Direction, Site, SiteLog
from www.serializers import DirectionSerializers, SiteSerializer, SiteLogMainSerializer


class DirectionView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers


class SiteListView(generics.ListAPIView):
    queryset = Site.objects.all().prefetch_related('logs', 'types')
    serializer_class = SiteSerializer = SiteSerializer


class SiteLogRetrieveAPIView(generics.GenericAPIView):
    queryset = SiteLog.objects.all()
    serializer_class = SiteLogMainSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.update_visitor_count()
        return Response(serializer.data)

