import json
from pathlib import Path


class ManifestLoader:
    def __init__(self, manifest_path: str):
        self.manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))

        self.documents = {doc["doc_id"]: doc for doc in self.manifest["documents"]}

    def get_document_metadata(
        self,
        doc_id: str,
    ) -> dict:
        return self.documents[doc_id]
