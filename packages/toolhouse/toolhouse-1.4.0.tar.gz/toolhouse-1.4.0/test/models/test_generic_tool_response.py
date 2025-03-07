# This file was generated by liblab | https://liblab.com/
# pylint: disable=C0116, C0115

import unittest
from src.toolhouse.models.GenericToolCallResults import GenericToolCallResults


class TestGenericToolResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)  # pylint: disable=W1503

    def test_generic_tool_response(self):
        # Create GenericToolResponse class instance
        test_model = GenericToolCallResults(content="blanditiis")
        self.assertEqual(test_model.content, "blanditiis")

    def test_generic_tool_response_required_fields_missing(self):
        # Assert GenericToolResponse class generation fails without required fields
        with self.assertRaises(TypeError):
            # pylint: disable=E1120, W0612
            test_model = GenericToolCallResults()  # noqa: F841


if __name__ == "__main__":
    unittest.main()
