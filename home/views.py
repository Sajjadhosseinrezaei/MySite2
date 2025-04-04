from django.shortcuts import render, redirect
from django.views import View
from .models import Project, Skill
from .forms import SendMailForm
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


class ProjectAndSkillListView(View):
    form_class = SendMailForm
    template_name = 'home/home.html'

    def get(self, request):
        context = {
            'projects': Project.objects.all(),
            'skills': Skill.objects.all(),
            'form': self.form_class(),
        }
        return render(request, self.template_name, context)
    
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
        context = {
            'projects': Project.objects.all(),
            'skills': Skill.objects.all(),
            'form': form,
        }

            
        return render(request, self.template_name, context)

    