# Issues

In this document, I want to describe the issues I encountered while working through the data-cleaning part of this course, because after refactoring, it looks like there wasn't much in the way of data transformation. This might be true if I had done the project from ground up using the most efficient steps, but because I was working off of an existing codebase, whenever I wrote new code, I had to match it to the inputs and outputs of the old code. This significantly increased the amount of time it took to do this relatively small project.

Don't get me wrong. I think it's great that there was any documentation on the data-cleaning at all! For sure, I wouldn't have even tried if there wasn't anything to work off of, but this is far from ideal. I had to do **A LOT** of refactoring, much more so than I've ever had to do in industry.



#### Issues

1. Data was unavailable

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

2. Data imports are convoluted

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

   Whelp. All this convoluted code does in the end is using pandas read_csv to retrieve data from a link. Why not just hard-code those links in the notebook and use `pd.read_csv` directly?

3. Original datasources are not identified. It took a while to find where all 23 files in 00_original came from.

4. Relevant datasources are not identified. After downloading all the data, I had to look through all 8 notebooks to figure out which ones were actually being used. It turns out only 4 out of 23 are relevant.

5. Pointless savepoints. Here is a list:
   cluster_n.csv
   cluster_ids.csv
   cluster_bools.csv
   mouse_genes_tidy.csv
   cellcycle_genes_tidy.csv
   amacrine.netcdf
   big_clusters.netcdf
   differential_clusters.netcdf
   differential_clusters_lowrank_tidy_metadata_amacrine.csv
   
6. Redundant data saved over and over again, mostly originating from cell_metadata, but also redundancies resulting from reshapes, like differential_clusters_lowrank.csv vs. differential_clusters_lowrank_tidy.csv.

   | cluster_id | celltype               | cluster_n | cluster_celltype_with_id            |
   | ---------- | ---------------------- | --------- | ----------------------------------- |
   | cluster_02 | Retinal ganglion cells | 2         | Retinal ganglion cells (cluster_02) |

7. Undocumented self-notes

   > The original supplementary file was corrupted and had many problems with the column values so I fixed them by hand, which is why we use `mmc4_v2.xlsx`.

8. Dropped leads

   > This is a  mess to clean ... each section is headed by the cluster numbers that are compared and have to iterate through every time you see "Clusters".
   >
   > Don't need this for now

9. Code that should have been a one-liners stretched out to many lines over many cell blocks including printing intermediate results. For example, compare [03-subset-digital_expression](https://github.com/harrisonized/cshl-singlecell-2017-v2/blob/master/03-subset-digital_expression.ipynb) with [05_make_retina_subsets_for_teaching](https://github.com/harrisonized/macosko2015/blob/master/notebooks/05_make_rentina_subsets_for_teaching.ipynb)

