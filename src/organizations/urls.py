from django.urls import include, path

from . import views

urlpatterns = [
    path('organizations/', include(([
        path('', views.organization_list, name='list'),
        path('api/organizations/', views.org_collection, name='collection'),
        path('<uuid:slug>/', views.my_organizations, name='my-orgs'),
        path('<uuid:slug>/view/', views.organization_details, name='org-details'),
        path('create/', views.create_organization, name='org-new'),
        path('send-request/', views.send_org_request, name='org-request'),
        path('response/', views.org_response, name='org-response'),
    ], 'organizations'))),
]
