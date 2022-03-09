from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
from django.contrib.auth.models import User
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post #Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   #we use this to ensure that only login users can create post



# function-base views for the blog
def jobpage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'jobs/index.html', context)

# CLASS-BASED VIEWS for the blog
# this lists the blog for us
class PostListView(ListView):
    model = Post
    template_name = 'jobs/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # to order the post in latest to older
    paginate_by = 6

#User's post list to list the post of a particular user
class UserPostListView(ListView):
    model = Post
    template_name = 'jobs/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



# this goes to the detail of each post
# where we use object.title instead of post.title
class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content']



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #this allows the current logged in user to create post
    #remember we must also create post_form.html file
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'jobs/post_form.html' #added by olu

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #we add this to check if the author of the post
    # is the one trying to edit it if not it wont work
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

 # capability to delete our post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
  #this function also ensures that the current
    # login user that want to delete the post is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#class AddCategoryView(CreateView):
 #   model = Category
 #   template_name = 'blog/post_category_form.html'
 #   fields = '__all__'
 #   success_url = '/'

