from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  
from datetime import datetime
from classcast.classcast_test_submissions.models import Classcast_student_info

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

@csrf_exempt
def updateprofile(request):
	# if not request.user.is_authenticated():
	# 	return JsonResponse({'status': 'False', 'Message': 'Not authenticated'})

	if(request.method == "GET"):
		return JsonResponse({'status': 'False', 'message': 'Get request'})

	try:

		# student_id = request.user.id
		student_id = int(request.POST.get('student_id'))
		pincode = int(request.POST.get('pincode'))
		standard = int(request.POST.get('standard'))
		stream = request.POST.get('stream')
		marks_scored_in_last_degree = float(request.POST.get('marks_scored_in_last_degree'))
	
		if Classcast_student_info.objects.filter(student_id=student_id).exists():
			student_info = Classcast_student_info.objects.get(student_id=student_id)
		else:
			student_info = Classcast_student_info(student_id=student_id, 
				total_time_spent_on_platform=0.0,
				active_status='active', last_active=datetime.now() ,
				total_karma_points=0.0)

		student_info.pincode = pincode
		student_info.standard = standard
		student_info.stream = stream
		student_info.marks_scored_in_last_degree = marks_scored_in_last_degree

		student_info.save()

		return JsonResponse({'status': 'True', 'message': 'Successfully created/updated'})

	except Exception, e:
		return JsonResponse({'status': 'False', 'message': 'Database error'})
