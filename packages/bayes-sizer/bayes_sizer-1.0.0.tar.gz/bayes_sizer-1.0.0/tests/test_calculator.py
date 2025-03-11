import pytest
from bayes_sizer.calculator import bayesian_sample_size

def test_bayesian_sample_size():
    """Test Bayesian sample size function returns a valid integer."""
    sample_size = bayesian_sample_size(prior_a=2, prior_b=2, min_effect=0.02, power=0.9, loss_threshold=0.01)
    assert isinstance(sample_size, int)
    assert sample_size > 0
