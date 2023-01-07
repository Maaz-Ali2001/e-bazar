from djongo import models

class User(models.Model):
    user_ID=models.ObjectIdField()
    user_Name=models.CharField(max_length=255)
    user_email_phone=models.EmailField(max_length=255)

    user_Password=models.CharField(max_length=255)
    objects=models.DjongoManager()

class Vendor_Bank_Details(models.Model):
    credit_card_Number=models.CharField(max_length=255)
    expires=models.DateField()
    credit_card_Holder=models.CharField(max_length=255)
    billing_Address=models.CharField(max_length=255)

    class Meta:
        abstract=True


class Vendor(models.Model):
    user_ID=models.ArrayReferenceField(
        to=User,
        on_delete=models.CASCADE
    )
    vendor_ID=models.ObjectIdField()
    vendor_Name=models.CharField(max_length=255)
    vendor_Password = models.CharField(max_length=255)
    vendor_CNIC = models.CharField(max_length=255)
    vendor_Type = models.CharField(max_length=255)
    vendor_Phone = models.IntegerField(max_length=100)
    vendor_Bank_Details=models.EmbeddedField(
        model_container=Vendor_Bank_Details,
    )
    objects = models.DjongoManager()


