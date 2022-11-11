from rest_framework import serializers
from users.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, required=True)
    email = serializers.EmailField(max_length=50, required=True)
    password = serializers.CharField(
        required=True, style={'input_type': 'password'})

    confirm_password = serializers.CharField(
        max_length=100, required=True,  style={'input_type': 'password'})

    bio = serializers.CharField(max_length=256, required=False)

    def validate_email(self, email):
        already_existing_mail = User.objects.filter(email=email).first()
        if already_existing_mail:
            raise serializers.ValidationError(
                "this email already exist try to login in ")
        return email

    def validate_username(self, username):
        already_existing_username = User.objects.filter(
            username=username).first()
        if already_existing_username:
            raise serializers.ValidationError(
                " this username already exist try another one")
        return username

    def validate(self, data):

        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Can not be empty")
        if len(data.get('password')) < 10:
            raise serializers.ValidationError("Password too short ")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("two passwords must be same")

        return data

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']
