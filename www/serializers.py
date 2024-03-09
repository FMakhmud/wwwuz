from www.models import Direction, SiteType, SiteLog
from rest_framework.serializers import ModelSerializer


class DirectionSerializers(ModelSerializer):
    class Meta:
        model = Direction
        fields = ('title', 'is_new',)


class SiteSerializer(ModelSerializer):
    class Meta:
        model = SiteType
        fields = (
            'title',
        )

#
# class SiteTypeSerializer(ModelSerializer):
#     class Meta:
#         model = SiteType
#         fields = (
#             'title',
#         )
#
#
# class SiteLogSerializer(ModelSerializer):
#     class Meta:
#         model = SiteLog
#         fields = (
#             'visitor_count',
#             'created_at',
#             'updated_at',
#         )


class SiteLogMainSerializer(ModelSerializer):
    class Meta:
        model = SiteLog
        fields = (
            'site',
            'visitor_count',
            'created_at',
            'updated_at',

        )
