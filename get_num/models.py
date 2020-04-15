from django.db import models

# Create your models here.モデルの作成

class Log(models.Model):
    created_at=models.DateTimeField(
        verbose_name="登録時間",
        auto_now_add=True,
    )
    press_ave_3min=models.FloatField(
        verbose_name="圧力センサ値",
        blank=True
    )
    work_or_sabori=models.FloatField(
        verbose_name="勤怠状況",
        blank=True
    )
    user_label=models.CharField(
        verbose_name="ユーザー識別",
        blank=True,
        default="kanta",
        max_length=50
    )

    #以下は管理サイトの表示設定
    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name='採取データ'
        verbose_name_plural='採取データ'
