from django.contrib.auth.mixins import UserPassesTestMixin


class AdminRequiredMixin(UserPassesTestMixin):
    """
    Mixin to restrict access to staff (admin) users only.
    """

    def test_func(self):
        """Return True if the current user is staff/admin."""
        return self.request.user.is_staff
