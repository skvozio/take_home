import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from job_application.models import JobApplication
from job_application.serializers import JobApplicationSerializer

client = Client()


class GetAllApplications(TestCase):
    def setUp(self):
        JobApplication.objects.create(
            title="Junior developer",
            company_name="Super Company",
            was_referred=True,
            contact_name="Sandy Claws",
            salary=45000,
            address="123, Quick str., Vancouver",
            date_applied="2021-02-07"
        )
        JobApplication.objects.create(
            title="Software engineer",
            company_name="Good Company",
            was_referred=False,
            contact_name="Amanda Palmer",
            salary=47000,
            address="123, Quick str., Vancouver",
            date_applied="2021-02-07"
        )

    def test_all_applications(self):
        response = client.get(reverse("api:applications-list"))
        # get data from db
        applications = JobApplication.objects.all()
        serializer = JobApplicationSerializer(applications, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetApplicationByID(TestCase):
    def setUp(self):
        self.junior = JobApplication.objects.create(
            title="Junior developer",
            company_name="Super Company",
            was_referred=True,
            contact_name="Sandy Claws",
            salary=45000,
            address="123, Quick str., Vancouver",
            date_applied="2021-02-07"
        )
        self.engineer = JobApplication.objects.create(
            title="Software engineer",
            company_name="Good Company",
            was_referred=False,
            contact_name="Amanda Palmer",
            salary=47000,
            address="123, Quick str., Vancouver",
            date_applied="2021-02-07"
        )

    def test_get_application_by_id(self):
        response = client.get(reverse("api:applications-detail", kwargs={"pk": self.engineer.pk}))
        application = JobApplication.objects.get(pk=self.engineer.pk)
        serializer = JobApplicationSerializer(application)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_application_by_invalid_id(self):
        response = client.get(reverse("api:applications-detail", kwargs={"pk": 15}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.dumps({"detail": "Not found."}), json.dumps(response.data))

    def test_get_application_by_query_string(self):
        url = reverse("api:applications-list") + '?title=Software'
        response = client.get(url)
        serializer = JobApplicationSerializer(self.engineer)
        self.assertEqual(response.data[0], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewPuppyTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'title': 'Project Manager',
            'company_name': 'Microsoft',
            'url': 'http://linked.in/jobs/12321',
            'was_referred': True,
            'contact_name': 'Nicolas Page',
            'salary': 120000,
            'address': "Somewhere in Bellevue",
        }
        self.invalid_payload = {
            'title': '',
            'company_name': 'Microsoft',
            'url': 'http://linked.in/jobs/12321',
            'was_referred': False,
            'contact_name': 'Nicolas Page',
            'salary': 120000,
            'address': "Somewhere in Bellevue",
        }

    def test_create_valid_application(self):
        response = client.post(
            reverse('api:applications-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_application(self):
        response = client.post(
            reverse('api:applications-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



