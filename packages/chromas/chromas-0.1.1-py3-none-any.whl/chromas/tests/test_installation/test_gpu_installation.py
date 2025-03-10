import unittest

class TestInstalledModules(unittest.TestCase):
    # GPU dependent library installations:
    def test_opencv(self):
        try:
            import cv2
        except ImportError:
            self.fail('OpenCV not installed')
        try:
            _ = cv2.__version__
        except Exception as e:
            self.fail(f'OpenCV not working: {e}')

    def test_torch(self):
        try:
            import torch
        except ImportError:
            self.fail('PyTorch (torch) not installed')
        try:
            _ = torch.__version__
        except Exception as e:
            self.fail(f'PyTorch (torch) not working: {e}')

    def test_torchaudio(self):
        try:
            import torchaudio
        except ImportError:
            self.fail('torchaudio not installed')
        try:
            _ = torchaudio.__version__
        except Exception as e:
            self.fail(f'torchaudio not working: {e}')

    def test_torchmetrics(self):
        try:
            import torchmetrics
        except ImportError:
            self.fail('torchmetrics not installed')
        try:
            _ = torchmetrics.__about__
        except Exception as e:
            self.fail(f'torchmetrics not working: {e}')
