from rest_framework import generics
from .models import Service, ServiceFAQ, Testimonial, Blog, Project, Contact, QuoteRequest, OnlineBooking, Gallery, FAQ
from .serializers import (
    ServiceSerializer, ServiceFAQSerializer, TestimonialSerializer, BlogSerializer,
    ProjectSerializer, ContactSerializer, QuoteRequestSerializer, OnlineBookingSerializer,
    GallerySerializer, FAQSerializer
)

# Service views
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Service FAQ views
class ServiceFAQListCreate(generics.ListCreateAPIView):
    queryset = ServiceFAQ.objects.all()
    serializer_class = ServiceFAQSerializer

class ServiceFAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceFAQ.objects.all()
    serializer_class = ServiceFAQSerializer

# Testimonial views
class TestimonialListCreate(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

# Blog views
class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Project views
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Contact views
class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Quote Request views
class QuoteRequestListCreate(generics.ListCreateAPIView):
    queryset = QuoteRequest.objects.all()
    serializer_class = QuoteRequestSerializer

class QuoteRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuoteRequest.objects.all()
    serializer_class = QuoteRequestSerializer

# Online Booking views
class OnlineBookingListCreate(generics.ListCreateAPIView):
    queryset = OnlineBooking.objects.all()
    serializer_class = OnlineBookingSerializer

class OnlineBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OnlineBooking.objects.all()
    serializer_class = OnlineBookingSerializer

# Gallery views
class GalleryListCreate(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

# FAQ views
class FAQListCreate(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
