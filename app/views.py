from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pet , AdoptionApplication, AdoptionEvent,  Donation


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'


# Pet List View
class PetListView(ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'


# Pet Detail View
class PetDetailView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'
    context_object_name = 'pet'


# Pet Create View
class PetCreateView(CreateView):
    model = Pet
    template_name = 'pets/pet_create.html'
    fields = ['name', 'species', 'breed', 'age', 'gender', 'description', 'photo', 'status']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('pet_list')


# Pet Update View
class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'pets/pet_update.html'
    fields = ['name', 'species', 'breed', 'age', 'gender', 'description', 'photo', 'status']

    success_url = reverse_lazy('pet_list')


# Pet Delete View
class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet_delete.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('pet_list')






# Adoption Application List View
class AdoptionApplicationListView(ListView):
    model = AdoptionApplication
    template_name = 'applications/adoption_application_list.html'
    context_object_name = 'applications'

# Adoption Application Detail View
class AdoptionApplicationDetailView(DetailView):
    model = AdoptionApplication
    template_name = 'applications/adoption_application_detail.html'
    context_object_name = 'application'

# Adoption Application Create View
class AdoptionApplicationCreateView(CreateView):
    model = AdoptionApplication
    template_name = 'applications/adoption_application_create.html'
    fields = ['pet', 'reason_for_adoption']

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('adoption_application_list')

# Adoption Application Update View
class AdoptionApplicationUpdateView(UpdateView):
    model = AdoptionApplication
    template_name = 'applications/adoption_application_update.html'
    fields = ['pet', 'reason_for_adoption', 'status']

    success_url = reverse_lazy('adoption_application_list')

# Adoption Application Delete View
class AdoptionApplicationDeleteView(DeleteView):
    model = AdoptionApplication
    template_name = 'applications/adoption_application_delete.html'
    context_object_name = 'application'
    success_url = reverse_lazy('adoption_application_list')




# Adoption Event List View
class AdoptionEventListView(ListView):
    model = AdoptionEvent
    template_name = 'events/adoption_event_list.html'
    context_object_name = 'events'

# Adoption Event Detail View
class AdoptionEventDetailView(DetailView):
    model = AdoptionEvent
    template_name = 'events/adoption_event_detail.html'
    context_object_name = 'event'

# Adoption Event Create View
class AdoptionEventCreateView(CreateView):
    model = AdoptionEvent
    template_name = 'events/adoption_event_create.html'
    fields = ['name', 'description', 'location', 'event_date']

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('adoption_event_detail', kwargs={'pk': self.object.pk})

class AdoptionEventUpdateView(UpdateView):
    model = AdoptionEvent
    fields = ['name', 'description', 'location', 'event_date']
    template_name = 'events/adoption_event_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('adoption_event_detail', kwargs={'pk': self.object.pk})


# Adoption Event Delete View
class AdoptionEventDeleteView(DeleteView):
    model = AdoptionEvent
    template_name = 'events/adoption_event_delete.html'
    context_object_name = 'event'
    success_url = reverse_lazy('adoption_event_list')



# Donation List View
class DonationListView(ListView):
    model = Donation
    template_name = 'donations/donation_list.html'
    context_object_name = 'donations'

# Donation Detail View
class DonationDetailView(DetailView):
    model = Donation
    template_name = 'donations/donation_detail.html'
    context_object_name = 'donation'

# Donation Create View
class DonationCreateView(CreateView):
    model = Donation
    template_name = 'donations/donation_create.html'
    fields = ['amount', 'message']

    def form_valid(self, form):
        form.instance.donor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('donation_list')

# Donation Update View
class DonationUpdateView(UpdateView):
    model = Donation
    template_name = 'donations/donation_update.html'
    fields = ['amount', 'message']

    success_url = reverse_lazy('donation_list')

# Donation Delete View
class DonationDeleteView(DeleteView):
    model = Donation
    template_name = 'donations/donation_delete.html'
    context_object_name = 'donation'
    success_url = reverse_lazy('donation_list')