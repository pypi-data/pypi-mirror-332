from rara_meta_extractor.utils import load_txt, load_json
import importlib.resources
import os

SIMPLE_FIELDS_FILE_PATH = importlib.resources.files("rara_meta_extractor.data") / "simple_fields.txt"
RESTRICTED_FIELDS_FILE_PATH = importlib.resources.files("rara_meta_extractor.data") / "fields.json"

SIMPLE_FIELDS = load_txt(SIMPLE_FIELDS_FILE_PATH, to_list=True)
RESTRICTED_FIELDS = load_json(RESTRICTED_FIELDS_FILE_PATH)

DEFAULT_INSTRUCTIONS = "This is a conversation between user and an information extractor \
whose sole purpose is to extract {0}. NB! Do not output any \
additional information or specifications!"

DEFAULT_CONFIG = {
    "fields": RESTRICTED_FIELDS,
    "instructions": DEFAULT_INSTRUCTIONS
}
