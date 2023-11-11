from django.http import  JsonResponse
from rest_framework import  status
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated


class RegisterUser(APIView):
    def post(self, request):
        # Extract user data from the request
        username = request.data.get('username')
        password = request.data.get('password')

        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        # Create a new user
        user = CustomUser.objects.create_user(username=username, password=password)
        

        # Log the user in
        login(request, user)

        return JsonResponse({'message': 'User registered and logged in successfully'}, status=status.HTTP_201_CREATED)
    
class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print(token)
            return JsonResponse({'token': str(token) }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can log out

    def delete(self, request):
        # Log out the user
        request.auth.delete()  # This is how you revoke the user's token

        return JsonResponse({'message': 'User logged out successfully'}, status=status.HTTP_204_NO_CONTENT)