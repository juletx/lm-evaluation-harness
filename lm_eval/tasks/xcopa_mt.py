"""
XCOPA: A Multilingual Dataset for Causal Commonsense Reasoning
https://ducdauge.github.io/files/xcopa.pdf

The Cross-lingual Choice of Plausible Alternatives dataset is a benchmark to evaluate the ability of machine learning models to transfer commonsense reasoning across languages.
The dataset is the translation and reannotation of the English COPA (Roemmele et al. 2011) and covers 11 languages from 11 families and several areas around the globe.
The dataset is challenging as it requires both the command of world knowledge and the ability to generalise to new languages.
All the details about the creation of XCOPA and the implementation of the baselines are available in the paper.

Homepage: https://github.com/cambridgeltl/xcopa
"""
from .xcopa import XCopa


_CITATION = """
@inproceedings{ponti2020xcopa,
  title={{XCOPA: A} Multilingual Dataset for Causal Commonsense Reasoning},
  author={Edoardo M. Ponti, Goran Glava\v{s}, Olga Majewska, Qianchu Liu, Ivan Vuli\'{c} and Anna Korhonen},
  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2020},
  url={https://ducdauge.github.io/files/xcopa.pdf}
}
"""

_LANG = ["et", "ht", "it", "id", "qu", "sw", "zh", "ta", "th", "tr", "vi"]

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
        f"xcopa-mt_{model}_{lang}": create_task(model, lang)
        for lang in _LANG
        for model in _MODELS
    }


def create_task(model, lang):
    class XCopa_MT(XCopa):
        DATASET_PATH = "juletxara/xcopa_mt"
        DATASET_NAME = model

        def __init__(self):
            super().__init__()

        def has_training_docs(self):
            return False

        def has_validation_docs(self):
            return False

        def has_test_docs(self):
            return True

        def training_docs(self):
            pass

        def validation_docs(self):
            pass

        def test_docs(self):
            return self.dataset[lang]

    return XCopa_MT
