from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST
from accounts import models, forms


@login_required
def get_profile(request):
    profile = models.Profile.objects.get(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


class UserCreateView(generic.CreateView):
    model = User
    form_class = forms.UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        profile = models.Profile.objects.create(user=self.object)
        return response


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = models.Profile
    template_name = "accounts/index.html"

    def get_queryset(self):
        qs = super().get_queryset()
        if "username" in self.request.GET:
            qs = qs.filter(user__username__icontains=self.request.GET["username"])

        return qs


@login_required
@require_POST
def follow(request, pk):
    profile = get_object_or_404(models.Profile, pk=pk)
    current_profile = get_object_or_404(models.Profile, user=request.user)
    current_profile.follows.add(profile)

    # Redirect to the next url. Default to the index view.
    next_url = request.POST.get("next", reverse_lazy("accounts:index"))
    return HttpResponseRedirect(next_url)


@login_required
@require_POST
def unfollow(request, pk):
    profile = get_object_or_404(models.Profile, pk=pk)
    current_profile = get_object_or_404(models.Profile, user=request.user)
    current_profile.follows.remove(profile)

    # Redirect to the next url. Default to the index view.
    next_url = request.POST.get("next", reverse_lazy("accounts:index"))
    return HttpResponseRedirect(next_url)
