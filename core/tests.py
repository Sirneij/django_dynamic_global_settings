from django.test import Client, TestCase
from django.urls import reverse

from core.models import GenericSettings


class ModelGenericSettingsTests(TestCase):
    def setUp(self) -> None:
        """Create the setup of the test."""
        self.generic_settings = GenericSettings.objects.create()

    def test_unicode(self) -> None:
        """Test the representation of the model."""
        self.assertEqual(
            str(self.generic_settings),
            f'GenericSettings for {self.generic_settings.id}',
        )

    def test_first_instance(self) -> None:
        """Test first instance function."""
        self.assertEqual(self.generic_settings.id, 1)

    def test_load(self) -> None:
        """Test the load function."""
        self.assertEqual(GenericSettings.load().id, 1)

    def test_many_instances(self) -> None:
        """Test many instances of the model."""

        def test_for_instance() -> None:
            """Test each instance of the model."""
            new_settings = GenericSettings.objects.create()
            self.assertEqual(
                new_settings.default_vpn_provider,
                ['Access', 'CyberGhost', 'ExpressVPN'],
            )
            self.assertEqual(
                new_settings.default_from_email,
                ['admin@dynamic_settings.com', 'user@dynamic_settings.com'],
            )

        test_for_instance()
        test_for_instance()
        test_for_instance()
        self.assertEqual(GenericSettings.objects.count(), 1)


class IndexTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_context(self) -> None:
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.context['generic_settings'], GenericSettings.load())
        self.assertEqual(response.templates[0].name, 'index.html')


class ChangeTestingTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.data_vpn = {'provider_type': 'vpn', 'default_vpn_provider': 'CyberGhost'}
        self.data_email = {
            'provider_type': 'email',
            'default_from_email': 'user@dynamic_settings.com',
        }

    def test_get(self) -> None:
        response = self.client.get(reverse('core:change_settings'))
        self.assertEqual(response.json()['success'], False)

    def test_post_without_data(self) -> None:
        response = self.client.post(reverse('core:change_settings'))
        self.assertEqual(response.json()['success'], False)

    def test_post_with_vpn_data(self) -> None:
        response = self.client.post(
            reverse('core:change_settings'), self.data_vpn, format='json'
        )
        self.assertEqual(response.json()['success'], True)

    def test_post_with_email_data(self) -> None:
        response = self.client.post(
            reverse('core:change_settings'), self.data_email, format='json'
        )
        self.assertEqual(response.json()['success'], True)
