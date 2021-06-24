from django.test import TestCase

from django.core.exceptions import ValidationError

from lost_and_found.objects_posts.models import Object


class ObjectTests(TestCase):
    valid_name = 'Object 1'
    valid_image = 'http://image.com'
    valid_width = 500
    valid_height = 1
    valid_weight = 1.5

    def test_when_width_is_less_than3_expect_to_raise(self):

        width = 2

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()

        self.assertIsNotNone(context.exception)

    def test_when_width_is_equal_to3_expect_success(self):

        width = 3

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        obj.full_clean()
        obj.save()

    def test_when_width_is_greater_than600_expect_to_raise(self):

        width = 601

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()

        self.assertIsNotNone(context.exception)

    def test_when_width_is_equal_to600_expect_success(self):

        width = 600

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        obj.full_clean()
        obj.save()

    def test_when_width_is_between_3and600_expect_success(self):

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=self.valid_width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        obj.full_clean()
        obj.save()
