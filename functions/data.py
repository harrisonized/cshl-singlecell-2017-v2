import itertools
import pandas as pd
from .data_tools import list_to_col
from .list_tools import pairwise


# Objects included in this file:
# # ClusterToCellType

# Functions included in this file:
# # cluster_markers_raw_df_to_tables
# # cluster_markers_tables_to_df
# # format_cluster_markers_datatypes
# # preprocess_digital_expression


class ClusterToCellType:
    """ this loosely follows 02_make_celltype_metadata.ipynb """
    def __init__(self):
        """Data was hard-coded from Figure 5D of the paper.
        Link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/figure/F5/
        """
        self.tuple = [
            (1, "Horizontal cells"),
            (2, "Retinal ganglion cells"),
            (range(3, 24), "Amacrine cells"),
            (24, "Rods"),
            (25, "Cones"),
            (range(26, 34), "Bipolar cells"),
            (34, "Muller glia"),
            (35, "Astrocytes"),
            (36, "Fibroblasts"),
            (37, "Vascular endothelium"),
            (38, "Pericytes"),
            (39, "Microglia"),
        ]
        
        self.dataframe = self.tuple_to_dataframe()
        
    def tuple_to_dataframe(self):
        """ converts the tuple to a dataframe """
        df = pd.DataFrame(self.tuple, columns=['cluster_no', 'cell_type'])
        df = list_to_col(df, 'cluster_no')
        df['cluster_name'] = df['cluster_no'].apply(lambda x: f'cluster_{str(x).zfill(2)}')
        return df


def cluster_markers_raw_df_to_tables(raw_df):
    """Splits the raw dataframe into separate tables
    Returns a list containing those tables
    """
    table_start_idx = raw_df[raw_df['gene_symbol'] == 'cluster no.'].index.to_list()  # identify start of each table
    table_start_idx = table_start_idx+[len(raw_df)+2]  # include the last element
    table_start_end = [(i+2, j-2) for i, j in pairwise(table_start_idx)]  # get start and end indices for each subtable

    cluster_markers_tables = [raw_df[i: j] for i, j in table_start_end]  # split df into multiple tables
    return cluster_markers_tables


def cluster_markers_tables_to_df(cluster_markers_tables):
    """Takes the list of tables, cleans the corrupted ones
    Returns a single combined dataframe
    
    Tables that were corrupted:
    type 1: 18
    type 2: 20, 21, 30, 31
    type 3: 24, 27, 33
    """
    pd.options.mode.chained_assignment = None  # prevents warnings
    
    for i, table in enumerate(cluster_markers_tables):
    
        if i in [18]:
            cluster_markers_tables[i-1]['cluster_no'] = cluster_markers_tables[i-1]['cluster_no'].apply(lambda x: x.split(' ')[0])
            cluster_markers_tables[i-1]['power'] = cluster_markers_tables[i-1].apply(lambda df: df['myDiff'].split(' ')[-1]+df['power'].split(' ')[0], axis=1)
            cluster_markers_tables[i-1]['myDiff'] = cluster_markers_tables[i-1].apply(lambda df: df['myAUC'].split(' ')[-1]+df['myDiff'].split(' ')[0], axis=1)
            cluster_markers_tables[i-1]['myAUC'] = cluster_markers_tables[i-1].apply(lambda df: df['gene_symbol'].split(' ')[-1]+df['myAUC'].split(' ')[0], axis=1)
            cluster_markers_tables[i-1]['gene_symbol'] = cluster_markers_tables[i-1]['gene_symbol'].apply(lambda x: x.split(' ')[0])

        if i in [20, 21, 30, 31]:
            cluster_markers_tables[i-1]['cluster_no'] = cluster_markers_tables[i-1]['power']
            cluster_markers_tables[i-1]['power'] = cluster_markers_tables[i-1]['myDiff'].apply(lambda x: x.split(' ')[-1])
            cluster_markers_tables[i-1]['myDiff'] = cluster_markers_tables[i-1].apply(lambda df: df['myAUC']+df['myDiff'].split(' ')[0], axis=1)
            cluster_markers_tables[i-1]['myAUC'] = cluster_markers_tables[i-1]['gene_symbol'].apply(lambda x: x.split(' ')[-1])
            cluster_markers_tables[i-1]['gene_symbol'] = cluster_markers_tables[i-1]['gene_symbol'].apply(lambda x: x.split(' ')[0])

        if i in [24, 27, 33]:
            cluster_markers_tables[i-1]['cluster_no'] = cluster_markers_tables[i-1].apply(lambda df: df['power'].split(' ')[-1]+df['cluster_no'].split(' ')[0], axis=1)
            cluster_markers_tables[i-1]['power'] = cluster_markers_tables[i-1].apply(lambda df: df['myDiff'].split(' ')[-1]+df['power'].split(' ')[0], axis=1)
            cluster_markers_tables[i-1]['myDiff'] = cluster_markers_tables[i-1].apply(lambda df: df['myAUC']+df['myDiff'].split(' ')[0], axis=1)
            cluster_markers_tables[i-1]['myAUC'] = cluster_markers_tables[i-1].apply(lambda df: df['gene_symbol'].split(' ')[-1], axis=1)
            cluster_markers_tables[i-1]['gene_symbol'] = cluster_markers_tables[i-1]['gene_symbol'].apply(lambda x: x.split(' ')[0])

    # rejoin the tables
    cluster_markers = pd.concat(cluster_markers_tables)
    
    return cluster_markers


def format_cluster_markers_datatypes(df):
    """ specifies column types on cluster_markers_df before export """
    df['gene_symbol'] = df['gene_symbol'].astype(str)
    df['myAUC'] = df['myAUC'].astype(float)
    df['myDiff'] = df['myDiff'].astype(float)
    df['power'] = df['power'].astype(float)
    df['cluster_no'] = df['cluster_no'].astype(int)

    return df


def preprocess_digital_expression(df):
    """Convenience function
    """
    df['gene_symbol'] = df['gene'].map(lambda x: x.split(':')[-1].upper())
    df = df.set_index('gene_symbol')
    df = df.drop(columns=['gene'])
    df = df.groupby('gene_symbol').sum()  # Sum genes with the same name

    # Transpose
    df = df.T
    df.index = 'r1_' + df.index  # Add `r1_` prefix to barcodes to indicate the first run

    return df
