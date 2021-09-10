from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


# def landing_page(request):
#     return render(request, 'landing.html')


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead-list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads
#     }
#     return render(request, 'leads/lead_list.html', context=context)


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = LeadModelForm
    template_name = 'leads/lead_create.html'

    def get_success_url(self):
        return reverse('leads:lead-list')


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {
#         'form': form
#     }
#     return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {
#         'form': form,
#         'lead': lead
#     }
#     return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads/')

# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         print("Receiving post request")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print("Form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print("Lead has been created")
#             return redirect('/leads/')
#     context = {
#         'form': form
#     }
#     return render(request, 'leads/lead_create.html', context)
