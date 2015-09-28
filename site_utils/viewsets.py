from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from site_utils.models import SiteMessages
from site_utils.models import SitePage
from site_utils.serializers import SitePageSerializer

@api_view(['GET'])
def site_page(request,page_slug):
    page = SitePage.objects.get(slug=page_slug)
    serialize_page = SitePageSerializer(page)
    return Response(serialize_page.data)

@api_view(['GET'])
def index_first_page(request):
    pages = SitePage.objects.all()
    if pages:
        serialize_first_page =SitePageSerializer(pages[0])
        return Response(serialize_first_page.data)
    return Response(status=200)

@api_view(['POST'])
def send_message(request):
    title = request.DATA.get('title')
    content = request.DATA.get('content')
    message_file = request.FILES.get('file')

    site_message = SiteMessages (title = title, content= content, message_file = message_file)
    site_message.save()

    return Response(status=200)


