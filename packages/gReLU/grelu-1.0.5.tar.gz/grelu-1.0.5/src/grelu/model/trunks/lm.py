from torch import nn
from grelu.sequence.format import indices_to_strings


from torch import nn
from grelu.sequence.format import indices_to_strings


class NucleotideTransformerTrunk(nn.Module):
    """
    A trunk class to generate sequence embeddings using the nucleotide transformer
    family of models (https://huggingface.co/collections/InstaDeepAI/nucleotide-transformer-65099cdde13ff96230f2e592). The following models are currently supported:
    
    'nucleotide-transformer-2.5b-multi-species'
    'nucleotide-transformer-2.5b-1000g'
    'nucleotide-transformer-500m-human-ref'
    'nucleotide-transformer-500m-1000g'
    'nucleotide-transformer-v2-50m-multi-species'
    'nucleotide-transformer-v2-100m-multi-species'
    'nucleotide-transformer-v2-500m-multi-species'
    'nucleotide-transformer-v2-250m-multi-species'

    Args:
        name: Name of the language model.
        dtype: Data type for the layers.
        device: Device for the layers.
    """
    def __init__(self, name, dtype=None, device=None):
        super().__init__()

        self.name = name
        self.load_model()

    def load_model(self):
        """
        Loads the nucleotide transformer model.
        """
        from transformers import AutoTokenizer, AutoModelForMaskedLM

        ALLOWED_MODELS = {
            'nucleotide-transformer-2.5b-multi-species': 2560,
            'nucleotide-transformer-2.5b-1000g': 2560,
            'nucleotide-transformer-500m-human-ref': 1280,
            'nucleotide-transformer-500m-1000g':1280,
            'nucleotide-transformer-v2-50m-multi-species':512,
            'nucleotide-transformer-v2-100m-multi-species':512,
            'nucleotide-transformer-v2-500m-multi-species':1024, 
            'nucleotide-transformer-v2-250m-multi-species':768,
        }
        if self.name in ALLOWED_MODELS:
            if 'v2' in self.name:
                self.esm = AutoModelForMaskedLM.from_pretrained(f'InstaDeepAI/{self.name}', trust_remote_code=True).esm
                self.tokenizer = AutoTokenizer.from_pretrained(f'InstaDeepAI/{self.name}', trust_remote_code=True)
                self.max_seq_len = 12282
            else:
                self.esm = AutoModelForMaskedLM.from_pretrained(f'InstaDeepAI/{self.name}').esm
                self.tokenizer = AutoTokenizer.from_pretrained(f'InstaDeepAI/{self.name}')
                self.max_seq_len = 5994

            self.channels = ALLOWED_MODELS[self.name]
        else:
            raise ValueError(f'name must be one of {ALLOWED_MODELS.keys().tolist()}.')

    def forward(self, x):
        """
        Forward pass

        Args:
            x : Input tensor of shape (N, 4, L)

        Returns:
            Output tensor of shape (N, T, output_length)
        """
        if x.shape[-1] >= self.max_seq_len:
            raise ValueError(
                f"Sequence length exceeds the maximum allowed by the model: {self.max_seq_len}"
            )
        else:
            is_n = x.max(axis=1).values == 0
            device = x.device
            x = x.argmax(axis=1)
            x[is_n] = 4
            x = indices_to_strings(x)
            x = self.tokenizer(x, return_tensors="pt", add_special_tokens=False, padding=True)
            x = x["input_ids"].to(device)
            x = self.esm(x, output_hidden_states=True)['hidden_states']
            x = x[-1].swapaxes(1,2)
            return x