from ..datasets.provided_datasets.AdultDatasetLoader import AdultDatasetLoader
from ..datasets.provided_datasets.IonosphereDatasetLoader import IonosphereDatasetLoader
from ..datasets.provided_datasets.IrisDatasetLoader import IrisDatasetLoader
from ..datasets.provided_datasets.TitanicDatasetLoader import TitanicDatasetLoader
from rocelib.datasets.custom_datasets.CsvDatasetLoader import CsvDatasetLoader


def get_example_dataset(name: str):
    """
    Returns a DatasetLoader class given the name of an example dataset

    @param name: the name of the dataset you wish to load, the options are:
                 - iris
                 - ionosphere
                 - adult
                 - titanic

    @return: DatasetLoader
    """
    if name == "iris":
        ds = IrisDatasetLoader()
        ds.load_data()
        return ds
    elif name == "ionosphere":
        ds = IonosphereDatasetLoader()
        ds.load_data()
        ds.default_preprocess()
        return ds
    elif name == "adult":
        ds = AdultDatasetLoader()
        ds.load_data()
        return ds
    elif name == "titanic":
        ds = TitanicDatasetLoader()
        ds.load_data()
        return ds
    elif name == "recruitment":
        ds = CsvDatasetLoader('./assets/recruitment_data.csv', "HiringDecision", 0)
        return ds
    else:
        raise ValueError(f"Unknown dataset: {name}")
