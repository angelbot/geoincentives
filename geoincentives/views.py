from coffin.shortcuts import render_to_response as jinja2_render_to_response
from geoincentives.forms import UserLoginForm

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from geoincentives.models import User

def home(request):

    context = {}
    context.update(csrf(request))

    return jinja2_render_to_response(
        'home.html', context
    )

@login_required(login_url='/login/')
def checkin(request):

    print request.session
    from IPython import embed; embed()

    events = [] request.user.get_nearby_events()

    return jinja2_render_to_response(
        'checkin.html', {
            'events': events,
        }
    )
