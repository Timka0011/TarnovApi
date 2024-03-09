from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, number, password=None):

        if not username:
            raise ValueError("Userda username bulishi kerak")
        user = self.model(username=username,
                          number=number)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, number, password=None):
        user = self.create_user(username=username, number=number, password=password)

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
