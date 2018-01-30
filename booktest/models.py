from django.db import models

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = 'bookinfo'

    # books1 = models.Manager()
    # books2 = BookInfoManager()

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    hbook=models.ForeignKey(BookInfo)

    def showname(self):
        return self.hname
    def __str__(self):
        return self.hname

