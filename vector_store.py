import numpy as np
import pickle
from pathlib import Path
from typing import List, Dict, Tuple
from ..config import Config

class VectorStore:
    
    def __init__(self, store_path: str = None):
        self.store_path = Path(store_path) if store_path else Config.VECTOR_DB_PATH / 'vector_store.pkl'
        self.vectors = []
        self.documents = []
        self.metadata_list = []
        self.load()
    
    def add_documents(self, documents: List[str], vectors: np.ndarray, metadata: Dict):
        for i, doc in enumerate(documents):
            self.documents.append(doc)
            self.vectors.append(vectors[i])
            self.metadata_list.append(metadata)
        
        self.save()
    
    def search(self, query_vector: np.ndarray, top_k: int = 3) -> List[Dict]:
        if len(self.vectors) == 0:
            return []
        
        vectors_array = np.array(self.vectors)
        
        similarities = np.dot(vectors_array, query_vector) / (
            np.linalg.norm(vectors_array, axis=1) * np.linalg.norm(query_vector)
        )
        
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            results.append({
                'document': self.documents[idx],
                'metadata': self.metadata_list[idx],
                'score': float(similarities[idx])
            })
        
        return results
    
    def save(self):
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            'vectors': self.vectors,
            'documents': self.documents,
            'metadata_list': self.metadata_list
        }
        with open(self.store_path, 'wb') as f:
            pickle.dump(data, f)
    
    def load(self):
        if self.store_path.exists():
            with open(self.store_path, 'rb') as f:
                data = pickle.load(f)
                self.vectors = data.get('vectors', [])
                self.documents = data.get('documents', [])
                self.metadata_list = data.get('metadata_list', [])
    
    def clear(self):
        self.vectors = []
        self.documents = []
        self.metadata_list = []
        self.save()
    
    def get_stats(self) -> Dict:
        return {
            'total_documents': len(self.documents),
            'total_vectors': len(self.vectors)
        }

