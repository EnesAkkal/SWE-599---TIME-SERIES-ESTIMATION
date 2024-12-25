import os
import torch
from models import iTransformer, TimeXer, TimeMixer


class Exp_Basic(object):
    def __init__(self, args):
        self.args = args
        # Only include the available models
        self.model_dict = {
            'iTransformer': iTransformer,
            'TimeXer': TimeXer,
            'TimeMixer': TimeMixer
        }

        # Check if the selected model exists in the dictionary
        if self.args.model not in self.model_dict:
            raise ValueError(f"Model {self.args.model} is not supported. Available models: {list(self.model_dict.keys())}")

        # Acquire the device and build the model
        self.device = self._acquire_device()
        self.model = self._build_model().to(self.device)

    def _build_model(self):
        """
        Build the model based on the selected architecture.
        """
        print(f"Building model: {self.args.model}")
        model_class = self.model_dict[self.args.model]
        model = model_class(self.args)  # Assuming models take `args` as input
        return model

    def _acquire_device(self):
        """
        Set up the device for training or testing.
        """
        if self.args.use_gpu:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(
                self.args.gpu) if not self.args.use_multi_gpu else self.args.devices
            device = torch.device(f'cuda:{self.args.gpu}')
            print(f'Using GPU: cuda:{self.args.gpu}')
        else:
            device = torch.device('cpu')
            print('Using CPU')
        return device

    def _get_data(self):
     
        pass

    def vali(self):
      
        pass

    def train(self):
     
        pass

    def test(self):
     
        pass
