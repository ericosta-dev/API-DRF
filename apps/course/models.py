from django.db import models

# Create your models here.
class Base(models.Model):
    publication = models.DateTimeField(auto_now_add=True)
    actualization = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Course(Base):
    title = models.CharField(max_length=255,verbose_name='Title')
    url = models.URLField(unique=True,verbose_name='URL')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

class Avaliation(Base):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='avaliations')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True,default='')
    avaliation = models.DecimalField(max_digits=2,decimal_places=1)

    class Meta:
        verbose_name = 'Avaliation'
        verbose_name_plural = 'Avaliations'
        unique_together = ['email','course']
        
    def __str__(self):
        return f'{self.name} rated the course: {self.course} with a note: {self.avaliation}'
