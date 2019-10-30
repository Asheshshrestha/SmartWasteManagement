from django.contrib.auth.models import User



def notice_context(request):
    notice_contexts=[]
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        notice_contexts = user.notifications.unread()[:5]
    return {'notice_contexts':notice_contexts}