from django.http import  JsonResponse
from rest_framework import  status
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny


class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Extract user data from the request
        username = request.data.get('username')
        password = request.data.get('password')

        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.create_user(username=username, password=password)           
            token, _ = Token.objects.get_or_create(user=user) 
            return JsonResponse({'id': user.id,'is_admin': user.is_admin, 'token': str(token), 'username': username}, status=status.HTTP_200_OK)
        except ValueError as error:
            return JsonResponse({'message': str(error) }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({'message': 'Something went wrong!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = authenticate(request, username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                return JsonResponse({'id': user.id, 'is_admin': user.is_admin,'token': str(token), 'username': username}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class LogoutUser(APIView):
    def delete(self, request):
        request.auth.delete()

        return JsonResponse({'message': 'User logged out successfully'}, status=status.HTTP_204_NO_CONTENT)