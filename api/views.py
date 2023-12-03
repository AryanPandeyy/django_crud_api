from rest_framework import status
from rest_framework.views import APIView, Response

# views here.
class APICALLS(APIView):
    def get(self, request):
        items = {
            "apple",
            "mango",
        }
        response_data = {"datas":items}
        return Response(response_data,status=status.HTTP_200_OK)
