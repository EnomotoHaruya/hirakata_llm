"""プロジェクト設定""" 
import os # ディレクトリ設定 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DIR_CORPUS = os.path.join(BASE_DIR, "corpus")
DIR_DATA = "/home/aichatbot25/data"
DIR_MODEL = os.path.join(BASE_DIR, "model")
DIR_WIKI = os.path.join(BASE_DIR, "wiki")
DIR_WIKI_CORPUS = os.path.join(DIR_WIKI, "corpus")
DIR_WIKI_CORPUS_TEXT = os.path.join(DIR_WIKI_CORPUS, "text")

# 入力ファイル 
EXCEL_FILE = os.path.join(DIR_DATA, "FAQlist.xlsx")
WIKI_FILE = os.path.join("/home/aichatbot25/book-local-llm-sample/src/ch4/anime_llm/corpus", "jawiki-latest-pages-articles-multistream.xml")

# 生成ファイル 
JSON_XLSX_DATASET_FILE = os.path.join(DIR_CORPUS, "FAQdataset.json") 
JSON_MERGED_DATASET_FILE = os.path.join(DIR_CORPUS, "merged_data.json")

JSON_WIKI_TARGET_FILES = os.path.join(DIR_WIKI_CORPUS, "hirakata_corpus_target_files.json")
JSON_WIKI_DATASET_FILE = os.path.join(DIR_WIKI_CORPUS, "hirakata_corpus.json")
JSON_TO_JSONL_FILE = os.path.join(DIR_WIKI_CORPUS, "train_data.json")


# パラメータ 
MODEL_NAME = "unsloth/Llama-3.2-3B-Instruct" 
OLLAMA_TIMEOUT = 30 
MAX_SEQ_LENGTH = 2048 
MAX_STEPS = 500 
MAX_DATASET_SIZE = 3000

os.makedirs(DIR_WIKI_CORPUS_TEXT, exist_ok=True)