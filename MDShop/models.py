from django.db import models

from django.db import models 
from django.urls import reverse

from autoslug import AutoSlugField

from django.db.models.signals import pre_save
from django.db import models 

from datetime import date
from mptt.fields import  TreeForeignKey
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver



class Category(MPTTModel):
    name   = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug   = models.SlugField(null=False,unique=True)
    img    = models.ImageField(upload_to='photos')


    def __str__(self):
        return self.name

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name'] 
    


    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})
    


    def __str__(self):
        full_path=[self.name] 
        k=self.parent
        while k is not None:
            full_path.append(k.name)
            k=k.parent
        return '/'.join(full_path[::-1])


class Razdel(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)

    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Жанры"""
    name        = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url         = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"





class smartphone(models.Model):
    def __str__(self):
        return self.title

    img1     = models.ImageField(upload_to='photos',null=True, blank=True)
    img2     = models.ImageField(upload_to='photos',null=True, blank=True)
    img3     = models.ImageField(upload_to='photos',null=True, blank=True)
    img4     = models.ImageField(upload_to='photos',null=True, blank=True)
    img5     = models.ImageField(upload_to='photos',null=True, blank=True)
    img6     = models.ImageField(upload_to='photos',null=True, blank=True)
    title    = models.CharField(max_length=255)
    price    = models.PositiveSmallIntegerField("цена", default=2019)
    genres   = models.ManyToManyField(Genre, verbose_name="жанры")
    razdel   = models.ManyToManyField(Razdel, verbose_name="Категория")
    slug     = AutoSlugField(populate_from='title' )
    

    class Meta:
            ordering=['-id']
    def get_absolute_url(self):
            return reverse("blog:Post",args=[self.id,self.slug])



   

        
class Customer(models.Model):
    user       = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone      = models.CharField(max_length=11,blank=True,null=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name  = models.CharField(max_length=30,null=True,blank=True)
    email      = models.EmailField(max_length=255,null=True,blank=True)
    
    class Meta:
            ordering=['-id']
    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)

    
    @receiver(post_save, sender=get_user_model())
    def create_likeCustomer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    
class CustomerLike(models.Model):
    
    likeNEW       =  models.ForeignKey(smartphone,  on_delete=models.CASCADE, null=True,blank=True)
    likeCustomer  =  models.ForeignKey(Customer,    on_delete=models.CASCADE, null=True           )
    created_at    =  models.DateTimeField(          auto_now_add=True,        null=True,blank=True)
    updated_at    =  models.DateTimeField(          auto_now=True,            null=True,blank=True)
    
    class Meta:
            ordering=['-id']
    @receiver(post_save, sender=Customer)
    def create_likeCustomer(sender, instance, created, **kwargs):
        if created:
            # if your user model has phone, if not remove phone.
            CustomerLike.objects.create(likeCustomer=instance)   



class CustomerAddress(models.Model):
    country          =      models.CharField(max_length=30,blank=True)
    town             =      models.CharField(max_length=30,blank=True)   
    address          =      models.CharField(max_length=30,blank=True)     
    house            =      models.CharField(max_length=30,blank=True)  
    apartment        =      models.CharField(max_length=30,blank=True)  
    index            =      models.CharField(max_length=30,blank=True)  
    addressCustomer  =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    class Meta:
            ordering =      ['-id']

class order(models.Model):
    orderCustomer    =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    smartphone       =      models.ManyToManyField(smartphone)
    orderAddress     =      models.ForeignKey(CustomerAddress, on_delete=models.CASCADE,null=True)
    
    class Meta:
            ordering =      ['-id'] 


    
    

    






	

    

