from site_utils.models import SitePage
from rest_framework import serializers

class SitePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitePage

