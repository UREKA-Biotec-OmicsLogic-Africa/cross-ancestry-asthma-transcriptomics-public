#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys
import pandas as pd

EXPECTED = {
    'ancestry_fdr': 2134,
    'ancestry_dual': 1020,
    'ancestry_african': 612,
    'ancestry_european': 408,
    'sex_fdr': 97,
    'sex_dual': 73,
    'network_edges': 173,
}


def fail(message):
    print('FAIL:', message)
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.')
    args = parser.parse_args()
    root = Path(args.root).resolve()
    ok = True

    manifest = root/'results/manuscript_1/MANIFEST.tsv'
    if not manifest.exists():
        ok = fail(f'Missing {manifest}') and ok
    else:
        m = pd.read_csv(manifest, sep='\t')
        if len(m) != 72:
            ok = fail(f'MANIFEST has {len(m)} rows, expected 72') and ok
        else:
            print('PASS: 72 generated files indexed')

    de_path = root/'results/manuscript_1/supplementary/S1_complete_DE_and_expression/MS1_S1A_primary_ancestry_adjusted_OLS.tsv.gz'
    if de_path.exists():
        de = pd.read_csv(de_path, sep='\t')
        fdr = int((de['fdr'] < 0.05).sum())
        dual = int(((de['fdr'] < 0.05) & (de['mean_difference'].abs() > 0.5)).sum())
        afr = int(((de['fdr'] < 0.05) & (de['mean_difference'] > 0.5)).sum())
        eur = int(((de['fdr'] < 0.05) & (de['mean_difference'] < -0.5)).sum())
        got = (fdr, dual, afr, eur)
        exp = (2134, 1020, 612, 408)
        if got != exp:
            ok = fail(f'Ancestry counts {got}, expected {exp}') and ok
        else:
            print('PASS: ancestry DE counts')
    else:
        ok = fail(f'Missing {de_path}') and ok

    sex_path = root/'results/manuscript_1/supplementary/S1_complete_DE_and_expression/MS1_S1C_primary_sex_adjusted_OLS.tsv.gz'
    if sex_path.exists():
        sex = pd.read_csv(sex_path, sep='\t')
        fdr = int((sex['fdr'] < 0.05).sum())
        dual = int(((sex['fdr'] < 0.05) & (sex['mean_difference'].abs() > 0.5)).sum())
        if (fdr, dual) != (97, 73):
            ok = fail(f'Sex counts {(fdr,dual)}, expected (97,73)') and ok
        else:
            print('PASS: sex DE counts')
    else:
        ok = fail(f'Missing {sex_path}') and ok

    net_path = root/'results/manuscript_1/supplementary/S4_coexpression_networks/MS1_S4_network_summary.tsv'
    if net_path.exists():
        net = pd.read_csv(net_path, sep='\t')
        full = net.loc[net['group'].eq('All samples')].iloc[0]
        if int(full['retained_edges']) != 173:
            ok = fail('Full network edge count is not 173') and ok
        else:
            print('PASS: full network edge count')
    else:
        ok = fail(f'Missing {net_path}') and ok

    curated_drive = root/'results/manuscript_1/main_tables/MS1_Table_3_curated_genes_revised.tsv'
    if curated_drive.exists():
        cur = pd.read_csv(curated_drive, sep='\t')
        genes = set(cur['gene_symbol'] if 'gene_symbol' in cur.columns else cur['Gene'])
        expected_genes = {'ALOX5','ARRB2','CD28','CLDN18','CXCL1','CXCL8','GATA3','LDHA','LTC4S','MMP9','PRDX1','TGFB1','TIMP2'}
        if genes != expected_genes:
            ok = fail(f'Curated-gene set differs: {sorted(genes ^ expected_genes)}') and ok
        else:
            print('PASS: 13-gene curated set')
    else:
        ok = fail(f'Missing {curated_drive}') and ok

    print('\nFINAL STATUS:', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
