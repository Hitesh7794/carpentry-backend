from rest_framework import serializers
from .models import Service, ServiceFAQ, Testimonial, Blog, Project, Contact, QuoteRequest, OnlineBooking, Gallery, FAQ, ProjectImage

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFAQ
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ProjectImageSerializr(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializr(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'images']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class QuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = '__all__'


class OnlineBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineBooking
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
