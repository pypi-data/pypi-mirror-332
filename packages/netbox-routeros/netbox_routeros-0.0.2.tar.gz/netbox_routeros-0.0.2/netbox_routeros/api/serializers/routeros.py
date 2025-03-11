from dcim.api.serializers import DeviceSerializer, PlatformSerializer
from netbox.api.serializers import NetBoxModelSerializer

from netbox_routeros import models


class RouterosTypeSerializer(NetBoxModelSerializer):
    platform = PlatformSerializer(nested=True)

    class Meta:
        model = models.RouterosType
        fields = (
            "id",
            "platform",
            "description",
            "comments",
            "tags",
        )
        brief_fields = (
            "id",
            "platform",
        )


class RouterosInstanceSerializer(NetBoxModelSerializer):
    device = DeviceSerializer(nested=True)

    class Meta:
        model = models.RouterosInstance
        fields = (
            "id",
            "device",
            "description",
            "comments",
            "tags",
        )
        brief_fields = (
            "id",
            "device",
        )
