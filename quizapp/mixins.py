from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from user.choices import UserType


class StudentRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.user_type != UserType.STUDENT:
            raise PermissionDenied
        return super(StudentRequiredMixin, self).dispatch(request, *args, **kwargs)


class TeacherRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.user_type != UserType.TEACHER:
            raise PermissionDenied
        return super(TeacherRequiredMixin, self).dispatch(request, *args, **kwargs)


class TeacherAndStudentRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.user_type != UserType.TEACHER and user.user_type != UserType.STUDENT:
            raise PermissionDenied
        return super(TeacherAndStudentRequiredMixin, self).dispatch(request, *args, **kwargs)
