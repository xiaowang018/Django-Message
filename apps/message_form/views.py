from django.shortcuts import render


# Create your views here.
from apps.message_form.models import Message


def message_form(request):
    # all_messages=Message.objects.all()
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        address = request.POST.get("address", "")
        messagetext = request.POST.get("message", "")
        message=Message()
        message.name=name
        message.email=email
        message.address=address
        message.message=messagetext
        message.save()
        return render(request,"message_form.html",{
            "message":message
        })
    if request.method=="GET":
        all_message=Message.objects.filter()
        if all_message:
            message=all_message[0]
            var_dict={
                "message":message
            }
        return render(request,"message_form.html",var_dict)