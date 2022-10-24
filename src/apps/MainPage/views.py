from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from .serializers import GetLinkSerializer
from LinkShortener.settings import SHORTLINK_HOST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def main_page(request, user_link=None):
    short_link = None

    context = {
        'short_link': short_link,
    }

    if user_link:
        link_to_redirect = get_object_or_404(Link, short_link=user_link)
        return redirect(link_to_redirect.full_link)

    elif request.POST:
        full_link = request.POST.get('link')
        link = Link.get_short_link_by_full_link(full_link=full_link)

        context['short_link'] = SHORTLINK_HOST + link

    return render(request, "index.html", context)


class GetLinkApi(APIView):
    def post(self, request):
        serializer = GetLinkSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            link = Link.get_short_link_by_full_link(full_link=serializer.data['full_link'])
            return Response(SHORTLINK_HOST + link)


