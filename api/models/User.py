from django.db import models


class User(models.Model):
    """
    사용자 정보를 저장하는 Model

    Args:
        user_id (CharField): 아이디
        user_pw (CharField): 비밀번호
        name (CharField): 이름
        mileage (PositiveIntegerField): 마일리지
        mobile (CharField): 전화번호
    """

    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    mileage = models.PositiveIntegerField(default=0)
    mobile = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_attribute(self, attr: str):
        """
        attr로 전달된 str 형식의 attr 이름을 통해 실제 데이터를 반환

        Args:
            attr (str): Model의 attribute

        Returns:
            data (str) or None
        """

        if 'user_id' in attr:
            return self.user_id
        elif 'user_pw' in attr:
            return self.user_pw
        elif 'name' in attr:
            return self.name
        elif 'mileage' in attr:
            return self.mileage
        elif 'mobile' in attr:
            return self.mobile
        else:
            return None

    def __str__(self):
        return self.user_id
