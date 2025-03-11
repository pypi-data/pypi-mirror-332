from dcim.api.serializers import InterfaceSerializer
from ipam.api.serializers import VLANSerializer
from netbox.api.fields import IntegerRangeSerializer
from netbox.api.serializers import NetBoxModelSerializer

from netbox_routeros import models

from .routeros import RouterosInstanceSerializer


class CapsmanInstanceSerializer(NetBoxModelSerializer):
    routeros = RouterosInstanceSerializer(nested=True)

    class Meta:
        model = models.CapsmanInstance
        fields = ("id", "routeros", "description", "comments", "tags")
        brief_fields = ("id", "routeros")


class CapsmanServerConfigSerializer(NetBoxModelSerializer):
    capsman = CapsmanInstanceSerializer(nested=True)

    class Meta:
        model = models.CapsmanServerConfig
        fields = ("id", "capsman", "enabled", "comments", "tags")
        brief_fields = ("id", "capsman")


class CapsmanChannelSerializer(NetBoxModelSerializer):
    capsman = CapsmanInstanceSerializer(nested=True)
    frequency = IntegerRangeSerializer(many=True, required=False)

    class Meta:
        model = models.CapsmanChannel
        fields = (
            "id",
            "name",
            "capsman",
            "band",
            "channel_width",
            "frequency",
            "skip_dfs_channels",
            "description",
            "enabled",
            "comments",
            "tags",
        )
        brief_fields = (
            "id",
            "capsman",
            "name",
            "band",
            "channel_width",
            "frequency",
        )


class CapsmanDatapathSerializer(NetBoxModelSerializer):
    capsman = CapsmanInstanceSerializer(nested=True)
    bridge = InterfaceSerializer(nested=True, allow_null=True)
    vlan = VLANSerializer(nested=True, allow_null=True)

    class Meta:
        model = models.CapsmanDatapath
        fields = (
            "id",
            "name",
            "capsman",
            "bridge",
            "vlan",
            "description",
            "enabled",
            "comments",
            "tags",
        )
        brief_fields = ("id", "capsman", "name", "bridge", "vlan")
