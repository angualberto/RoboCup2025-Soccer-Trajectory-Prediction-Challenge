# Script para validar o formato dos arquivos de submissão.

import os
import sys
import pandas as pd

def validate(test_data_dir, submit_dir):
    print(f"Validando submissão em {submit_dir} com dados de teste {test_data_dir}...")
    for fname in os.listdir(test_data_dir):
        if fname.endswith('.tracking.csv'):
            test_file = os.path.join(test_data_dir, fname)
            submit_file = os.path.join(submit_dir, fname)
            if not os.path.exists(submit_file):
                print(f"Arquivo ausente na submissão: {fname}")
                continue
            test_df = pd.read_csv(test_file)
            submit_df = pd.read_csv(submit_file)
            if test_df.shape != submit_df.shape:
                print(f"Formato diferente para {fname}: esperado {test_df.shape}, encontrado {submit_df.shape}")
            else:
                print(f"{fname}: OK")
    print("Validação concluída.")

if __name__ == "__main__":
    input_dir = sys.argv[2]
    submit_dir = sys.argv[4]
    validate(input_dir, submit_dir)