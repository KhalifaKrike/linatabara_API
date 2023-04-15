from django.db import models

'''
print(donor.get_blood_type_display())  # Output: "A+"
donor = Donor(name='John Smith', blood_type=BloodType.A_POSITIVE)
donor.save()
the first value is the database value that will be stored, 
and the second value is a human-readable label that will be displayed in forms and the Django admin.
'''


class BloodType(models.Model):
    type = models.CharField(max_length=3)
    number_type = models.IntegerField(default=0)
    def __str__(self):
        return self.type

class Wilaya(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    number_in_wilaya = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.number) +'- '+ self.name


class Daiira(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    wilaya_n = models.IntegerField()
    number_in_daiira = models.IntegerField(default=0)

    def __str__(self):
        return self.name + '(' +str(self.wilaya_n)+')'


class Donor(models.Model):
    #BLOOD_CHOICES = [(type.type, type.type) for type in BloodType.objects.all()]
    #WILAYA_CHOICES = [(wilaya.number, wilaya.name) for wilaya in Wilaya.objects.all()]
    #blood = models.CharField(max_length=3, choices=BLOOD_CHOICES)
    #wilaya = models.CharField(max_length=30, choices=WILAYA_CHOICES)
    #daiira = models.CharField(max_length=30,blank=True)

    blood = models.ForeignKey(BloodType, on_delete=models.SET_NULL,null=True,blank=True)
    wilaya = models.ForeignKey(Wilaya,on_delete=models.SET_NULL,null=True,blank=True)
    daiira = models.ForeignKey(Daiira,on_delete=models.SET_NULL,null=True,blank=True)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=128,blank=False)
    n_tel = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return str(self.wilaya).replace('-','') + ' |  type =' + str(self.blood)
    
    def save(self, *args, **kwargs):
        if self.wilaya:
            self.wilaya.number_in_wilaya = Donor.objects.filter(wilaya=self.wilaya).count() + 1
            self.wilaya.save()

        if self.blood:
            self.blood.number_type = Donor.objects.filter(blood=self.blood).count() + 1
            self.blood.save()

        if self.daiira:
            self.daiira.number_in_daiira = Donor.objects.filter(daiira=self.daiira).count() + 1
            self.daiira.save()

        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        if self.wilaya:
            self.wilaya.number_in_wilaya = Donor.objects.filter(wilaya=self.wilaya).count() - 1
            self.wilaya.save()

        if self.blood:
            self.blood.number_type = Donor.objects.filter(blood=self.blood).count() - 1
            self.blood.save()

        if self.daiira:
            self.daiira.number_in_daiira = Donor.objects.filter(daiira=self.daiira).count() - 1
            self.daiira.save()

        super().delete(*args, **kwargs)
        

'''
def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "n_tel": self.n_tel,
            "blood": self.blood.type,
            "wilaya": self.wilaya.name,
            "daiira": self.daiira.name,
        }

    def as_json(self):
        return json.dumps(self.to_dict())
'''