# Data

Create a downloads folder and download the relevant data. Use the python notebooks to generate the rest. At the end of the project, here are the files in my directory.

```
data
├── downloads
│   ├── retina_clusteridentities.txt
│   ├── NIHMS687993-supplement-supp_data_2.xlsx
│   ├── NIHMS687993-supplement-supp_data_4.xlsx
│   └── GSM1626793_P14Retina_1.digital_expression.txt
│
├── big_clusters
│   ├── big_clusters_expression.csv
│   ├── big_clusters_cell_metadata.csv
│   └── big_clusters_gene_expression.csv
├── amacrine
│   ├── amacrine_expression.csv
│   ├── amacrine_cell_metadata.csv
│   └── amacrine_gene_expression.csv
├── retina
│   ├── differential_clusters_expression.csv
│   ├── differential_clusters_cell_metadata.csv
│   └── differential_clusters_gene_expression.csv
│
├── pca
│   ├── differential_clusters_pca_lowrank.csv
│   └── differential_clusters_pca_sparse.csv
│
├── NIHMS687993-supplement-supp_data_4v2.csv
├── mouse_gene_metadata.csv
│
├── ISSUES.md
└── README.md
```



#### Relevant Data

| Data                                                         | Source                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| retina_clusteridentities.txt                                 | curl http://mccarrolllab.org/wp-content/uploads/2015/05/retina_clusteridentities.txt --output retina_clusteridentities.txt |
| NIHMS687993-supplement-supp_data_2.xlsx,<br />NIHMS687993-supplement-supp_data_4.xlsx | Downloaded from here: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/<br />Look in Supplementary Materials |
| GSM1626793_P14Retina_1.digital_expression.txt                | Downloaded from here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63472 |

Data was downloaded as-is. For example, there are errors in NIHMS687993-supplement-supp_data_4.xlsx that are fixed in 01-clean-supp_data_4.



#### Irrelevant Data

In my repository, I put these in downloads/extra, but feel free not to download these.

| Data                                                         | Source                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| mmc1.pdf<br />mmc3.xlsx                                      | Downloaded from here: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/<br />Look in Supplementary Materials |
| GSM1626794_P14Retina_2.digital_expression.txt.gz<br />GSM1626795_P14Retina_3.digital_expression.txt.gz<br />GSM1626796_P14Retina_4.digital_expression.txt.gz<br />GSM1626797_P14Retina_5.digital_expression.txt.gz<br />GSM1626798_P14Retina_6.digital_expression.txt.gz<br />GSM1626799_P14Retina_7.digital_expression.txt.gz | Downloaded from here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63472 |
| GSM1544798_SpeciesMix_ThousandSTAMPs_HUMAN.digital_expression.txt.gz<br />GSM1544798_SpeciesMix_ThousandSTAMPs_MOUSE.digital_expression.txt.gz<br />GSM1544799_SpeciesMix_HundredSTAMPs_HUMAN.digital_expression.txt.gz<br />GSM1544799_SpeciesMix_HundredSTAMPs_MOUSE.digital_expression.txt.gz | Downloaded from here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63269 |
| GSM1629192_Pure_HumanMouse_HUMAN.digital_expression.txt.gz GSM1629192_Pure_HumanMouse_MOUSE.digital_expression.txt.gz | Downloaded from here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1629192 |
| GSM1629193_ERCC.digital_expression.txt.gz,<br />GSM1629193_hg19_ERCC.dict.txt.gz,<br />GSM1629193_hg19_ERCC.refFlat.txt.gz | Downloaded from here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1629193 |

