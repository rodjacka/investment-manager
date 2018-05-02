from django.db import models


class SettingType(models.Model):
    setting_type = models.CharField(max_length=20)
    def __str__(self):
        return self.setting_type

class Settings(models.Model):
    setting_name = models.CharField(max_length=200)
    setting_type = models.ForeignKey('SettingType', on_delete=models.CASCADE)
    setting_text_value = models.CharField(max_length=200, blank=True)
    setting_numerical_value = models.FloatField(blank=True)

    def get_value(self):
        if self.setting_type=='numeric':
            return self.setting_numerical_value
        else:
            return self.setting_text_value

    def set_value(self,val):
        if self.setting_type=='numeric':
            self.setting_numerical_value = val
        else:
            self.setting_text_value = val

    class Meta:
        verbose_name_plural = "settings"



class SecurityClass(models.Model):
    security_class = models.CharField(max_length=200)

    def __str__(self):
        return self.security_class

class SecurityType(models.Model):
    security_type = models.CharField(max_length=200)

    def __str__(self):
        return self.security_type

class SecurityDividend(models.Model):
    dividend_date = models.DateField()
    dividend_per_share = models.FloatField()
    franking_percentage = models.FloatField()
    security = models.ForeignKey('Security', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "dividends"

    def __str__(self):
        return str(self.dividend_date)

class Security(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    benchmark = models.CharField(max_length=200, blank=True, null=True)
    management_expense_ratio = models.FloatField(blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True)
    fetch_data = models.BooleanField(default=False)
    security_type = models.ForeignKey('SecurityType', on_delete=models.CASCADE, null=True,)
    security_class = models.ForeignKey('SecurityClass', on_delete=models.CASCADE, null=True,)

    class Meta:
        verbose_name_plural = "securities"

    def __str__(self):
        return self.symbol

class SecurityDailyPrice(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    security = models.ForeignKey('Security', on_delete=models.CASCADE)

#### Notes ####
class NoteTypes(models.Model):
    note_type = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "notetypes"

class Note(models.Model):
    note_type = models.ForeignKey('NoteTypes', on_delete=models.CASCADE)
    security = models.ForeignKey('Security', on_delete=models.CASCADE)
    security_daily_price = models.ForeignKey('SecurityDailyPrice', on_delete=models.CASCADE)
    note_date = models.DateTimeField()
    content = models.TextField()


#### Portfolios ####
class PortfolioSecurity(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    security = models.ForeignKey('Security', on_delete=models.CASCADE)
    weight = models.FloatField()

    class Meta:
        verbose_name_plural = "portfoliosecurities"


class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateField()
    date_first_trade = models.DateField()
    expected_standard_deviation = models.FloatField()
    expected_annual_return = models.FloatField()
    sharpe_ratio = models.FloatField()
    skewness = models.FloatField()
    kurtosis = models.FloatField()






