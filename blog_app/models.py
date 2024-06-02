from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True) # save time when instance is created
    updated_at = models.DateTimeField(auto_now = True) # save time when .save() is called (instance is updated)

    def __str__(self):
        return self.name
    
    def edit(self, name, desc, img):
        self.name = name
        self.description = desc
        self.image = img

    # generate short description if description is greater than 50 words.
    def short_description(self):
        words = self.description.split()
        if (len(words) > 50):
            return ' '.join(words[:30]) + '...' # join the first thirty words with a ' ' (space) between each word
                                                # and add '...' at the end to indicate truncation happened.
        return self.description

