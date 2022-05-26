from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from PMWorks_II.models import UserRole, Role


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        role_id = UserRole.objects.filter(user=user.id).values()[0]['RoleID_id']
        role_name = Role.objects.filter(id=role_id).values()[0]['RoleName']
        print('****************************')
        print(role_name)
        print('****************************')
        # Add custom claims
        token['role'] = role_name
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer