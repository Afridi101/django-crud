# check the that the user is authenticated or not
def is_auth(request):
    if request.session.has_key('user'):
        return True
    else:
        return False
