from aim5005.features import MinMaxScaler, StandardScaler, LabelEncoder
import numpy as np
import unittest
from unittest.case import TestCase

### TO NOT MODIFY EXISTING TESTS

class TestFeatures(TestCase):
    def test_initialize_min_max_scaler(self):
        scaler = MinMaxScaler()
        assert isinstance(scaler, MinMaxScaler), "scaler is not a MinMaxScaler object"
        
        
    def test_min_max_fit(self):
        scaler = MinMaxScaler()
        data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
        scaler.fit(data)
        assert (scaler.maximum == np.array([1., 18.])).all(), "scaler fit does not return maximum values [1., 18.] "
        assert (scaler.minimum == np.array([-1., 2.])).all(), "scaler fit does not return maximum values [-1., 2.] " 
        
        
    def test_min_max_scaler(self):
        data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
        expected = np.array([[0., 0.], [0.25, 0.25], [0.5, 0.5], [1., 1.]])
        scaler = MinMaxScaler()
        scaler.fit(data)
        result = scaler.transform(data)
        assert (result == expected).all(), "Scaler transform does not return expected values. All Values should be between 0 and 1. Got: {}".format(result.reshape(1,-1))
        
    def test_min_max_scaler_single_value(self):
        data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
        expected = np.array([[1.5, 0.]])
        scaler = MinMaxScaler()
        scaler.fit(data)
        result = scaler.transform([[2., 2.]]) 
        assert (result == expected).all(), "Scaler transform does not return expected values. Expect [[1.5 0. ]]. Got: {}".format(result)
        
    def test_standard_scaler_init(self):
        scaler = StandardScaler()
        assert isinstance(scaler, StandardScaler), "scaler is not a StandardScaler object"
        
    def test_standard_scaler_get_mean(self):
        scaler = StandardScaler()
        data = [[0, 0], [0, 0], [1, 1], [1, 1]]
        expected = np.array([0.5, 0.5])
        scaler.fit(data)
        assert (scaler.mean == expected).all(), "scaler fit does not return expected mean {}. Got {}".format(expected, scaler.mean)
        
    def test_standard_scaler_transform(self):
        scaler = StandardScaler()
        data = [[0, 0], [0, 0], [1, 1], [1, 1]]
        expected = np.array([[-1., -1.], [-1., -1.], [1., 1.], [1., 1.]])
        scaler.fit(data)
        result = scaler.transform(data) 

        assert (result == expected).all(), "Scaler transform does not return expected values. Expect {}. Got: {}".format(expected.reshape(1,-1), result.reshape(1,-1))
        
    def test_standard_scaler_single_value(self):
        data = [[0, 0], [0, 0], [1, 1], [1, 1]]
        expected = np.array([[3., 3.]])
        scaler = StandardScaler()
        scaler.fit(data)
        result = scaler.transform([[2., 2.]]) 
        assert (result == expected).all(), "Scaler transform does not return expected values. Expect {}. Got: {}".format(expected.reshape(1,-1), result.reshape(1,-1))

    # TODO: Add a test of your own below this line
    
    def test_standard_scaler_fit_transform(self):
    # Test that fit_transform produces the same result as fit followed by transform
        data = [[1, 2], [3, 4], [5, 6]]
    
        scaler1 = StandardScaler()
        result_fit_transform = scaler1.fit_transform(data)
    
        scaler2 = StandardScaler()
        scaler2.fit(data)
        result_transform = scaler2.transform(data)
    
    # Using np.allclose for floating point comparisons
        assert np.allclose(result_fit_transform, result_transform), (
            f"fit_transform and fit/transform results differ. fit_transform returned: {result_fit_transform}, "
            f"fit then transform returned: {result_transform}"
        )

    def test_label_encoder_example(self):
    

    
        data = [3, 1, 2, 3, 1]
        
        
        expected_classes = np.array([1, 2, 3])
        
        encoder = LabelEncoder()
        encoder.fit(data)
        assert np.array_equal(encoder.classes_, expected_classes), (
            f"Expected classes_ to be {expected_classes}, got {encoder.classes_}"
        )
    
        expected_transformed = np.array([2, 0, 1, 2, 0])
        transformed = encoder.transform(data)
        assert np.array_equal(transformed, expected_transformed), (
            f"Expected transform to return {expected_transformed}, got {transformed}"
        )
   
        encoder2 = LabelEncoder()
        fit_transformed = encoder2.fit_transform(data)
        assert np.array_equal(fit_transformed, expected_transformed), (
            f"Expected fit_transform to return {expected_transformed}, got {fit_transformed}"
        )
if __name__ == '__main__':
    unittest.main()