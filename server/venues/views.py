from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from venues.models import Venue
from venues.serializers import VenueSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def venue_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Venue.objects.all()
        serializer = VenueSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = VenueSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data, status=201)
    #     return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def venue_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Venue.objects.get(pk=pk)
    except Venue.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VenueSerializer(snippet)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = VenueSerializer(snippet, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data)
    #     return JSONResponse(serializer.errors, status=400)
    #
    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return HttpResponse(status=204)


@csrf_exempt
def venue_nearby(request, lat, lon):

    # https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points

    from math import radians, cos, sin, asin, sqrt

    def haversine(lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        print(lon1, lat1, lon2, lat2)

        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2.0)**2.0 + cos(lat1) * cos(lat2) * sin(dlon/2.0)**2.0
        c = 2.0 * asin(sqrt(a))
        km = 6367.0 * c
        return km

    venues = Venue.objects.all()
    venues = [venue for venue in venues if haversine(float(lon), float(lat), float(venue.longitude), float(venue.latitude)) < 0.5]
    print(len(venues))

    serializer = VenueSerializer(venues, many=True)
    response = JSONResponse(serializer.data)
    return response
