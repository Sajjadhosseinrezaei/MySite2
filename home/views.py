from django.shortcuts import render, redirect
from django.views import View
from .models import Project, Skill
from .forms import SendMailForm
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView

# Create your views here.


class ProjectAndSkillListView(ListView):
    model = Project
    form_class = SendMailForm
    template_name = 'home/home.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.all().order_by('-created')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['form'] = self.form_class()
        return context
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Handle the form submission
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_body = f"نام: {full_name}\nایمیل: {email}\nپیام: {message}"
            send_mail(subject=subject, message=email_body,
                      recipient_list=['sajjadhosseinrezaei@yahoo.com'],
                      from_email=email)
            messages.success(request, 'پیام شما با موفقیت ارسال شد.')
            return redirect('home:home')
        else:
            messages.error(request, 'خطا در ارسال پیام. لطفا دوباره تلاش کنید.')
        context = self.get_context_data()
        context['form'] = form    
        return render(request, self.template_name, context)

    