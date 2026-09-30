from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortURLCreate(APIView):
    # Handles POST /shorten
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShortURLDetail(APIView):
    def get_object(self, shortCode):
        # Automatically returns a 404 Not Found if the code doesn't exist
        return get_object_or_404(ShortURL, short_code=shortCode)

    # Handles GET /shorten/<shortCode>
    def get(self, request, shortCode):
        url_obj = self.get_object(shortCode)
        # The user accessed the link, so we tell the Librarian to add 1 to the tally
        url_obj.access_count += 1
        url_obj.save()
        
        serializer = ShortURLSerializer(url_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handles PUT /shorten/<shortCode>
    def put(self, request, shortCode):
        url_obj = self.get_object(shortCode)
        serializer = ShortURLSerializer(url_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handles DELETE /shorten/<shortCode>
    def delete(self, request, shortCode):
        url_obj = self.get_object(shortCode)
        url_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShortURLStats(APIView):
    # Handles GET /shorten/<shortCode>/stats
    def get(self, request, shortCode):
        url_obj = get_object_or_404(ShortURL, short_code=shortCode)
        serializer = ShortURLSerializer(url_obj)
        # We only retrieve the data here; we do not increase the access count
        return Response(serializer.data, status=status.HTTP_200_OK)