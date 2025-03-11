from netbox.api.viewsets import NetBoxModelViewSet

from netbox_routeros import models
from netbox_routeros.api import serializers


class RouterosTypeViewSet(NetBoxModelViewSet):
    queryset = models.RouterosType.objects.prefetch_related("platform", "tags")
    serializer_class = serializers.RouterosTypeSerializer


class RouterosInstanceViewSet(NetBoxModelViewSet):
    queryset = models.RouterosInstance.objects.prefetch_related("device", "tags")
    serializer_class = serializers.RouterosInstanceSerializer
