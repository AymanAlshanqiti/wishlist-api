
from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):
	
	message = 'You shall not pass'

	def has_object_permission(self, request, view, obj):
		if request.user == obj.added_by:
			return True
		return False