import unittest
from ..app.app import PredictionRequest, predict


class TestPredictionRequest(unittest.TestCase):
    def test_valid_request(self):
        request = PredictionRequest(
            age=30,
            sex="male",
            bmi=25.0,
            children=2,
            smoker=False,
            region="Northeast"
        )

        self.assertTrue(request.is_valid())

    def test_invalid_request(self):
        request = PredictionRequest(
            age=-10,
            sex="invalid",
            bmi="not a number",
            children=100,
            smoker=None,
            region=""
        )

        self.assertFalse(request.is_valid())


class TestPredict(unittest.TestCase):
    def test_predict_success(self):
        request = PredictionRequest(
            age=30,
            sex="male",
            bmi=25.0,
            children=2,
            smoker=False,
            region="Northeast"
        )

        predictions = predict(request)

        self.assertTrue(isinstance(predictions, dict))
        self.assertEqual(len(predictions), 1)
        self.assertIn("predictions", predictions)
        self.assertIsInstance(predictions["predictions"], float)

    def test_predict_invalid_request(self):
        request = PredictionRequest(
            age=-10,
            sex="invalid",
            bmi="not a number",
            children=100,
            smoker=None,
            region=""
        )

        with self.assertRaises(ValueError):
            predict(request)
