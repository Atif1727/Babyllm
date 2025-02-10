from typing import List
from sentencepiece import SentencePieceProcessor

import logging

# Customizing logging
logger=logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",  # Log to a file
    filemode="w"  # Overwrite the log file on each run
)

TOKENIZER_MODEL = "tokenizer.model"

class Tokenizer:
    def __init__(self,tokenizer_model):
        model_path=tokenizer_model if tokenizer_model else TOKENIZER_MODEL
        self.sp_model = SentencePieceProcessor(model_file=model_path)
        self.model_path = model_path

        self.n_words = self.sp_model.vocab_size()
        self.bos_id = self.sp_model.bos_id()
        self.eos_id = self.sp_model.eos_id()
        self.pad_id = self.sp_model.pad_id()

    def encode(self, s: str, bos: bool, eos: bool) -> List[int]:
        logger.info("Encoding the text using tokenizer...")
        t = self.sp_model.encode(s)
        if bos:
            t = [self.bos_id] + t
        if eos:
            t = t + [self.eos_id]
        return t

    def decode(self, tokens: List[int]) -> str:
        logger.info("Decoding the text using tokenizer...")
        return self.sp_model.decode(tokens)
