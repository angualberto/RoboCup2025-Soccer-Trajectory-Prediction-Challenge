# Script para gerar test-data a partir dos jogos completos.

import os
import sys
import pandas as pd

def create_test_data(input_dir, output_dir):
    print(f"Extraindo dados de teste de {input_dir} para {output_dir}...")
    os.makedirs(output_dir, exist_ok=True)
    for fname in os.listdir(input_dir):
        if fname.endswith('.tracking.csv'):
            df = pd.read_csv(os.path.join(input_dir, fname))
            # Exemplo: pega últimos 30 frames antes do último evento de gol
            if 'goal' in df.columns:
                goal_frames = df[df['goal'] == 1].index
                if len(goal_frames) > 0:
                    last_goal = goal_frames[-1]
                    test_df = df.iloc[max(0, last_goal-30):last_goal]
                    test_df.to_csv(os.path.join(output_dir, fname), index=False)
    print("Concluído.")

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    create_test_data(input_dir, output_dir)