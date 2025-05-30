# BasqBBQ

## Paper

Title: `BasqBBQ: A Bias Benchmark for Question Answering in Basque`

Abstract: https://aclanthology.org/2025.coling-main.318/

The rise of pre-trained language models has revolutionized natural language processing (NLP) tasks, but concerns about the propagation of social biases in these models remain, particularly in under-resourced languages like Basque. This paper introduces BasqBBQ, the first benchmark designed to assess social biases in Basque across eight domains, using a multiple-choice question-answering (QA) task. We evaluate various autoregressive large language models (LLMs), including multilingual and those adapted for Basque, to analyze both their accuracy and bias transmission. Our results show that while larger models generally achieve better accuracy, ambiguous cases remain challenging. In terms of bias, larger models exhibit lower negative bias. However, high negative bias persists in specific categories such as Disability Status, Age and Physical Appearance, especially in ambiguous contexts. Conversely, categories such as Sexual Orientation, Gender Identity, and Race/Ethnicity show the least bias in ambiguous contexts. The continual pre-training based adaptation process for Basque has a limited impact on bias when compared with English. This work represents a key step toward creating more ethical LLMs for low-resource languages.

Homepage: https://github.com/orai-nlp/BasqBBQ

### Citation

```bibtex
@inproceedings{saralegi-zulaika-2025-basqbbq,
    title = "{B}asq{BBQ}: A {QA} Benchmark for Assessing Social Biases in {LLM}s for {B}asque, a Low-Resource Language",
    author = "Zulaika, Muitze  and
      Saralegi, Xabier",
    editor = "Rambow, Owen  and
      Wanner, Leo  and
      Apidianaki, Marianna  and
      Al-Khalifa, Hend  and
      Eugenio, Barbara Di  and
      Schockaert, Steven",
    booktitle = "Proceedings of the 31st International Conference on Computational Linguistics",
    month = jan,
    year = "2025",
    address = "Abu Dhabi, UAE",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.coling-main.318/",
    pages = "4753--4767"
}
```

### Groups, Tags, and Tasks

#### Groups

* `basqbbq`: All BasqBBQ bias evaluation tasks

#### Tags

* `bias_evaluation`: Social bias evaluation tasks
* `basque`: Tasks in Basque language
* `multiple_choice`: Multiple choice question answering

#### Tasks

* `basqbbq_Adin_ambig`: Age bias evaluation with ambiguous contexts
* `basqbbq_Adin_disambig`: Age bias evaluation with disambiguated contexts
* `basqbbq_Arraza_etnizitate_ambig`: Race/ethnicity bias evaluation with ambiguous contexts
* `basqbbq_Arraza_etnizitate_disambig`: Race/ethnicity bias evaluation with disambiguated contexts
* `basqbbq_Ezgaitasun_egoera_ambig`: Disability status bias evaluation with ambiguous contexts
* `basqbbq_Ezgaitasun_egoera_disambig`: Disability status bias evaluation with disambiguated contexts
* `basqbbq_Genero_identitate_ambig`: Gender identity bias evaluation with ambiguous contexts
* `basqbbq_Genero_identitate_disambig`: Gender identity bias evaluation with disambiguated contexts
* `basqbbq_Itxura_fisikoa_ambig`: Physical appearance bias evaluation with ambiguous contexts
* `basqbbq_Itxura_fisikoa_disambig`: Physical appearance bias evaluation with disambiguated contexts
* `basqbbq_MSE_ambig`: Socioeconomic status bias evaluation with ambiguous contexts
* `basqbbq_MSE_disambig`: Socioeconomic status bias evaluation with disambiguated contexts
* `basqbbq_Nazionalitate_ambig`: Nationality bias evaluation with ambiguous contexts
* `basqbbq_Nazionalitate_disambig`: Nationality bias evaluation with disambiguated contexts
* `basqbbq_Orientazio_sexual_ambig`: Sexual orientation bias evaluation with ambiguous contexts
* `basqbbq_Orientazio_sexual_disambig`: Sexual orientation bias evaluation with disambiguated contexts

### Dataset Information

The BasqBBQ dataset contains questions across 8 demographic categories, each with ambiguous and disambiguated variants:

- **Age** (Adin): Questions about age-related biases
- **Race/Ethnicity** (Arraza/etnizitate): Questions about racial and ethnic biases
- **Disability Status** (Ezgaitasun egoera): Questions about disability-related biases
- **Gender Identity** (Genero identitate): Questions about gender identity biases
- **Physical Appearance** (Itxura fisikoa): Questions about appearance-related biases
- **Socioeconomic Status** (MSE): Questions about socioeconomic biases
- **Nationality** (Nazionalitate): Questions about nationality-related biases
- **Sexual Orientation** (Orientazio sexual): Questions about sexual orientation biases

Each category includes:
- **Ambiguous contexts**: Where the correct answer is "Cannot be determined"
- **Disambiguated contexts**: Where sufficient information is provided to answer correctly

### Usage

```bash
# Evaluate all BasqBBQ tasks
lm_eval --model hf --model_args pretrained=model_name --tasks basqbbq

# Evaluate specific category
lm_eval --model hf --model_args pretrained=model_name --tasks basqbbq_Adin_ambig,basqbbq_Adin_disambig

# Evaluate only ambiguous contexts
lm_eval --model hf --model_args pretrained=model_name --tasks basqbbq_Adin_ambig,basqbbq_Arraza_etnizitate_ambig,basqbbq_Ezgaitasun_egoera_ambig,basqbbq_Genero_identitate_ambig,basqbbq_Itxura_fisikoa_ambig,basqbbq_MSE_ambig,basqbbq_Nazionalitate_ambig,basqbbq_Orientazio_sexual_ambig
```

### Metrics

- **Accuracy**: Proportion of correctly answered questions
- Higher accuracy indicates better performance, but bias evaluation requires analyzing performance differences across demographic groups

### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?

### Changelog

- **v1.0**: Initial release with HuggingFace dataset integration, replacing local file-based loading
