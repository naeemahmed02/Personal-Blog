from django.db import models
from blog.models import Post
from accounts.models import CustomUser

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments', default=0)
    comment_field = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title}"