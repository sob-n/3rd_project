# from django.db import models
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator
#
# # Create your models here.
#
# class Face(models.Model):
#     user=models.ForeignKey(USER,on_delete=models.CASCADE)
#     seq=models.IntField(null=False)
#     create_date
#
#     blink_mean
#     direction_tot
#     emotion_per
#
#     chart1 #blink
#     chart2 #direction
#     chart3 #emotion
#     screenshot
#
#
# class Voice(models.Model):
#     user=models.ForeignKey(USER,on_delete=models.CASCADE)
#     seq=models.IntField(null=False)
#     create_date
#
#     time
#     rate_mean
#     filler_tot
#
#     chart1 #rate
#     chart2 #tone
#     chart3 #wordcloud
#
#     tone
#     STT_res
