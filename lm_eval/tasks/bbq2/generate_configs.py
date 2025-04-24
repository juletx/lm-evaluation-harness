import yaml


categories = [
    "Age",
    "Disability_status",
    "Gender_identity",
    "Nationality",
    "Physical_appearance",
    "Race_ethnicity",
    "Religion",
    "SES",
    "Sexual_orientation",
]

conditions = ["ambig", "disambig"]

# Generate configs for each combination
for category in categories:
    for condition in conditions:
        task_name = f"bbq_{category}_{condition}"
        config = {
            "task": task_name,
            "dataset_path": "json",
            "dataset_name": None,
            "dataset_kwargs": {
                "data_files": [
                    {
                        "split": "test",
                        "path": f"/gaueko0/users/jetxaniz007/phd/lm_eval/lm-evaluation-harness/lm_eval/tasks/bbq/BBQ/data/BBQ/{category}_{condition}.jsonl",
                    },
                    {
                        "split": "train",
                        "path": f"/gaueko0/users/jetxaniz007/phd/lm_eval/lm-evaluation-harness/lm_eval/tasks/bbq/fewshot/no{category}_4s.jsonl",
                    },
                ]
            },
            "include": "bbq_template.yaml",
        }

        # Save config
        output_file = f"{task_name}.yaml"
        with open(output_file, "w") as f:
            yaml.dump(config, f, sort_keys=False)
