from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext, loader, Context
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from smartp.models import park
from smartp.serializers import SmartSerializer

# Create your views here.
def index(request):
	
	a=park.objects.all()
	template = loader.get_template('smartp/index.html')
	context = RequestContext(request,{'c':a})
	return HttpResponse(template.render(context))

def fk(request):
	
	a=park.objects.all()
	template = loader.get_template('smartp/fk.html')
	context = RequestContext(request,{'c':a})
	return HttpResponse(template.render(context))

def update(request):
	p_name=str(request.POST.get('parking_n'))
	p_n=int(request.POST.get('parking_no'))
	p_s=int(request.POST.get('parking_s'))
	a=park.objects.filter(parking_name=p_name)

	for p in a:
		if (p.parking_no)==int(p_n):
			p.status=p_s
			p.save()
			#template = loader.get_template('smartp/fk.html')
			#context = RequestContext(request,{'park':parks})
			#return HttpResponse(template.render(context))

	# a=park(parking_name=p_name,parking_no=p_n,status=p_s)
	# a.save()
	parks=park.objects.all()
	#parks="ketan"

	template = loader.get_template('smartp/index.html')
	context = RequestContext(request,{'park':parks})
	return HttpResponse(template.render(context))

def inde(request):
	parks=park.objects.all()
	template = loader.get_template('smartp/fk.html')
	context = RequestContext(request,{'park':parks})
	return HttpResponse(template.render(context))

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def update_api(request):
	if request.method == 'GET':
		park_objects = park.objects.all()
        serializer = SmartSerializer(park_objects, many=True)
        return JSONResponse(serializer.data)