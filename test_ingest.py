from research_navigator.ingest.chunker import Chunker
from research_navigator.ingest.embedder import Embedder
from research_navigator.ingest.manifest_loader import ManifestLoader
from research_navigator.ingest.parser import PDFParser
from research_navigator.ingest.qdrant_store import QdrantStore

pdf_path = (
    r"..\ai-research-navigator-corpus"
    r"\ai-research-navigator-corpus"
    r"\documents\arxiv\arxiv-1706.03762.pdf"
)

doc_id = "arxiv-1706.03762"

# Load metadata from manifest
loader = ManifestLoader(
    r"..\ai-research-navigator-corpus"
    r"\ai-research-navigator-corpus"
    r"\manifest.json"
)

metadata = loader.get_document_metadata(doc_id)

# Parse document
parser = PDFParser()

document = parser.parse(
    pdf_path,
    doc_id,
)

# Create chunks
chunker = Chunker()

chunks = chunker.chunk_document(document)

print(f"Chunks created: {len(chunks)}")

# Create embeddings
embedder = Embedder()

vectors = embedder.embed_batch([chunk.text for chunk in chunks])

print(f"Vectors created: {len(vectors)}")

# Store in Qdrant
store = QdrantStore()

store.create_collection()

store.upsert_chunks(
    chunks,
    vectors,
    metadata,
)

print("Done")
