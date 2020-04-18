import pandas as pd
import multiprocessing as mlp

# INITIAL PARAMETERS
filename_config = 'config.json'
log_input = None
pathway_input = None
gene_input = None
hop_input = None

# inserire log

# set the number of the CPUs
NUM_CORES = mlp.cpu_count()

# mi serve a non troncare le info salvate all'interno del DF
pd.set_option('display.max_colwidth', -1)


COLS_DF = ['hop', 'name_start', 'hsa_start', 'name_end', 'hsa_end', 'url_gene_end', 'relation', 'type_rel', 'pathway_origin']
DF_TREE = pd.DataFrame(columns=COLS_DF)

# list of the updated pathway
LIST_UPDATED_PATHWAY = []

# list of the colors for prints
COLORS = {
    "pink": "\033[95m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "end_line": "\033[0m",
    "bold": "\033[1m",
    "underline": "\033[4m"
}