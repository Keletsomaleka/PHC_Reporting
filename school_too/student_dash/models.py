from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.conf import settings
# Create  a new user
class MyChurchManager(BaseUserManager):

    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("users must have email")
        if not username:
            raise ValueError("users must have username")
        user = self.model(
            email = self.normalize_email(email),
            username =username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Church(models.Model):
    name = models.CharField(max_length=200, unique=True)
    church_est_date = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

class ChurchLeader(AbstractBaseUser):

    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    username = models.CharField(max_length=30, unique=True)
    church_name = models.ForeignKey(Church,max_length=60 ,on_delete=models.CASCADE,null=True, blank=True)
    position = models.CharField(max_length=100,choices=[('Chairperson','Chairperson'),('Secretary','Secretary'),('Treasurer','Treasurer')],null=True,blank=True)
    cellphone = models.IntegerField( null=True, blank=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyChurchManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __st__(self):
        return self.church_name

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_Label):
        return True


class Stats(models.Model):

    church_name         = models.ForeignKey(Church,on_delete=models.CASCADE)
    username            = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    women               = models.IntegerField(null=True, blank=True)
    men                 = models.IntegerField(null=True, blank=True)
    youth_g1            = models.IntegerField(null=True, blank=True)
    youth_g2            = models.IntegerField(null=True, blank=True)
    children_g1         = models.IntegerField(null=True, blank=True)
    children_g2         = models.IntegerField(null=True, blank=True)
    children_g3         = models.IntegerField(null=True, blank=True)
    ordained_ministers  = models.IntegerField(null=True, blank=True)
    licensed_ministers  = models.IntegerField(null=True, blank=True)
    mission_workers     = models.IntegerField(null=True, blank=True)
    Total               = models.IntegerField(null=True,blank=True)
    created_at          = models.DateField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return str(self.church_name)
    
    
class FinancialReport(models.Model):

    church_name         = models.ForeignKey(Church,on_delete=models.CASCADE)
    username            = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    tithe_budgeted      = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    tithe_actual        = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    offering_budgeted   = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    offering_actual     = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    other_income        = models.DecimalField(decimal_places=2, max_digits=10,null=True,blank=True)
    salaries_budgeted    = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    salaries_actual     = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    housing_allowance_budgeted   = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    housing_allowance_actual   = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    pension_plan_budgeted         =models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    pension_plan_actual         = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    clergy_continuing_Education_budgeted = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    clergy_continuing_Education_actual = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    travel_allowance_budgeted = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    travel_allowance_actual = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    office_supplies_budgeted    = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    office_supplies_actual = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    worship_supplies_budgeted = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    worship_supplies_actual = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    cleaning_and_maintenance_budgeted = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    cleaning_and_maintenance_actual = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    taxes_budgeted               = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    taxes_actual                 = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    insurance_budgeted         = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    insurance_actual           = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    utilities_budgeted           = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    utilities_actual            = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    telephone_budgeted           = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    telephone_actual            = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    capital_expenses_budgeted    = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    capital_expenses_actual     = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    debt_retirement_budgeted     = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    debt_retirement_actual       = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True)
    other_expenses      = models.DecimalField(decimal_places=2, max_digits=10,null=True,blank=True)

    def __str__(self):
        return str(self.church_name)




class Filter(models.Model):
    church_name = models.ForeignKey(Church, on_delete=models.CASCADE,null=True, blank=True)
  


class Report(models.Model):

    username            = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    church_name         = models.ForeignKey(Church,on_delete=models.CASCADE)
    mens_ministry_report= models.TextField()
    Mens_activities     = models.TextField(null=True,blank=True)
    womens_ministry_report =models.TextField()
    Womens_activities    = models.TextField(null=True,blank=True)
    youth_ministry_report = models.TextField()
    youth_activities     = models.TextField(null=True,blank=True)
    childrens_ministry_report =models.TextField()
    children_activities   = models.TextField(null=True,blank=True)
    Pastors_report        = models.TextField()
    pastor_activies       = models.TextField(null=True,blank=True)
    created_at            = models.DateField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return str(self.church_name)