from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=50)
    
    locations = [
        ('Hangyeong-myeon', '한경면'), 
        ('Hallim-eup', '한림읍'),
        ('Aewol-eup', '애월읍'), 
        ('Jeju-si', '제주시'), 
        ('Jocheon-eup', '조천읍'), 
        ('Gujwa-eup', '구좌읍'),
        ('Daejeong-eup', '대정읍'),
        ('Andeok-myeon', '안덕면'),
        ('Seogwipo-si', '서귀포시'),
        ('Namwon-eup', '남원읍'),
        ('Pyoseon-myeon', '표선면'),
        ('Seongsan-eup', '성산읍'),
        ('Udo-myeon', '우도면'),
    ]
    
    location = models.CharField(max_length=50, choices=locations)
    mainphoto = models.ImageField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return self.name