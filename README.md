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
The LC-MS/MS data and compound annotation  workflows are available at the following links

**Zenodo**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10366840.svg)](https://doi.org/10.5281/zenodo.10366840)

**GNPS tools**
    
[Feature Based Molecular Networking](https://gnps2.org/status?task=7b134da60f0f4a80aec790d2a294aedd)

[Chemwalker Nextflow](https://gnps2.org/status?task=9141a5cdabf842d39387e514e5305398)




