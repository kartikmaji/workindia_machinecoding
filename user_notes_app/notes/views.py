from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from notes.models import Notes
import json
from .helpers import parse_request_data

# pintu = User.objects.create_user("pint2", "pintu@swiggy.com", "password")
# notes1 = Notes.create("hello", pintu)

# Create your views here.
@require_http_methods(["POST"])
@csrf_exempt
def registration(request):
    request_data = parse_request_data(request)
    if request_data == None:
        return HttpResponseBadRequest("bad request")    
    
    try:
        # creating user with same username will give integrity error
        # will give bad request in response
        new_user = User.objects.create_user(request_data['username'], request_data['password'])
    except Exception as e:
        print("Error creating new user: %s", e)
        return HttpResponseBadRequest("bad request")
    return JsonResponse({'status': 'account created'})

@require_http_methods(["POST"])
@csrf_exempt
def login(request):
    request_data = parse_request_data(request)
    if request_data == None:
        return HttpResponseBadRequest("bad request")
    
    try:
        user = authenticate(username=request_data['username'], password=request_data['password'])
        if user is None:
            return JsonResponse({'status': 'error', 'description': 'invalid credentials'})
        else:
            return JsonResponse({'status': 'ok', 'userId': user.username})
    except Exception as e:
        print("Error logging in user: ", e)
        return HttpResponseBadRequest("bad request")
    return JsonResponse()

@require_http_methods(["GET"])
def list_notes(request):
    request_data = parse_request_data(request)
    if request_data == None:
        return HttpResponseBadRequest("bad request")
    
    try:
        user = User.objects.get(username=request_data['user'])
        if user is None:
            return JsonResponse({'status': 'error', 'description': 'invalid credentials'})
        else:
            notes = Notes.objects.filter(owner=user)
            return JsonResponse([{'id': note.id, 
                'owner': note.owner.username,
                'name': note.content, 
                'created_at': note.creation_date} for note in notes], safe=False)
    except Exception as e:
        print("Error getting in list of notes: ", e)
        return HttpResponseBadRequest()
    return JsonResponse({'status': 'ok'})

@require_http_methods(["POST"])
@csrf_exempt
def new_note(request):
    request_data = parse_request_data(request)
    if request_data == None:
        return HttpResponseBadRequest("bad request")

    try:
        user = User.objects.get(username=request_data['user'])
        if user is None:
            return JsonResponse({'status': 'error', 'description': 'invalid credentials'})
        else:
            notes = Notes.objects.create(content=request_data['note'], owner=user)
            return JsonResponse({'status': 'success'})
    except Exception as e:
        print("Error creating notes: ", e)
        return HttpResponseBadRequest()
    return JsonResponse({'status': 'ok'})