# Mackosko

This follows the main part of the cshl-singlecell-2017 course.

Note that `08-recreate-figure_5-clustergrams` was the template for `1.5_recreate_macosko2015_figure_5.ipynb`. 



#### Data Descriptions

1. [Figure 5D](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/figure/F5/) of the paper
2. retina_clusteridentities.txt was curl'd from [here](http://mccarrolllab.org/wp-content/uploads/2015/05/retina_clusteridentities.txt)
3. NIHMS687993-supplement-supp_data_4.xlsx was downloaded from [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)
4. NIHMS687993-supplement-supp_data_2.xlsx was downloaded from [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)
5. GSM1626793_P14Retina_1.digital_expression.txt was downloaded from [here](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63472)



#### Notebook Descriptions

1. 02-make-cell_type-metadata.ipynb
   1. Hard codes cell clusters from Figure 5D of the paper
   2. Exports to `metadata/cluster_ids_to_celltypes.csv`
2. 03-make-cell-metadata.ipynb
   1. Reads in `cluster_ids_to_celltypes.csv` and `retina_clusteridentities.txt`
   2. Combines the data
   3. Exports it as `metadata/cell_metadata.csv`
3. 04-clean-supp_data_4.ipynb
   1. Reads in NIHMS687993-supplement-supp_data_4.xlsx
   2. The data was corrupted, so this notebook fixes that
   3. Exports this as `FINAL_MARKERS_FOR_EACH_CLUSTERS.csv`
4. 04-make-mouse-gene-metadata
   1. Reads in`FINAL_MARKERS_FOR_EACH_CLUSTERS.csv`
   2. Reads in `NIHMS687993-supplement-supp_data_2.xlsx`
   3. Exports `mouse_gene_metadata.csv`
5. 05-clean-data-from-retina_1
   1. Reads in `metadata/cell_metadata`, `mouse_gene_metadata.csv`, and `GSM1626793_P14Retina_1.digital_expression.txt`.
   2. Outputs `expression.csv`, `cell_metadata.csv`, and `gene_expression.csv` for the following groups:
      1. big_clusters
      2. amacrine
      3. differential
6. 05-clean-data-from-retina_1-for-PCA
   1. Reads in `metadata/cell_metadata`, `amacrine_gene_metadata.csv`, and `differential_clusters_expression.csv`
   2. Exports: `differential_clusters_lowrank.csv`, `differential_clusters_lowrank_tidy.csv`, `differential_clusters_lowrank_tidy_metadata.csv`, and `differential_clusters_lowrank_tidy_metadata_amacrine.csv`.
7. 08-recreate-figure_5-clustergrams
   1. Reads in `metadata/cell_metadata.csv` and `amacrine_expression.csv`, `amacrine_cell_metadata.csv`, and `amacrine_gene_metadata.csv`
   2. Outputs figures
   3. Comments: can probably stop using `cell_metadata` and use the raw file instead.
8. 08-recreate-figure_5a-c.
   1. Reads in `cell_metadata.csv` and `differential_expression.csv`, `differential_cell_metadata.csv`, and `differential_gene_metadata.csv`
   2. Outputs figures



#### Other Data

Supplementary files found in `macoscko2015/data/00original`. Most of them are not used.

````
GSM1544798_SpeciesMix_ThousandSTAMPs_HUMAN.digital_expression.txt.gz
GSM1544798_SpeciesMix_ThousandSTAMPs_MOUSE.digital_expression.txt.gz
GSM1544799_SpeciesMix_HundredSTAMPs_HUMAN.digital_expression.txt.gz
GSM1544799_SpeciesMix_HundredSTAMPs_MOUSE.digital_expression.txt.gz
GSM1626793_P14Retina_1.digital_expression.txt.gz
GSM1626794_P14Retina_2.digital_expression.txt.gz
GSM1626795_P14Retina_3.digital_expression.txt.gz
GSM1626796_P14Retina_4.digital_expression.txt.gz
GSM1626797_P14Retina_5.digital_expression.txt.gz
GSM1626798_P14Retina_6.digital_expression.txt.gz
GSM1626799_P14Retina_7.digital_expression.txt.gz
GSM1629192_Pure_HumanMouse_HUMAN.digital_expression.txt.gz
GSM1629192_Pure_HumanMouse_MOUSE.digital_expression.txt.gz
GSM1629193_ERCC.digital_expression.txt.gz
GSM1629193_hg19_ERCC.dict.txt.gz
GSM1629193_hg19_ERCC.refFlat.txt.gz
mmc1.pdf
mmc2.xlsx
mmc3.xlsx
mmc4.xlsx
mmc4_v2.xlsx
retina_clusteridentities.txt
````

