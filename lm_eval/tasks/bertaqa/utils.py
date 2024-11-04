def process_docs_global(dataset):
    """Filter examples with "Gai orokorrak" group."""

    def global_example(example: dict) -> bool:
        """Check if an example is global."""
        return example["group"] == "Gai orokorrak"

    return dataset.filter(global_example)


def process_docs_local(dataset):
    """Filter examples with "Euskal gaiak" group."""

    def local_example(example: dict) -> bool:
        """Check if an example is local."""
        return example["group"] == "Euskal gaiak"

    return dataset.filter(local_example)
