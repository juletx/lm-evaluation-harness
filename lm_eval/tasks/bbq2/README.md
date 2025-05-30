# BBQ

## Paper

Title: `BBQ: A hand-built bias benchmark for question answering`

Abstract: https://aclanthology.org/2022.findings-acl.165/

It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question-sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. Our task evaluate model responses at two levels: (i) given an under-informative context, we test how strongly responses reflect social biases, and (ii) given an adequately informative context, we test whether the model’s biases override a correct answer choice. We find that models often rely on stereotypes when the context is under-informative, meaning the model’s outputs consistently reproduce harmful biases in this setting. Though models are more accurate when the context provides an informative answer, they still rely on stereotypes and average up to 3.4 percentage points higher accuracy when the correct answer aligns with a social bias than when it conflicts, with this difference widening to over 5 points on examples targeting gender for most models tested.

Homepage: https://github.com/nyu-mll/BBQ

### Citation

```bibtex
@inproceedings{parrish-etal-2022-bbq,
    title = "{BBQ}: A hand-built bias benchmark for question answering",
    author = "Parrish, Alicia  and
      Chen, Angelica  and
      Nangia, Nikita  and
      Padmakumar, Vishakh  and
      Phang, Jason  and
      Thompson, Jana  and
      Htut, Phu Mon  and
      Bowman, Samuel",
    editor = "Muresan, Smaranda  and
      Nakov, Preslav  and
      Villavicencio, Aline",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2022",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-acl.165/",
    doi = "10.18653/v1/2022.findings-acl.165",
    pages = "2086--2105",
}
```

### Groups, Tags, and Tasks

#### Groups

* `bbq`: All BBQ bias evaluation tasks

#### Tags

* `bias_evaluation`: Social bias evaluation tasks
* `english`: Tasks in English language
* `multiple_choice`: Multiple choice question answering

#### Tasks

* `bbq_Age_ambig`: Age bias evaluation with ambiguous contexts
* `bbq_Age_disambig`: Age bias evaluation with disambiguated contexts
* `bbq_Disability_status_ambig`: Disability status bias evaluation with ambiguous contexts
* `bbq_Disability_status_disambig`: Disability status bias evaluation with disambiguated contexts
* `bbq_Gender_identity_ambig`: Gender identity bias evaluation with ambiguous contexts
* `bbq_Gender_identity_disambig`: Gender identity bias evaluation with disambiguated contexts
* `bbq_Nationality_ambig`: Nationality bias evaluation with ambiguous contexts
* `bbq_Nationality_disambig`: Nationality bias evaluation with disambiguated contexts
* `bbq_Physical_appearance_ambig`: Physical appearance bias evaluation with ambiguous contexts
* `bbq_Physical_appearance_disambig`: Physical appearance bias evaluation with disambiguated contexts
* `bbq_Race_ethnicity_ambig`: Race/ethnicity bias evaluation with ambiguous contexts
* `bbq_Race_ethnicity_disambig`: Race/ethnicity bias evaluation with disambiguated contexts
* `bbq_Religion_ambig`: Religion bias evaluation with ambiguous contexts
* `bbq_Religion_disambig`: Religion bias evaluation with disambiguated contexts
* `bbq_SES_ambig`: Socioeconomic status bias evaluation with ambiguous contexts
* `bbq_SES_disambig`: Socioeconomic status bias evaluation with disambiguated contexts
* `bbq_Sexual_orientation_ambig`: Sexual orientation bias evaluation with ambiguous contexts
* `bbq_Sexual_orientation_disambig`: Sexual orientation bias evaluation with disambiguated contexts

### Dataset Information

The BBQ dataset contains questions across 9 demographic categories, each with ambiguous and disambiguated variants:

- **Age**: Questions about age-related biases and stereotypes
- **Disability Status**: Questions about disability-related biases
- **Gender Identity**: Questions about gender identity biases
- **Nationality**: Questions about nationality-related biases
- **Physical Appearance**: Questions about appearance-related biases
- **Race/Ethnicity**: Questions about racial and ethnic biases
- **Religion**: Questions about religious biases
- **Socioeconomic Status (SES)**: Questions about socioeconomic biases
- **Sexual Orientation**: Questions about sexual orientation biases

Each category includes:
- **Ambiguous contexts**: Where the correct answer is "Cannot be determined" due to insufficient information
- **Disambiguated contexts**: Where sufficient information is provided to answer correctly

### Usage

```bash
# Evaluate all BBQ tasks
lm_eval --model hf --model_args pretrained=model_name --tasks bbq

# Evaluate specific category
lm_eval --model hf --model_args pretrained=model_name --tasks bbq_Age_ambig,bbq_Age_disambig

# Evaluate only ambiguous contexts
lm_eval --model hf --model_args pretrained=model_name --tasks bbq_Age_ambig,bbq_Disability_status_ambig,bbq_Gender_identity_ambig,bbq_Nationality_ambig,bbq_Physical_appearance_ambig,bbq_Race_ethnicity_ambig,bbq_Religion_ambig,bbq_SES_ambig,bbq_Sexual_orientation_ambig
```

### Metrics

- **Accuracy**: Proportion of correctly answered questions
- **Bias Score**: Measures the difference in accuracy between stereotyped and non-stereotyped groups
- Higher accuracy on disambiguated contexts and appropriate performance on ambiguous contexts indicates good bias detection

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
