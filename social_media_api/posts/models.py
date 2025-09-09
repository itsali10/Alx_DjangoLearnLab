from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.TextField()

    def __str__(self):
        return f'Post by {self.author.username} at {self.created_at}' 
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='likes')
    
    def __str__(self):
        return f'Like by {self.user.username} on {self.post.title}'