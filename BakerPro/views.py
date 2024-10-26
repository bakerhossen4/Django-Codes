
from django.http import HttpResponse

def Home( request ):
    return HttpResponse(' Home Page ')
def Contact( request ):
    return HttpResponse('Contact Page')
def Gallery( request ) :
    return HttpResponse('Gallery Page ')