"""
XNLI: Evaluating Cross-lingual Sentence Representations
https://arxiv.org/abs/1809.05053

Based on the implementation of @yongzx (see https://github.com/EleutherAI/lm-evaluation-harness/pull/258)

Prompt format (same as XGLM and mGPT):

sentence1 + ", right? " + mask = (Yes|Also|No) + ", " + sentence2

Predicition is the full sequence with the highest likelihood.

Language specific prompts are translated word-by-word with Google Translate
and may differ from the ones used by mGPT and XGLM (they do not provide their prompts).

Homepage: https://github.com/facebookresearch/XNLI
"""
from .xnli import XNLIBase

_CITATIONS = """
@InProceedings{conneau2018xnli,
  author = "Conneau, Alexis
        and Rinott, Ruty
        and Lample, Guillaume
        and Williams, Adina
        and Bowman, Samuel R.
        and Schwenk, Holger
        and Stoyanov, Veselin",
  title = "XNLI: Evaluating Cross-lingual Sentence Representations",
  booktitle = "Proceedings of the 2018 Conference on Empirical Methods
               in Natural Language Processing",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  location = "Brussels, Belgium",
}
"""

_LANG = [
    "ar",
    "bg",
    "de",
    "el",
    "es",
    "fr",
    "hi",
    "ru",
    "sw",
    "th",
    "tr",
    "ur",
    "vi",
    "zh",
]

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
        f"xnli-mt_{model}_{lang}": create_task(model, lang)
        for lang in _LANG
        for model in _MODELS
    }


def create_task(model, lang):
    class XNLIBase_MT(XNLIBase):
        DATASET_PATH = "juletxara/xnli_mt"
        DATASET_NAME = model
        QUESTION_WORD = "right"
        ENTAILMENT_LABEL = "Yes"
        NEUTRAL_LABEL = "Also"
        CONTRADICTION_LABEL = "No"

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

    return XNLIBase_MT
