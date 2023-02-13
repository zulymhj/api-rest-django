import logging
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from shop.serializers.input import OrderInputSerializer
from shop.serializers.output import OrderOutputSerializer
from shop.models import (Order, Customer, Cart)

logger = logging.getLogger(__name__)


class OrderView(viewsets.ModelViewSet):
    http_method_names = ["post", 'get', 'put', 'delete']
    permission_classes = [permissions.AllowAny]
    default_serializer_class = OrderInputSerializer
    serializer_classes = {
        "create": OrderInputSerializer,
        "update": OrderInputSerializer
    }
    queryset = Order.objects.none()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def list(self, request, *args, **kwargs):
        return Response("Permission denied", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        instance = Order.objects.get(id=kwargs["pk"])
        serializer = OrderInputSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            serializer = OrderInputSerializer(data=request.data)
            if serializer.is_valid():
                order = serializer.create(serializer.validated_data)
                return Response({'success': True, 'data': OrderOutputSerializer(order).data},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.info("create - OrderView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = Order.objects.get(id=kwargs["pk"])
            serializer = OrderInputSerializer(instance, data=request.data)
            if serializer.is_valid():
                order = serializer.update(instance, serializer.validated_data)
                return Response({'success': True, 'data': OrderOutputSerializer(order).data},
                                status=status.HTTP_200_OK)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.info("update - OrderView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = Order.objects.get(id=kwargs["pk"])
            instance.status = 2
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            logger.info("destroy - OrderView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
