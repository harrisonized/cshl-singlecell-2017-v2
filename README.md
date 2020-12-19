# CSHL Single Cell 2017



#### Introduction

I took on this project because I wanted to learn more about data visualization in a biological context. While working in the Yeo lab, one of the people I admired from afar is Olga Botvinnik, who regularly presented on visualizations generated from PCA and clustering. Conveniently, she made the course she taught at Cold Spring Harbor available for free on her Github account, so I felt this was a good place to start.

The main course repository is cshl-singlecell-2017, and it focuses on generating visualizations using a subset of the the Macosko Drop-Seq dataset, which is available from the macosko2015 repository. The meat of the course is in three notebooks:

1. 1.5_recreate_macosko2015_figure_5
2. 2.2_apply_clustering_on_knn_graph.ipynb
3. 50_Example_workflow_reanalyzing_macosko2015.ipynb

Aside from that, there was a small detour in 1.2_Downloading_public_data_Shalek2013 with a trivial amount of EDA.

The macosko2015 library has a notebooks folder that documents the data cleaning. Unfortunately, these notebooks were extremely confusing for reasons I discuss in another document. After much refactoring, I filtered out the redundant and irrelevant data, reduced the number of data-cleaning notebooks, grouped together similar functions, and reduced the number and size of saved files. With a smaller number of concise notebooks, it's now clear how the input data for the PCA and clustergrams were generated from the raw data.

I don't think many people are looking to study from this obscure course taught 3 years ago, but just in case anyone does, I hope my repository makes it relatively straightforward to jump straight to the meat of visualizing clustergrams and performing PCA.



#### Data Sources

Relevant data only

1. `ClusterToCellType` was hard-coded from [Figure 5D](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/figure/F5/)
2. GSM1626793_P14Retina_1.digital_expression.txt was downloaded from [here](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63472)
3. retina_clusteridentities.txt was curl'd from [here](http://mccarrolllab.org/wp-content/uploads/2015/05/retina_clusteridentities.txt)
4. NIHMS687993-supplement-supp_data_4.xlsx was downloaded from [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)
5. NIHMS687993-supplement-supp_data_2.xlsx was downloaded from [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)



#### Notebooks

| Notebook                          | Inputs                                                       | Outputs                                                      |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 01-clean-supp_data_4              | NIHMS687993-supplement-supp_data_4.xlsx                      | NIHMS687993-supplement-supp_data_4v2.xlsx                    |
| 02-make-mouse-gene-metadata       | NIHMS687993-supplement-supp_data_4v2.csv<br />NIHMS687993-supplement-supp_data_2.xlsx | mouse_gene_metadata.csv                                      |
| 03-subset-digital_expression      | mouse_gene_metadata<br />retina_clusteridentities.txt<br />GSM1626793_P14Retina_1.digital_expression.txt, | big_clusters_expression.csv<br />big_clusters_cell_metadata.csv<br />big_clusters_gene_metadata.csv<br />amacrine_expression.csv<br />amacrine_cell_metadata.csv<br />amacrine_gene_metadata.csv<br />differential_expression.csv<br />differential_cell_metadata.csv<br />differential_gene_metadata.csv |
| 04-recreate-figure_5-clustergrams | retina_clusteridentities.txt<br />amacrine_expression.csv    | clustergrams figures                                         |
| 05-recreate-figure_5a-c           | retina_clusteridentities.txt<br />amacrine_expression.csv    | figures                                                      |
| 06-pca-on-differential_clusters   | differential_clusters_expression.csv                         | differential_clusters_lowrank.csv<br />differential_clusters_sparse.csv |



#### Summary

I followed along the cshl-singlecell-2017 and streamlined the data-cleaning and visualization. At some point in the future I'll revisit this project and write a blog post.