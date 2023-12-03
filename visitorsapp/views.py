from django.shortcuts import render, HttpResponse

# import statement using relative import
from .models import Post

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]

# Create your views here.
def home(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }
    return render(request, 'visitors/home.html', context)

def about(request):
    return render(request, 'visitors/about.html')
    # return render(request, "about.html")

# if __name__ == "__main__":
#     Your main script logic here
#     pass