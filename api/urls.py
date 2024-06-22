from django.urls import path
from .views import (
    ServiceListCreate, ServiceDetail, ServiceFAQListCreate, ServiceFAQDetail,
    TestimonialListCreate, TestimonialDetail, BlogListCreate, BlogDetail,
    ProjectListCreate, ProjectDetail, ContactListCreate, ContactDetail,
    QuoteRequestListCreate, QuoteRequestDetail, OnlineBookingListCreate,
    OnlineBookingDetail, GalleryListCreate, GalleryDetail, FAQListCreate, FAQDetail
)

urlpatterns = [
    path('services/', ServiceListCreate.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
    path('service-faqs/', ServiceFAQListCreate.as_view(), name='service-faq-list-create'),
    path('service-faqs/<int:pk>/', ServiceFAQDetail.as_view(), name='service-faq-detail'),
    path('testimonials/', TestimonialListCreate.as_view(), name='testimonial-list-create'),
    path('testimonials/<int:pk>/', TestimonialDetail.as_view(), name='testimonial-detail'),
    path('blogs/', BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('contacts/', ContactListCreate.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path('quote-requests/', QuoteRequestListCreate.as_view(), name='quote-request-list-create'),
    path('quote-requests/<int:pk>/', QuoteRequestDetail.as_view(), name='quote-request-detail'),
    path('online-bookings/', OnlineBookingListCreate.as_view(), name='online-booking-list-create'),
    path('online-bookings/<int:pk>/', OnlineBookingDetail.as_view(), name='online-booking-detail'),
    path('galleries/', GalleryListCreate.as_view(), name='gallery-list-create'),
    path('galleries/<int:pk>/', GalleryDetail.as_view(), name='gallery-detail'),
    path('faqs/', FAQListCreate.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', FAQDetail.as_view(), name='faq-detail'),
]
