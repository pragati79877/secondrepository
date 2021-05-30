from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from blog.forms import EmailSendForm
# Create your views here.
def post_list_view(r):
    post_list=Post.objects.all()
    paginator = Paginator(post_list,2)
    page_number=r.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage :
        post_list=paginator.page(paginator.num_pages)
    return render(r,'blog/post_list.html',{'post_list':post_list})
def post_detail_view(r,year,month,day,post):
   post=get_object_or_404(Post,slug=post,
                            status='publish',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,)


   return render(r,'blog/post_detail.html',{'post':post})


def mail_send_view(r,id):
    post= get_object_or_404(Post,id=id,status='publish')
    sent=False
    if r.method=='POST':
        form=EmailSendForm(r.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail('subject','message','durga@blog.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(r,'blog/sharebymail.html',{'form':form,'post':post,'sent':sent})
