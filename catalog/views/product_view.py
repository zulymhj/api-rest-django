import logging
import os
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from datetime import date

from catalog.serializers.input import ProductInputSerializer
from catalog.serializers.output import ProductOutputSerializer
from catalog.models.product import Product

logger = logging.getLogger(__name__)


class ProductView(viewsets.ModelViewSet):
    http_method_names = ["post", 'get', 'put', 'delete']
    permission_classes = [permissions.AllowAny]
    default_serializer_class = ProductInputSerializer
    serializer_classes = {
        "create": ProductInputSerializer,
        "update": ProductInputSerializer
    }
    queryset = Product.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def create(self, request, *args, **kwargs):
        try:
            serializer = ProductInputSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                product = serializer.create(serializer.validated_data)
                return Response({'success': True, 'data': ProductOutputSerializer(product).data},
                                status=status.HTTP_201_CREATED)
            return Response({'success': False, 'message': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.info("create - ProductView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = ProductInputSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                product = serializer.update(instance, serializer.validated_data)
                return Response({'success': True, 'data': ProductOutputSerializer(product).data},
                                status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.info("update - ProductView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            product = self.get_object()
            product.status = 2
            product.deleted_at = date.today()
            product.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            logger.info("destroy - ProductView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            # list product active and order by category
            products = Product.objects.all().exclude(status=2).order_by('category', 'created_at')
            serializer = ProductOutputSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as ex:
            logger.info("list - ProductView")
            logger.error(ex)
            return Response({
                'success': False,
                'message': ex
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
