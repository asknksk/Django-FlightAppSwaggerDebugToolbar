from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from users.serializers import RegisterSerializer
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

     #register olduğu anda token dönmesi için yaptık
    def create(self, request, *args, **kwargs):  #functionu genericsten aldık
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  #if serializer.is_valid in kısa yöntemi
        # self.perform_create(serializer)  #serialzer.save() anlamına geliyor
        user = serializer.save() # bunu yazdık onun yerine  direk token oluşturuyor save edince
        data = serializer.data #datayı neyi oluşturduk
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['error'] = 'userDont have token. Please login'
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)