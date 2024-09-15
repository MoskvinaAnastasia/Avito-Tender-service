from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Bid, Organization, Tender
from .serializers import (BidSerializer, OrganizationSerializer,
                          TenderSerializer)


@api_view(['GET'])
@permission_classes([AllowAny])
def ping(request):
    """Эндпоинт для проверки доступности сервера."""
    return Response(status=200)


class TenderViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с тендерами."""

    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def new(self, request):
        """Создать новый тендер."""
        if not request.user.has_perm('create_tender'):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def my(self, request):
        """Возвращает список тендеров текущего пользователя."""
        user = request.user
        tenders = Tender.objects.filter(creator=user)
        serializer = TenderSerializer(tenders, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def edit(self, request, pk=None):
        """Редактировать существующий тендер. Увеличивается версия."""
        tender = self.get_object()
        if not request.user.has_perm('edit_tender', tender):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TenderSerializer(tender, data=request.data, partial=True)
        if serializer.is_valid():
            tender = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Опубликовать тендер. Доступен только ответственной организацией."""
        tender = self.get_object()
        if not request.user.has_perm('publish_tender', tender):
            return Response(status=status.HTTP_403_FORBIDDEN)

        tender.status = 'PUBLISHED'
        tender.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        """Закрыть тендер. Доступен только ответственной организацией."""
        tender = self.get_object()
        if not request.user.has_perm('close_tender', tender):
            return Response(status=status.HTTP_403_FORBIDDEN)

        tender.status = 'CLOSED'
        tender.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True,
            methods=['put'],
            url_path='rollback/(?P<version>[0-9]+)')
    def rollback(self, request, pk=None, version=None):
        """Откатить тендер к указанной версии."""
        tender = self.get_object()
        if version is None or not tender.rollback_version(version):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        tender.save()
        serializer = TenderSerializer(tender)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BidViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с предложениями."""

    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def new(self, request):
        """Создать новое предложение."""
        """Доступно только автору и ответственной организацией."""
        if not request.user.has_perm('create_bid'):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def my(self, request):
        """Возвращает список предложений текущего пользователя."""
        user = request.user
        bids = Bid.objects.filter(creator=user)
        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def edit(self, request, pk=None):
        """Редактировать существующее предложение. Увеличивается версия."""
        bid = self.get_object()
        if not request.user.has_perm('edit_bid', bid):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = BidSerializer(bid, data=request.data, partial=True)
        if serializer.is_valid():
            bid = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def rollback(self, request, pk=None, version=None):
        """Откатить предложение к указанной версии."""
        bid = self.get_object()
        if version is None or not bid.rollback_version(version):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        bid.save()
        serializer = BidSerializer(bid)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False,
            methods=['get'],
            url_path=r'(?P<tender_id>[0-9]+)/list')
    def list_bid(self, request, tender_id=None):
        """Получить список предложений для указанного тендера."""
        bids = Bid.objects.filter(tender_id=tender_id)
        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def decision(self, request):
        """Согласование/отклонение предложения."""
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def reviews(self, request):
        """Просмотр отзывов на предложения."""
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def feedback(self, request):
        """Добавить обратную связь по предложению."""
        return Response(status=status.HTTP_200_OK)


class OrganizationViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с организациями."""

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
