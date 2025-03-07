from happy.splitters import HappySplitter
from happy.splitters import CrossValidationSplitter, TrainTestSplitter

bf = "/data/fracpete/waikato/happy/test_data/test_ids"
splitter = HappySplitter(bf)
splitter.generate_splits(1, 1, 60.0, 15.0, False, 10.0)
splitter.save_splits_to_json(bf + "/traintest-noreg-current.json")
splitter = HappySplitter(bf)
splitter.generate_splits(1, 1, 60.0, 15.0, True, 10.0)
splitter.save_splits_to_json(bf + "/traintest-reg-current.json")
splitter = HappySplitter(bf)
splitter.generate_splits(10, 10, 60.0, 15.0, False, 10.0)
splitter.save_splits_to_json(bf + "/cv-noreg-current.json")
splitter = HappySplitter(bf)
splitter.generate_splits(10, 10, 60.0, 15.0, True, 10.0)
splitter.save_splits_to_json(bf + "/cv-reg-current.json")

splitter = TrainTestSplitter(bf, False, 60.0, 15.0, holdout_percent=10.0, seed=1)
splitter.generate_splits().save(bf + "/traintest-noreg-new.json")
splitter = TrainTestSplitter(bf, True, 60.0, 15.0, holdout_percent=10.0, seed=1)
splitter.generate_splits().save(bf + "/traintest-reg-new.json")
splitter = CrossValidationSplitter(bf, False, 10, 10, 60.0, 15.0, holdout_percent=10.0, seed=1)
splitter.generate_splits().save(bf + "/cv-noreg-new.json")
splitter = CrossValidationSplitter(bf, True, 10, 10, 60.0, 15.0, holdout_percent=10.0, seed=1)
splitter.generate_splits().save(bf + "/cv-reg-new.json")
