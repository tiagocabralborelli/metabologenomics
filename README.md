# Characterization of a novel marine isolate Micromonospora spp. BRA006 through a metabologenomics approach

## Repository map table

|Directory | Content |
|--------- | ------- |
|[notebooks](/notebooks)|Jupyter notebooks to run the data analysis of this work|
|[BGC](/BGC)|Files of each biosynthetic gene cluster from Illumina and MinION assemblies   |
|[bgc_comp](/bgc_comp)|Blast databases and BGC files to compare BRA006 data and reference sequences from [MiBiG](https://mibig.secondarymetabolites.org/)|
|[COG](/COG)|Files from the [Clusters of Orthologous Genes project](https://www.ncbi.nlm.nih.gov/research/cog) (COGs) with IDs and description of each COG pathway|
|[prokka](/prokka)|Prokka data files|
|[taxonomy](/taxonomy)|Phylogenetic tree file from [TYGS](https://tygs.dsmz.de/) server|


## Prepare the environment
To recreate our analysis step-by-step follow the procedures bellow

**Download miniconda installer**
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
**Execute it**
```
bash Miniconda3-latest-Linux-x86_64.sh
```
**Create and activate a dedicated environment**

```
conda env create -f omics_env.yml

conda activate omics 
```

## Datasets and metabolomic analysis
The LC-MS/MS data and compound-annotation  workflows are available at the following links

**Zenodo**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10366840.svg)](https://doi.org/10.5281/zenodo.10366840)

**GNPS tools**
    
[Feature Based Molecular Networking](https://gnps2.org/status?task=7b134da60f0f4a80aec790d2a294aedd)

[Chemwalker Nextflow](https://gnps2.org/status?task=9141a5cdabf842d39387e514e5305398)



## Acknowledgements
[Prokka](https://pubmed.ncbi.nlm.nih.gov/24642063/) - Seemann T. Prokka: rapid prokaryotic genome annotation. Bioinformatics. 2014 Jul 15;30(14):2068-9. doi: 10.1093/bioinformatics/btu153. Epub 2014 Mar 18. PMID: 24642063.

[AntiSMASH](https://academic.oup.com/nar/article/51/W1/W46/7151336?login=false) - Kai Blin, Simon Shaw, Hannah E Augustijn, Zachary L Reitz, Friederike Biermann, Mohammad Alanjary, Artem Fetter, Barbara R Terlouw, William W Metcalf, Eric J N Helfrich, Gilles P van Wezel, Marnix H Medema, Tilmann Weber, antiSMASH 7.0: new and improved predictions for detection, regulation, chemical structures and visualisation, Nucleic Acids Research, Volume 51, Issue W1, 5 July 2023, Pages W46–W50
