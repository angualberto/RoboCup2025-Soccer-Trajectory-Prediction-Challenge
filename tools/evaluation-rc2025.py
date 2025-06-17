# Script de avaliação comparando predição com ground-truth.

import os
import sys
import pandas as pd
import numpy as np

def evaluate(gt_dir, submit_dir):
    print(f"Avaliando submissão em {submit_dir} contra {gt_dir}...")
    total_error = 0
    count = 0
    for fname in os.listdir(gt_dir):
        if fname.endswith('.tracking.csv'):
            gt_file = os.path.join(gt_dir, fname)
            submit_file = os.path.join(submit_dir, fname)
            if not os.path.exists(submit_file):
                print(f"Arquivo ausente na submissão: {fname}")
                continue
            gt_df = pd.read_csv(gt_file)
            submit_df = pd.read_csv(submit_file)
            # Erro médio quadrático para todas as posições
            cols = [col for col in gt_df.columns if '_x' in col or '_y' in col]
            err = ((gt_df[cols] - submit_df[cols]) ** 2).mean().mean()
            print(f"{fname}: RMSE={np.sqrt(err):.4f}")
            total_error += err
            count += 1
    if count > 0:
        print(f"RMSE médio: {np.sqrt(total_error/count):.4f}")
    else:
        print("Nenhum arquivo avaliado.")

if __name__ == "__main__":
    gt = sys.argv[2]
    submit = sys.argv[4]
    evaluate(gt, submit)