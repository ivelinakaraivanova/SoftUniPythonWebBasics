from expenses_tracker.expenses.models import Expenses
from expenses_tracker.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        expenses = Expenses.objects.all()
        profile.budget_left = profile.budget - sum(e.price for e in expenses)
        return profile

