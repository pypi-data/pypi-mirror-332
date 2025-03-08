import torch
import numpy as np
from typing import Tuple, Mapping, List
from transformers import PreTrainedTokenizer


class BertCollator:
	"""配合BertDataset使用
	传入({input_id, attention_mask, token_type_id}, labels), 
	返回({input_ids: [], attention_mask: [], token_type_ids: []}, labels),
	"""

	def __call__(self, examples: List[Tuple[Mapping, torch.Tensor]]) -> Tuple[Mapping, torch.Tensor]:
		tokenizes, labels = zip(*examples)
		new_tokenizes = {k: [] for k in tokenizes[0].keys()}
		for d in tokenizes:
			for k, v in d.items():
				new_tokenizes[k].append(v)
		new_tokenizes = {k: torch.stack(v) for k, v in new_tokenizes.items()}

		return new_tokenizes, torch.tensor(labels, dtype=torch.long)


class BertTokenizeCollator:
	"""传入的是(text, label), 返回的是({input_ids: [], attention_mask: [], token_type_ids: []}, labels)"""
	
	def __init__(self, tokenizer: PreTrainedTokenizer, max_length: int = None, **kwargs):
		self.tokenizer = tokenizer
		self.max_length = max_length
		self.kwargs = kwargs
	
	def __call__(self, examples: List[Tuple[str, int]]) -> Tuple[Mapping, torch.Tensor]:
		texts, labels = zip(*examples)
		labels = torch.LongTensor(np.array(labels))
		
		return self.tokenizer.batch_encode_plus(texts,
                                                max_length=self.max_length,
                                                padding='max_length',
                                                truncation=True,
                                                return_attention_mask=True,
                                                return_tensors='pt',
												**self.kwargs), labels
		