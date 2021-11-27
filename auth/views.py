from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

# # Create your views here.
# class TestLoginView(APIView):

#     user = User.objects.first()
#     data = get_tokens_for_user(user)


class MeView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        user = serializer.data
        return Response(
            {
                "username": user["username"],
                "email": user["email"],
            }
        )
