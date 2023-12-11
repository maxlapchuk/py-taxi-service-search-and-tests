from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ManufacturerModelTest(TestCase):
    def setUp(self) -> None:
        Manufacturer.objects.create(
            name="BMW",
            country="Germany"
        )

    def test_name_max_length(self):
        manufacturer = Manufacturer.objects.get(id=1)
        max_length = manufacturer._meta.get_field(
            "name"
        ).max_length
        self.assertEqual(max_length, 255)

    def test_country_max_length(self):
        manufacturer = Manufacturer.objects.get(id=1)
        max_length = manufacturer._meta.get_field(
            "country"
        ).max_length
        self.assertEqual(max_length, 255)

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.get(id=1)
        expected_str = f"{manufacturer.name} {manufacturer.country}"
        self.assertEqual(str(manufacturer), expected_str)


class DriverModelTest(TestCase):
    def setUp(self) -> None:
        get_user_model().objects.create(
            username="admin.user",
            password="test123",
            first_name="Admin",
            last_name="User",
            license_number="JOY26458"
        )

    def test_license_number_max_length(self):
        driver = get_user_model().objects.get(id=1)
        max_length = driver._meta.get_field(
            "license_number"
        ).max_length
        self.assertEqual(max_length, 255)

    def test_driver_str(self):
        driver = get_user_model().objects.get(id=1)
        expected_str = (
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )
        self.assertEqual(str(driver), expected_str)

    def test_get_absolute_url(self):
        driver = get_user_model().objects.get(id=1)
        self.assertEqual(
            driver.get_absolute_url(),
            "/drivers/1/"
        )


class CarModelTest(TestCase):
    def setUp(self) -> None:
        manufacturer = Manufacturer.objects.create(
            name="BMW",
            country="Germany"
        )
        Car.objects.create(
            model="X1",
            manufacturer=manufacturer,
        )

    def test_name_max_length(self):
        car = Car.objects.get(id=1)
        max_length = car._meta.get_field(
            "model"
        ).max_length
        self.assertEqual(max_length, 255)

    def test_car_str(self):
        car = Car.objects.get(id=1)
        expected_str = f"{car.model}"
        self.assertEqual(
            str(car), expected_str
        )