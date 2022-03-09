from django.db import models
from django.urls import reverse
from django.utils import timezone #for the Datetimefield
from django.contrib.auth.models import User #since our users are going to be making the post
from ckeditor.fields import RichTextField
#from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import Profile
from django.shortcuts import get_object_or_404, render



class Post(models.Model):
    title = models.CharField(max_length=100)
    #content = RichTextField(blank=True, null=True)   #without the image upload capability
    content = RichTextUploadingField()
    #content = models.TextField()   ---this display a text area without formatting
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #One to many relationship
    #category = models.CharField(choices=choice_list, max_length=255, default='uncategorized')
    slug = models.SlugField(null=True, unique=True)


    def __str__(self):
        return self.title



#******************************************
#limiting the entry of individual user in the post, each user cannot post more than 5
    def save(self, *args, **kwargs):
        if self.__class__.objects.filter(author=self.author).count() >= 5:
            raise ValueError('You have exceded your post limit')
            return None   #want it to return validation error
        return super(Post, self).save(*args, **kwargs)
        # return super().save(*args, **kwargs) python3.x
 #****************************************************

    #we add this to redirect us to the new post page
    # once new post is created, we need a return reverse
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

#*********************
    #using the slug to
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug':self.slug})
    #**************************



def create_slug(instance, new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)



