# cleanmagma

- [x] To retrieve the information from GWAS summary statistics file for running magma.
- [x] To run magma with snp to gene annotation, gene level and gene set level enrichment.
- [x] To summarize the results for the same input gmt files (named gene list) enriched to multiple GWAS data and plot a heatmap with rows are given input gmt names and columns are different GWAS file names.

Examples:
```{py}
from prepmagma import res
from prepmama import db

#work_folderwhere the GWAS summary files are located

#target_folder where the used GWAS summary files are moved to
#filename is the single  GWAS summary file you want to work on
db.run_single_gwas(work_folder, filename, target_folder, p = ['p'], n=['n_ownbw'], rsid=['rsid'], chromosome=['chr'], position=['pos'])
#res_folder is where all the results located
#summary_file is a tsv combining the results in res_folder
#pattern for filtering VARIABLE to be combined

df = res.compile_res(res_folder, summary_file, pattern)
res.heatmap(df, 'gsea/heatmap_common.pdf')
```