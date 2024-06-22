from django.contrib import admin

# Register your models here.
from .models import Service, ServiceFAQ, Testimonial, Blog, Project, Contact, QuoteRequest, OnlineBooking, Gallery, FAQ, ProjectImage

admin.site.register(Service)

admin.site.register(ServiceFAQ)

admin.site.register(Testimonial)

admin.site.register(Blog)

admin.site.register(Project)
admin.site.register(ProjectImage)

admin.site.register(Contact)

admin.site.register(QuoteRequest)

admin.site.register(OnlineBooking)

admin.site.register(Gallery)

admin.site.register(FAQ)