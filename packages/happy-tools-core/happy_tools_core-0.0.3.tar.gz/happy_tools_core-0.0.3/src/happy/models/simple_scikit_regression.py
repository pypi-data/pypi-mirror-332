from happy.models.sklearn import create_model
from happy.models.scikit_spectroscopy import ScikitSpectroscopyModel
from happy.pixel_selectors import MultiSelector, SimpleSelector
from happy.preprocessors import SpectralNoiseInterpolator, PadPreprocessor, SNVPreprocessor, \
    MultiPreprocessor, DerivativePreprocessor, WavelengthSubsetPreprocessor


class SimpleModel(ScikitSpectroscopyModel):

    def __init__(self, data_folder, target):
        regression_method = create_model("linearregression", {})

        pixel_selector0 = SimpleSelector(64, criteria=None)
        train_pixel_selectors = MultiSelector([pixel_selector0])

        subset_indices = list(range(60, 190))
        w = WavelengthSubsetPreprocessor(subset_indices=subset_indices)
        clean = SpectralNoiseInterpolator()
        SNVpp = SNVPreprocessor()
        SGpp = DerivativePreprocessor(window_length=15)
        padp = PadPreprocessor(width=128, height=128, pad_value=0)
        pp = MultiPreprocessor(preprocessor_list=[w, clean, SNVpp, SGpp, padp])

        super().__init__(data_folder, target, additional_meta_data=None, model=regression_method,
                         pixel_selector=train_pixel_selectors, happy_preprocessor=pp)
