"""
PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification
https://arxiv.org/abs/1908.11828

The dataset consists of 23,659 human translated PAWS evaluation pairs and
296,406 machine translated training pairs in 6 typologically distinct languages.

Examples are adapted from  PAWS-Wiki

Prompt format (same as in mGPT):

"<s>" + sentence1 + ", right? " + mask + ", " + sentence2 + "</s>",

where mask is the string that matches the label:

Yes, No.

Example:

<s> The Tabaci River is a tributary of the River Leurda in Romania, right? No, The Leurda River is a tributary of the River Tabaci in Romania.</s>

Language specific prompts are translated word-by-word with Google Translate
and may differ from the ones used by mGPT and XGLM (they do not provide their prompts).

Homepage: https://github.com/google-research-datasets/paws/tree/master/pawsx
"""
from .pawsx import PAWSXBase

_CITATION = """
@inproceedings{yang-etal-2019-paws,
    title = "{PAWS}-{X}: A Cross-lingual Adversarial Dataset for Paraphrase Identification",
    author = "Yang, Yinfei  and
      Zhang, Yuan  and
      Tar, Chris  and
      Baldridge, Jason",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1382",
    doi = "10.18653/v1/D19-1382",
    pages = "3687--3692",
}"""

_LANG = [
    "de",
    "es",
    "fr",
    "ja",
    "ko",
    "zh",
]

_MODELS = [
    "nllb-200-distilled-600M",
    "nllb-200-distilled-1.3B",
    "nllb-200-1.3B",
    "nllb-200-3.3B",
    "xglm-564M",
    "xglm-1.7B",
    "xglm-2.9B",
    "xglm-4.5B",
    "xglm-7.5B",
    "bloom-560m",
    "bloom-1b1",
    "bloom-1b7",
    "bloom-3b",
    "bloom-7b1",
    "llama-7B",
    "llama-13B",
    "llama-30B",
    # "llama-65B",
    "RedPajama-INCITE-Base-3B-v1",
    "RedPajama-INCITE-7B-Base",
    "open_llama_3b",
    "open_llama_7b",
    "open_llama_13b",
]


def create_all_tasks():
    """Creates a dictionary of tasks from a list of subjects
    :return: {task_name: task}
    """
    return {
        f"pawsx-mt_{model}_{lang}": create_task(model, lang)
        for lang in _LANG
        for model in _MODELS
    }


def create_task(model, lang):
    class PAWSXBase_MT(PAWSXBase):
        DATASET_PATH = "juletxara/pawsx_mt"
        DATASET_NAME = model
        YES = "Yes"
        NO = "No"
        QUESTION_WORD = "right"

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

    return PAWSXBase_MT
