from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer): #create a user serializer
    class Meta:
        model=CustomUser
        fields=('email','username','password')
        extra_kwargs={'password':{'write_only':True,'required':True}} #password is write only and required

    def create(self,validated_data): #create a new user
        user= CustomUser(
            username=validated_data['username'], #create a new user with the validated data
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
  
#change password serializer
class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# reset password serializer
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta: #meta class to specify the fields
        fields = ['email']