# CSHL Single Cell 2017



#### Introduction

I took on this project because I wanted to learn more about data visualization in a biological context. While working in the [Yeo lab](https://yeolab.github.io/), one of the people I admired from afar is [Olga Botvinnik](https://olgabotvinnik.com/), who regularly presented on visualizations generated from PCA and clustering. Conveniently, she made the course she taught at Cold Spring Harbor available for free on [her Github account](https://github.com/olgabot), so I felt this was a good place to start.

The main course repository is [cshl-singlecell-2017](https://github.com/harrisonized/cshl-singlecell-2017), and it focuses on generating visualizations using a subset of the the Macosko Drop-Seq dataset, which is available from the [macosko2015](https://github.com/harrisonized/macosko2015) repository. The meat of the course is in two notebooks:

1. [1.5_recreate_macosko2015_figure_5](https://github.com/harrisonized/cshl-singlecell-2017/blob/master/notebooks/1.5_recreate_macosko2015_figure_5.ipynb)
2. [2.2_apply_clustering_on_knn_graph](https://github.com/harrisonized/cshl-singlecell-2017/blob/master/notebooks/2.2_apply_clustering_on_knn_graph.ipynb)

Aside from that, there was a small detour in [1.2_Downloading_public_data_Shalek2013](https://github.com/harrisonized/cshl-singlecell-2017/blob/master/notebooks/1.2_Downloading_public_data_Shalek2013.ipynb) with a trivial amount of EDA.

The [macosko2015](https://github.com/harrisonized/macosko2015) library has a [notebooks](https://github.com/harrisonized/macosko2015/tree/master/notebooks) folder that documents the data cleaning. Unfortunately, these notebooks were extremely confusing for reasons I discuss in [another document](https://github.com/harrisonized/cshl-singlecell-2017-v2/blob/master/data/ISSUES.md). After much refactoring, I filtered out the redundant and irrelevant data, reduced the number of data-cleaning notebooks, grouped together similar functions, and reduced the number and size of saved files. With a smaller number of concise notebooks, it's now clear how the input data for the PCA and clustergrams were generated from the raw data.

I don't think many people are looking to study from this obscure course taught 3 years ago, but just in case anyone does, I hope my repository makes it relatively straightforward to jump straight to the meat of visualizing clustergrams and performing PCA, which is where the value of this course resides.



#### Data Sources

Relevant data only

1. `ClusterToCellType` was hard-coded from [Figure 5D](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/figure/F5/)
2. GSM1626793_P14Retina_1.digital_expression.txt was downloaded from [here](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63472)
3. retina_clusteridentities.txt was curl'd from [here](http://mccarrolllab.org/wp-content/uploads/2015/05/retina_clusteridentities.txt)
4. NIHMS687993-supplement-supp_data_4.xlsx was downloaded from [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)
5. NIHMS687993-supplement-supp_data_2.xlsx was downloaded from [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)



#### Notebooks

| Notebook                                       | Inputs                                                       | Outputs                                                      |
| ---------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 01-clean-supp_data_4                           | NIHMS687993-supplement-supp_data_4.xlsx                      | NIHMS687993-supplement-supp_data_4v2.xlsx                    |
| 02-make-mouse-gene-metadata                    | NIHMS687993-supplement-supp_data_4v2.csv<br />NIHMS687993-supplement-supp_data_2.xlsx | mouse_gene_metadata.csv                                      |
| 03-subset-digital_expression                   | mouse_gene_metadata<br />retina_clusteridentities.txt<br />GSM1626793_P14Retina_1.digital_expression.txt, | big_clusters_expression.csv<br />big_clusters_cell_metadata.csv<br />big_clusters_gene_metadata.csv<br />amacrine_expression.csv<br />amacrine_cell_metadata.csv<br />amacrine_gene_metadata.csv<br />differential_expression.csv<br />differential_cell_metadata.csv<br />differential_gene_metadata.csv |
| 04-recreate-figure_5-clustergrams              | retina_clusteridentities.txt<br />amacrine_expression.csv    | clustergrams figures                                         |
| 05-recreate-figure_5a-c                        | retina_clusteridentities.txt<br />amacrine_expression.csv    | figures                                                      |
| 06-pca-on-differential_clusters                | differential_clusters_expression.csv                         | differential_clusters_lowrank.csv<br />differential_clusters_sparse.csv |
| 07-apply_clustering_on_knn_graph.ipynb         | big_clusters_expression.csv retina_clusteridentities.txt     | figures                                                      |
| 08-pca-and-tsne-on-differential_clusters.ipynb | differential_clusters_expression.csv                         |                                                              |



#### License

This project is licensed under the terms of the [MIT license](https://github.com/harrisonized/cshl-singlecell-2017-v2/blob/master/LICENSE), just like the original [cshl-singlecell-2017](https://github.com/harrisonized/cshl-singlecell-2017).



#### Summary

I followed along part of cshl-singlecell-2017 and in the process, streamlined the data-cleaning and visualization. I'm done with this project for now. At some point in the future, I may revisit and probably write a blog post about what I learned.
