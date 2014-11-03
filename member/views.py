from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from member.forms import RegistrationForm, LoginForm
from member.models import Member
from django.contrib.auth import authenticate,login, logout



def MemberRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
#                user = User.objects.create_user( username=form.cleaned_data['username'], email=form.cleaned_data['email'],password=form.cleaned_data['password'],)
                user = User.objects.create_user( username=form.cleaned_data['username'],password=form.cleaned_data['password'],email=form.cleaned_data['email'],)
                user.save()
                member = Member(user=user,name = form.cleaned_data['name'],email=form.cleaned_data['email'],)
                member.save()
                return HttpResponseRedirect('/profile/')
# http://mayukhsaha.wordpress.com/2013/05/09/simple-login-and-user-registration-application-using-django/
# http://runnable.com/UqLQLKmXsSAmAAd5/user-registration-form-with-captcha-using-django-simple-captcha-for-python
        else:
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
    else:
        """ User is not submitting the form , Show them a blank registration form  """
        form = RegistrationForm()
        context = {'form':form}
        return render_to_response('register.html', context,context_instance=RequestContext(request))


@login_required
def Profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    member = request.user
    context = {'member':member}
    return render_to_response('profile.html',context,context_instance=RequestContext(request))




def LoginRequest(request):
     if request.user.is_authenticated():
         return HttpResponseRedirect('/profile/')
     if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             member = authenticate(username=username,password=password)
             if member is not None:
                 login(request,member)
                 return HttpResponseRedirect('/profile/')
             else:
                 return render_to_response('login.html',{'form': form}, context_instance=RequestContext(request))
         else:
             return render_to_response('login.html',{'form': form}, context_instance=RequestContext(request))



     else:
         ''' User is not bunmitting the form , show login form '''
         form = LoginForm()
         context = {'form':form}
         return render_to_response('login.html', context, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')