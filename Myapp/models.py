from django.db import models

# Model for ผู้ใช้ (User)
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model for ข่าวสาร (News)
class News(models.Model):
    image = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    announcement_date = models.DateField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

# Model for อุปกรณ์ (Equipment)
class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    name = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    img = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

# Model for สนาม (Field)
class Field(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

# Model for การจอง (Booking)
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')
    equipment_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.user.first_name}"

