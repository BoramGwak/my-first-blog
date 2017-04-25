# python의 모든 Model 객체를 선언하여 모델을 만드는 곳

#from ~ import~ : 다른 파일에 있는 것을 가져와서 쓰겠다.
from django.db import models 
from django.utils import timezone
# Create your models here.

class Post(models.Model): # post라는 모델(객체) 선언 
# models.model : class가 모델임을 의미 - 이 코드를 통해 Post라는 객체가 장고의 데이터베이스에 저장된다는 것을 알수 있음.
    author = models.ForeignKey('auth.User')
    # models.ForeignKey : 다른 모델에 대한 링크 
    title = models.CharField(max_length=200) 
    # models.CharField : 글자수가 제한된 텍스트 정의 - 200자까지 
    text = models.TextField()
    # models.TextField : 글자수에 제한이 없는 긴 텍스트 정의 
    created_date = models.DateTimeField(
            default=timezone.now)
    # models.DateTimeField : 날짜,시간 
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # def publish(self) : publish라는 메서드 선언 


    def __str__(self):
        return self.title

    # __ : dunder(던더) : 더블 언더스코어 