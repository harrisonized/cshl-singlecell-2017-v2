These are notebooks that became irrelevant after refactoring.

| Notebook                    | Input                                                        | Output                                                       |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| e02-make-cell-type-metadata | `ClusterToCellType`                                          | cluster_ids_to_celltypes.csv                                 |
| e03-make-cell-metadata      | `ClusterToCellType`,<br />retina_clusteridentities.txt       | cell_metadata.csv                                            |
| e05-reshape-pca-lowrank     | differential_clusters_pca_lowrank.csv,<br />retina_clusteridentities.txt,<br />amacrine_gene_metadata.csv | differential_clusters_lowrank_tidy.csv,<br />amacrine_lowrank_tidy.csv |