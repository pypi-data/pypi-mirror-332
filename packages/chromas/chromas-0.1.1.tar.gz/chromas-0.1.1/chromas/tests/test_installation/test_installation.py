import unittest

class TestInstalledModules(unittest.TestCase):
    def test_numpy(self):
        try:
            import numpy
        except ImportError:
            self.fail('Numpy not installed')
        try:
            x = numpy.array([1,2,3])
        except:
            self.fail('Numpy not working')
    
    def test_scipy(self):
        try:
            import scipy
        except ImportError:
            self.fail('Scipy not installed')
        try:
            scipy.__version__
        except:
            self.fail('Scipy not working')
    
    def test_pandas(self):
        try:
            import pandas
        except ImportError:
            self.fail('Pandas not installed')
    
    def test_matplotlib(self):
        try:
            import matplotlib
        except ImportError:
            self.fail('Matplotlib not installed')
    
    def test_tqdm(self):
        try:
            import tqdm
        except ImportError:
            self.fail('Tqdm not installed')
    
    def test_pytest(self):
        try:
            import pytest
        except ImportError:
            self.fail('Pytest not installed')
    
    # Custom modules:
    def test_moving_least_squares(self):
        try:
            import moving_least_squares
        except ImportError:
            self.fail('Moving least squares not installed')
    


