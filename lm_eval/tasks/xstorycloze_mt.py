"""
Few-shot Learning with Multilingual Language Models
https://arxiv.org/abs/2112.10668

XStoryCloze consists of the professionally translated version of the [English StoryCloze dataset](https://cs.rochester.edu/nlp/rocstories/) (Spring 2016 version) to 10 non-English languages. This dataset is released by Meta AI.
Homepage: https://github.com/facebookresearch/fairseq/pull/4820
"""
from .storycloze import StoryCloze


_CITATION = """
@article{DBLP:journals/corr/abs-2112-10668,
  author    = {Xi Victoria Lin and
               Todor Mihaylov and
               Mikel Artetxe and
               Tianlu Wang and
               Shuohui Chen and
               Daniel Simig and
               Myle Ott and
               Naman Goyal and
               Shruti Bhosale and
               Jingfei Du and
               Ramakanth Pasunuru and
               Sam Shleifer and
               Punit Singh Koura and
               Vishrav Chaudhary and
               Brian O'Horo and
               Jeff Wang and
               Luke Zettlemoyer and
               Zornitsa Kozareva and
               Mona T. Diab and
               Veselin Stoyanov and
               Xian Li},
  title     = {Few-shot Learning with Multilingual Language Models},
  journal   = {CoRR},
  volume    = {abs/2112.10668},
  year      = {2021},
  url       = {https://arxiv.org/abs/2112.10668},
  eprinttype = {arXiv},
  eprint    = {2112.10668},
  timestamp = {Tue, 04 Jan 2022 15:59:27 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2112-10668.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_LANG = ["ru", "zh", "es", "ar", "hi", "id", "te", "sw", "eu", "my"]
_MODELS = [
    "nllb-200-distilled-600M",
    "nllb-200-distilled-1.3B",
    "nllb-200-1.3B",
    "nllb-200-3.3B",
]


def create_all_tasks():
    """Creates a dictionary of tasks from a list of subjects
    :return: {task_name: task}
    """
    return {
        f"xstory_cloze-mt_{model}_{lang}": create_task(model, lang)
        for lang in _LANG
        for model in _MODELS
    }


def create_task(model, lang):
    class XStoryCloze_MT(StoryCloze):
        DATASET_PATH = "juletxara/xstory_cloze_mt"
        DATASET_NAME = model

        def __init__(self):
            super().__init__(data_dir="")

        def has_training_docs(self):
            return False

        def has_validation_docs(self):
            return True

        def has_test_docs(self):
            return False

        def training_docs(self):
            pass

        def validation_docs(self):
            return self.dataset[lang]

        def test_docs(self):
            pass

    return XStoryCloze_MT
