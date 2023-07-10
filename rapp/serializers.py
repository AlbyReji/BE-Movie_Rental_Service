from rest_framework import serializers
from .models import Movie
from rest_framework.validators import UniqueValidator
from django.utils import timezone
from datetime import date

class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=4,max_length=100,validators=[UniqueValidator(queryset=Movie.objects.all())])
    release_date = serializers.DateField(required=True)
    genre = serializers.ChoiceField(required=True,
            choices=["Action", "Drama", "Comedy", "Thriller", "Sci-Fi"],
            error_messages={ 'invalid_choice': 'Not valid,Please Choose - Action, Drama, Comedy, Thriller or Sci-Fi.'})
    duration_minutes = serializers.IntegerField(min_value=1, max_value=600)
    rating = serializers.FloatField(min_value=0.0, max_value=10.0, required=False, allow_null=True)

    def validate_title(self,value):
        pf = "Movie -"
        if not value.startswith("Movie -"):
            raise serializers.ValidationError("The Title Must strt with 'Movie -' ")
        title_text = value[len(pf):]
        title_len = len(title_text)
        if title_len < 4 or title_len > 100:
            raise serializers.ValidationError(" The title text must be between 2 and 100 characters long")
        return value

        
    def validate_release_date(self,value):
        current_date = timezone.now().date()

        if value > current_date:
            raise serializers.ValidationError("Release date cannot be in the future")

        release_date = date(current_date.year - 30,current_date.month, current_date.day)

        if value < release_date:
            raise serializers.ValidationError("Release date should not be more than 30 years ago")
        return value

    class Meta:
        model = Movie
        fields = '__all__'