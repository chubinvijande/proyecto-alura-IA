from pathlib import Path


def get_sources(documents):
    return sorted(
        {
            Path(doc.metadata["source"]).name
            for doc in documents
        }
    )