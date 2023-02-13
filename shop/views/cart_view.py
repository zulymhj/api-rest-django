import logging
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from datetime import datetime, date, timedelta

from shop.serializers.input import CartInputSerializer
from shop.serializers.output import CartOutputSerializer
from shop.models import (Cart)

logger = logging.getLogger(__name__)


class CartView(viewsets.ModelViewSet):
    http_method_names = ["post", 'get', 'put', 'delete']
    permission_classes = [permissions.AllowAny]
    default_serializer_class = CartInputSerializer
    serializer_classes = {
        "create": CartInputSerializer,
        "update": CartInputSerializer
    }
    queryset = Cart.objects.none()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def list(self, request, *args, **kwargs):
        return Response("Permission denied", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        instance = Cart.objects.get(id=kwargs["pk"])
        serializer = CartOutputSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            date_now = date.today()
            #cart pending buy
            cart_exist = Cart.objects.filter(
                status=0,
                created_at__gte=date_now
            ).order_by('created_at').first()

            serializer = CartInputSerializer(data=request.data)
            if serializer.is_valid():
                if cart_exist:
                    cart = serializer.update(cart_exist, serializer.validated_data)
                    return Response({'success': True, 'data': CartOutputSerializer(cart).data},
                                    status=status.HTTP_200_OK)
                cart = serializer.create(serializer.validated_data)
                return Response({'success': True, 'data': CartOutputSerializer(cart).data},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.info("create - CartView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = Cart.objects.get(id=kwargs["pk"])
            serializer = CartInputSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                cart = serializer.update(instance, serializer.validated_data)
                return Response({'success': True, 'data': CartOutputSerializer(cart).data},
                                status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as ex:
            logger.info("update - CartView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = Cart.objects.get(id=kwargs["pk"])
            instance.status = 2
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            logger.info("destroy - CartView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
