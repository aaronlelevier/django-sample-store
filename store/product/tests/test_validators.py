import unittest

import pytest
from django.core.exceptions import ValidationError

from product import validators


class ValidatorsTests(unittest.TestCase):
    def test_validate_stars(self):
        assert validators.validate_stars(1) == 1

        assert validators.validate_stars(5) == 5

        with pytest.raises(ValidationError):
            validators.validate_stars(0)

        with pytest.raises(ValidationError):
            validators.validate_stars(6)
