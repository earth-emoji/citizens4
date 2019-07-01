import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .forms import OrganizationForm
from .models import Organization, OrganizationRequest
from .serializers import OrganizationSerializer
from accounts.models import UserProfile

# Create your views here.
def my_organizations(request, slug, template_name='organizations/org-list.html', data={}):
    founder = UserProfile.objects.get(slug=slug, user=request.user)
    organizations = Organization.objects.filter(founder=founder)
    data["organizations"] = organizations
    return render(request, template_name, data)


def create_organization(request, template_name="organizations/org_form.html", data={}):
    form = OrganizationForm(request.POST or None)
    if form.is_valid():
        organization = Organization.objects.create(
            name = form.cleaned_data['name'],
            description = form.cleaned_data['description'],
            founder = request.user.profile
        )
        organization.save()
        return redirect('organizations:my-orgs', request.user.profile.slug)
    data["form"] = form
    data["type"] = "organization"
    return render(request, template_name, data)


def organization_list(request, template_name='organizations/org-list.html', data={}):
    organizations = Organization.objects.all()
    data["organizations"] = organizations
    return render(request, template_name, data)


def organization_details(request, slug, template_name='organizations/details.html', data={}):
    organization = get_object_or_404(Organization, slug=slug)
    requests = OrganizationRequest.objects.filter(organization=organization).exclude(status=True)
    data['organization'] = organization
    data["requests"] = requests
    return render(request, template_name, data)

def send_org_request(request):
    user = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        org_id = request.POST['organization']
        org = Organization.objects.get(pk=org_id)
        group_request = OrganizationRequest.objects.create(organization=org, prospect=user)
        data = {'message': 'Your request has been sent!'}
        return JsonResponse(data)
    # return response
    return HttpResponse('')

def org_requests(request, pk, template_name='organizations/requests.html', data = {}):
    organization = get_object_or_404(Organization, pk=pk)
    requests = OrganizationRequest.objects.filter(organization=organization).exclude(status=True)
    
    data["organization"] = organization
    data["org_requests"] = requests
    return render(request, template_name, data)

def org_response(request):

    if request.method == 'POST':
        group_id = request.POST['organization']
        prospect_id = request.POST['prospect']

        organization = Organization.objects.get(pk=group_id)
        prospect = UserProfile.objects.get(pk=prospect_id)

        # get request
        org_request = OrganizationRequest.objects.get(organization=organization, prospect=prospect)

        # update request
        org_request.status = True
        org_request.save()
        Membership.objects.create(organization=organization, person=prospect)
        message = "%s has been added to %s" %(prospect.user.name, organization.name)
        data = {'message': message}
        return JsonResponse(data)
     # return response
    return HttpResponse('')


@api_view(['GET', 'POST'])
def org_collection(request):
    if request.method == 'GET':
        organizations = Organization.objects.filter(founder=request.user.profile)
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'descsription': request.data('desc'),
            'founder': request.user.profile.pk
        }
        serializer = OrganizationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
