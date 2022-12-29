from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from cloudinary.forms import CloudinaryJsFileField

User = get_user_model()


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comment = serializers.HyperlinkedRelatedField(
        view_name="comment_detail", many=True, read_only=True
    )

    file = CloudinaryJsFileField(attrs={"multiple": 1})

    class Meta:
        model = Post
        fields = ("id", "status_body", "date", "comment", "file")


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(view_name="post_detail", read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source="post"
    )

    class Meta:
        model = Comment
        fields = ("id", "body", "date", "post", "post_id")


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop("password")
        password_confirmation = data.pop("password_confirmation")

        if password != password_confirmation:
            raise serializers.ValidationError(
                {"password_confirmation": "Passwords do not match"}
            )

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})

        data["password"] = make_password(password)
        return data

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password_confirmation",
        )
