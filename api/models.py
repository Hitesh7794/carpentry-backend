from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='public/images/services/', blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='public/images/testimonials/', blank=True , null=True)
    rating = models.PositiveIntegerField(default=5)
    google_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Testimonial by {self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='public/images/blogs/')
    tags = models.CharField(max_length=200, help_text='Comma-separated tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='public/images/projects/')

    def __str__(self):
        return f"Image for {self.project.title}"


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name}"


class QuoteRequest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    project_details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote Request from {self.name}"


class OnlineBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    service = models.CharField(max_length=300)
    date = models.DateField()
    additional_info = models.TextField(blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name}"


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
