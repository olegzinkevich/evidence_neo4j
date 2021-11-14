from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def inviteOrUserAuthCheck(request):

    print('start inviteOrUserAuthCheck()')
    # checking if user is logged in or if it came by Invite link
    try:
        invite = request.session['invite']
    except:
        invite = None
    print(invite)

    if invite == 'True':
        pass
    elif request.user.is_authenticated:
        pass
    else:
        # return render(request, 'allauth/account/login.html')
        return redirect("/accounts/login")