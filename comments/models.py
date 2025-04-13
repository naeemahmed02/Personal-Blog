from django.db import models
from blog.models import Post

class Comments(models.Model):
    comment_field = models.TextField()
    # user = None
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now= True)

    # def __str__(self):
    #     return f"Comment by {self.user} on {self.post.title}"