import yaml


categories = [
    "Adin",
    "Arraza_etnizitate",
    "Ezgaitasun_egoera",
    "Genero_identitate",
    "Itxura_fisikoa",
    "MSE",
    "Nazionalitate",
    "Orientazio_sexual",
]

conditions = ["ambig", "disambig"]

# Generate configs for each combination
for category in categories:
    for condition in conditions:
        task_name = f"basqbbq_{category}_{condition}"
        config = {
            "task": task_name,
            "dataset_path": "json",
            "dataset_name": None,
            "dataset_kwargs": {
                "data_files": [
                    {
                        "split": "test",
                        "path": f"/gaueko0/users/jetxaniz007/phd/lm_eval/lm-evaluation-harness/lm_eval/tasks/basqbbq/BasqBBQ/data/BasqBBQ/{category}_{condition}.jsonl",
                    },
                    {
                        "split": "train",
                        "path": f"/gaueko0/users/jetxaniz007/phd/lm_eval/lm-evaluation-harness/lm_eval/tasks/basqbbq/fewshot/no{category}_4s.jsonl",
                    },
                ]
            },
            "include": "basqbbq_template.yaml",
        }

        # Save config
        output_file = f"{task_name}.yaml"
        with open(output_file, "w") as f:
            yaml.dump(config, f, sort_keys=False)
