from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  
from datetime import datetime
from classcast.classcast_test_submissions.models import Classcast_student_info
from django.contrib.auth.models import User
from common.djangoapps.student.models import UserProfile

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
		# username = request.POST.get('username')
		student_id = int(request.POST.get('student_id'))
		
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		
		pincode = int(request.POST.get('pincode'))
		standard = int(request.POST.get('standard'))
		stream = request.POST.get('stream')
		marks_scored_in_last_degree = float(request.POST.get('marks_scored_in_last_degree'))
		DOB = float(request.POST.get('DOB'))
		phone_number = request.POST.get('phone_number') 
		
		gender = request.POST.get('gender')
	
		

		if Classcast_student_info.objects.filter(student_id=student_id).exists():
			student_info = Classcast_student_info.objects.get(student_id=student_id)
		else:
			student_info = Classcast_student_info(student_id=student_id, 
				total_time_spent_on_platform=0.0,
				active_status='active', last_active=datetime.now() ,
				total_karma_points=0.0)

		user = User.objects.get(id=student_id)
		user_profile = UserProfile.objects.get(user_id=student_id)

		if first_name is not None:
			user.first_name = first_name
		if last_name is not None:
			user.last_name = last_name
		if (first_name is not None) and (last_name is not None):
			user_profile.name = first_name + ' ' + last_name
		if pincode is not None:
			student_info.pincode = pincode
		if standard is not None:
			student_info.standard = standard	
		if stream is not None:
			student_info.stream = stream
		if marks_scored_in_last_degree is not None:
			student_info.marks_scored_in_last_degree = marks_scored_in_last_degree
		if DOB is not None:
			student_info.DOB = DOB
		if phone_number is not None:
			student_info.phone_number = phone_number
		if gender is not None:
			user_profile.gender = gender



		student_info.save()
		user.save()
		user_profile.save()

		return JsonResponse({'status': 'True', 'message': 'Successfully created/updated'})

	except Exception, e:
		return JsonResponse({'status': 'False', 'message': 'Database error'})
