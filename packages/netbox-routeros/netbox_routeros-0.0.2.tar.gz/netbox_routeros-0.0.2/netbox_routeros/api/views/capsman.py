from netbox.api.viewsets import NetBoxModelViewSet

from netbox_routeros import models
from netbox_routeros.api import serializers


class CapsmanInstanceViewSet(NetBoxModelViewSet):
    queryset = models.CapsmanInstance.objects.prefetch_related("routeros", "tags")
    serializer_class = serializers.CapsmanInstanceSerializer


class CapsmanServerConfigViewSet(NetBoxModelViewSet):
    queryset = models.CapsmanServerConfig.objects.prefetch_related("capsman", "tags")
    serializer_class = serializers.CapsmanServerConfigSerializer


class CapsmanChannelViewSet(NetBoxModelViewSet):
    queryset = models.CapsmanChannel.objects.prefetch_related("capsman", "tags")
    serializer_class = serializers.CapsmanChannelSerializer


class CapsmanDatapathViewSet(NetBoxModelViewSet):
    queryset = models.CapsmanDatapath.objects.prefetch_related(
        "capsman", "bridge", "vlan", "tags"
    )
    serializer_class = serializers.CapsmanDatapathSerializer
