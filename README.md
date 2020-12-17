# CSHL Single Cell 2017



#### Introduction

I took on this project, because I wanted to learn more about data visualization in a biological context. While working in the Yeo lab, one of the people I admired from afar is Olga Botvinnik, who regularly presented during lab meetings visualizations generated from PCA and clustering. Conveniently, she made the course she taught at Cold Spring Harbor available for free on her Github account, so I felt this was a good place to start.

The main course repository is cshl-singlecell-2017, and it focuses on using PCA to analyze the Macosko Drop-Seq dataset, which is available from the macosko2015 repository. The meat of the course is in three notebooks:

1. `1.5_recreate_macosko2015_figure_5.ipynb`
2. `2.2_apply_clustering_on_knn_graph.ipynb`
3. `50_Example_workflow_reanalyzing_macosko2015.ipynb`

Aside from that, there was a small detour in `1.2_Downloading_public_data_Shalek2013.ipynb` with a minor amount of EDA.



#### Getting Started

In the cshl-singlecell-2017 repository, the first notebook to call upon this dataset is `1.5_recreate_macosko2015_figure_5`, where the data is read in using the following lines of code:

```python
import macosko2015
urlname = macosko2015.BASE_URL + 'differential_clusters_expression.csv'
expression = pd.read_csv(urlname, index_col=0)
```

I have to say, I'm not a fan of abstracting away data paths. In order to figure out what this code was doing, I had to take a peek in `macosko2015`, where I found this:

```
BASE_URL = "https://media.githubusercontent.com/media/olgabot/macosko2015/" \
         "master/data/05_make_rentina_subsets_for_teaching/"
```

Of course, when I tried to import this data, I got an error. Peeking in file that came with the git repository, here's what I found:

| version https://git-lfs.github.com/spec/v1                   |
| ------------------------------------------------------------ |
| oid sha256:cb8a06f5ee26dbf29a2aecc697a752eacf91e2b8063efddd03d81cf2f5d0733c |
| size 16255430                                                |

So rather than give me the data directly, it gives me a hash.

In `2.2_apply_clustering_on_knn_graph`, it's even worse:

```python
import macosko2015
counts, cell_metadata, gene_metadata = macosko2015.load_big_clusters()
counts.head()
```

Peeking into the `macosko2015` library again, here's what I found:

```python
def load_big_clusters(package='pandas'):
    """Read expression and metadata for 50 random cells from 6 biggest clusters
    
    300 cells, 259 genes
    
    Parameters
    ----------
    package : 'pandas' | 'xarray'

    Returns
    -------
    if format == "pandas":
        expression, cell_metadata, gene_metadata
    if format == "xarray"
        xarray.Dataset
    """
    return _load('big_clusters', package)


def _load(prefix, package):
    """Internal method for loading """

    expression = read_csv(BASE_URL, '{}_expression.csv'.format(prefix))
    cell_metadata = read_csv(BASE_URL, '{}_cell_metadata.csv'.format(prefix))
    gene_metadata = read_csv(BASE_URL, '{}_gene_metadata.csv'.format(prefix))

    if package == 'xarray':
        ds = xr.Dataset({'expression': (['cell', 'gene'], expression),
                         'gene_metadata':
                             (['gene', 'gene_feature', ], gene_metadata),
                         'cell_metadata':
                             (['cell', 'cell_feature'], cell_metadata)},
                        coords={'gene': expression.columns,
                                'cell': expression.index,
                                'cell_feature': cell_metadata.columns,
                                'gene_feature': gene_metadata.columns})
        return ds
    if package == 'pandas':
        return expression, cell_metadata, gene_metadata
    else:
        raise ValueError('"{}" is not a valid format. Only "pandas" and '
                         '"xarray" are accepted'.format(package))


def read_csv(folder, filename):
    """Wrapper for pandas read_csv that uses the first column for the index"""
    csv = urljoin(folder, filename)
    return pd.read_csv(csv, index_col=0)
```

Whelp. All this convoluted code does in the end is using pandas read_csv to retrieve data from a link. Why not just hard-code those links in the notebook and use `pd.read_csv` directly? This made me scratch my head.

Poking around a little more, I found a folder called  `notebooks`, which documents how the data was cleaned. Bingo, this was exactly what I needed! Since the raw data was actually available online due to being part of a published paper, if I followed along the data-cleaning notebooks, I should end up with the same data.



#### Cleaning the Data-Cleaning

Like the data imports, this part left me scratching my head too. Things that made this part hard to follow along were:

1. Redundancies, ie. saving files like this:

   | cluster_id | celltype               | cluster_n | cluster_celltype_with_id            |
   | ---------- | ---------------------- | --------- | ----------------------------------- |
   | cluster_02 | Retinal ganglion cells | 2         | Retinal ganglion cells (cluster_02) |

2. Undocumented self-notes

   > The original supplementary file was corrupted and had many problems with the column values so I fixed them by hand, which is why we use `mmc4_v2.xlsx`.

   This didn't give me enough information to figure out what was done, so I had to completely redo this part.

3. Dropped leads

   > This is a  mess to clean ... each section is headed by the cluster numbers that are compared and have to iterate through every time you see "Clusters".
   >
   > Don't need this for now

4. Unused files (either intermediates or for scoping purposes):

   ```
   cluster_n.csv
   cluster_ids.csv
   cluster_bools.csv
   mouse_genes_tidy.csv
   cellcycle_genes_tidy.csv
   amacrine.netcdf
   big_clusters.netcdf
   differential_clusters.netcdf
   differential_clusters_lowrank.csv
   differential_clusters_lowrank_tidy_metadata_amacrine.csv
   differential_clusters_sparse.csv
   ```

Don't get me wrong. I think it's great that there was any documentation at all! For sure, I would have given up if there wasn't anything to work off of, but this is far from ideal. It was clear that I had A LOT of work ahead of me. I was going to have to do some cleaning of the data cleaning (and then cleaning of the cleaning of the cleaning...).



#### Current Status of this Project

After a lot of data cleaning, I've arrived at a point where I can confidently say where the data comes from. At some point I will write a blog post about what each of these parts mean to accomplish, so stay tuned!

