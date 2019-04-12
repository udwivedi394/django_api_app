from django.urls import path

from bank.api.bank_api import BranchDetailer, BranchFinder

urlpatterns = [
    path('branch-details/', BranchDetailer.as_view(), name='Branch Details'),
    path('find-branch/', BranchFinder.as_view(), name='Branch Finder')
]
