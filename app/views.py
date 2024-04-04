from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import SCRAP_URL    
from django.contrib import messages
from django.http import HttpResponseBadRequest

def home(request):
    url = SCRAP_URL+'posts/get/?'
    for key, val in request.GET.items() : 
        if val :
            url += f'{key}={val}&'
        
    action = Action(url)
    context = action.get()
    context['pages'] = [i for i in range(1,context['pages']+1)]
 
    return render(request,'index.html',context)

def create(request):
    context = {}
    if request.method == "POST" : 
        data = {}

        for key,val in request.POST.items() : 
            if val :
                if key == 'telegram' : 
                    val = f"https://web.telegram.org/k/#@{val}"
                elif key == 'whatsapp' :
                    val = f'https://wa.me/+2{val}'
                data[key] = val

        url = SCRAP_URL + f'posts/create/'
        action = Action(url=url,data=data)
        action.post()
        
        if action.is_ok:
            messages.success(request,'تم رفع المنشور الخاص بك بنجاح')
            return redirect('home')
        else:
            context['error'] = 'الرجاء التأكد من صحة البيانات'
    return render(request,'create.html',context)


def delete(request):
    if request.method == "POST" : 
        postid = request.POST.get('post_id')
        student_collage_id = request.POST.get('student_collage_id')
        url = SCRAP_URL + f'posts/delete/{postid}/'
        action = Action(url=url,data={'student_id':student_collage_id})
        action.delete()
        if action.is_ok: 
            messages.success(request,'تم حذف المنشور بنجاح')
        else:
            messages.success(request,'لم يتم حذف المنشور لان البيانات التي ادخلتها غير صحيحة')

        return redirect('home')
    else:
        raise HttpResponseBadRequest(request)