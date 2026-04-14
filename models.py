from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    CATEGORY_CHOICES = [
        ('Faculty', 'Faculty'),
        ('Infrastructure', 'Infrastructure'),
        ('Canteen', 'Canteen'),
        ('Library', 'Library'),
        ('Other', 'Other'),
    ]

    student_name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.category}"