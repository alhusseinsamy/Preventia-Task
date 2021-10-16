from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.FileField(upload_to='post_images')
    normal_user = models.ForeignKey('usersApp.NormalUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def likes_count(self):
        likes = self.like_set
        count = likes.count()
        return count
    
    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    text = models.TextField()
    normal_user = models.ForeignKey('usersApp.NormalUser', on_delete=models.CASCADE)
    post = models.ForeignKey('socialApp.Post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    normal_user = models.ForeignKey('usersApp.NormalUser', on_delete=models.CASCADE)
    post = models.ForeignKey('socialApp.Post', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['normal_user', 'post'], name='like user post constraint')
        ]

    def __str__(self):
        return str(self.id)


