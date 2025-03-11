import pytest
from scipy.stats import beta, norm
from bayes_sizer.priors import get_beta_prior, get_normal_prior

def test_get_beta_prior():
    """Test Beta prior distribution."""
    prior = get_beta_prior(2, 5)
    assert isinstance(prior, beta)

def test_get_normal_prior():
    """Test Normal prior distribution."""
    prior = get_normal_prior(mean=0, std=1)
    assert isinstance(prior, norm)
