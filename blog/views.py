from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, SignInForm

# Create your views here.

# All Posts


class Posts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

# Single Post


class PostDetail(View):
    template_name = "blog/post-detail.html"
    model = Post

    # Helper function for checking if a post has been bookmarked
    def is_stored_post(self, request, post_id: int):
        session_posts = request.session.get("stored_posts")
        if session_posts:
            is_read_later = post_id in session_posts
        else:
            is_read_later = False
        return is_read_later

    def get_context(self, request, post, comment_form):
        return {
            "post": post,
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-date"),
            "is_read_later": self.is_stored_post(request, post.id),
        }

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post-detail.html", self.get_context(request, post, CommentForm()))

    # Post request occur when users comment on a post
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        # Only allow comments from users that are logged in
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("sign-in"))

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            return HttpResponseRedirect(reverse("post", args=[slug]))
        else:
            return render(request, "blog/post-detail.html", self.get_context(request, post, comment_form))


class ReadLaterView(View):

    # Loads list of bookmarked posts
    def get(self, request):
        session_posts = request.session.get("stored_posts")

        context = {}

        if session_posts:
            posts = Post.objects.filter(id__in=session_posts)
            context["posts"] = posts
            context["has_posts"] = True

        else:
            context["posts"] = []
            context["has_posts"] = False

        return render(request, "blog/bookmark.html", context)

    # Adding a post to a list of bookmarked posts
    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        id = int(request.POST["post_id"])

        if id in stored_posts:
            stored_posts.remove(id)
        else:
            stored_posts.append(id)

        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect(reverse("post", args=[request.POST["post_slug"]]))


class Index(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        return super().get_queryset()[:3]


class SignUp(View):
    def get(self, request):
        # Using django's default user creation form
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "blog/sign-up.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {"form": form}
            return render(request, "blog/sign-up.html", context)


class SignIn(View):
    def get(self, request):
        context = {"form": SignInForm()}
        return render(request, "blog/sign-in.html", context)

    def post(sekf, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get(
                "username"), password=form.cleaned_data.get("password"))
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                context = {
                    "form": form,
                    "login_failed": True
                }
                return render(request, "blog/sign-in.html", context)
        else:
            context = {"form": form}
            return render(request, "blog/sign-in.html", context)


def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
