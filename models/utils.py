# Funções auxiliares para o modelo.

import numpy as np
import pandas as pd

def cartesian_to_polar(x, y, ref_x=0, ref_y=0):
    dx, dy = x - ref_x, y - ref_y
    r = np.hypot(dx, dy)
    theta = np.arctan2(dy, dx)
    return r, theta

def polar_to_cartesian(r, theta, ref_x=0, ref_y=0):
    x = ref_x + r * np.cos(theta)
    y = ref_y + r * np.sin(theta)
    return x, y

def estimate_velocity(df, cols_x, cols_y):
    # Calcula velocidade simples por diferença entre frames consecutivos
    vels = {}
    for col_x, col_y in zip(cols_x, cols_y):
        vels[col_x] = df[col_x].diff().fillna(0)
        vels[col_y] = df[col_y].diff().fillna(0)
    return vels

def estimate_acceleration(vels, cols_x, cols_y):
    # Calcula aceleração simples por diferença entre frames consecutivos
    accs = {}
    for col_x, col_y in zip(cols_x, cols_y):
        accs[col_x] = vels[col_x].diff().fillna(0)
        accs[col_y] = vels[col_y].diff().fillna(0)
    return accs