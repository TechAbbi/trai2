from django.db import models


class Student(models.Model):
    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.score}'

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    score = models.DecimalField(max_digits=5, decimal_places=2)


class Exam(models.Model):
    def __str__(self):
        return f"{self.date}"

    date = models.DateField()
    student = models.ForeignKey(Student, related_name="exams", on_delete=models.CASCADE)


