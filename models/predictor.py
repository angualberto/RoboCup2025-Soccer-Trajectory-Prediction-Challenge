import numpy as np
import pandas as pd
from .utils import cartesian_to_polar, polar_to_cartesian

class Entity:
    def __init__(self, x, y, vx=0, vy=0, ax=0, ay=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

    def to_polar(self, ref_x=0, ref_y=0):
        return cartesian_to_polar(self.x, self.y, ref_x, ref_y)

    def update_state(self, x, y, vx, vy, ax, ay):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.ax, self.ay = ax, ay

    def predict_next_polar(self, dt, ref_x=0, ref_y=0):
        r, theta = self.to_polar(ref_x, ref_y)
        vr = (self.vx * np.cos(theta) + self.vy * np.sin(theta))
        vtheta = (-self.vx * np.sin(theta) + self.vy * np.cos(theta)) / (r + 1e-6)
        ar = (self.ax * np.cos(theta) + self.ay * np.sin(theta))
        atheta = (-self.ax * np.sin(theta) + self.ay * np.cos(theta)) / (r + 1e-6)
        r_next = r + vr * dt + 0.5 * ar * dt**2
        theta_next = theta + vtheta * dt + 0.5 * atheta * dt**2
        return r_next, theta_next

    def predict_next_cartesian(self, dt, ref_x=0, ref_y=0):
        r_next, theta_next = self.predict_next_polar(dt, ref_x, ref_y)
        return polar_to_cartesian(r_next, theta_next, ref_x, ref_y)

class DomoDeFerro:
    def __init__(self, anticipation_time=1.0, radius=3.0):
        self.anticipation_time = anticipation_time
        self.radius = radius

    def check_interception(self, defender, ball, dt):
        ball_future = ball.predict_next_cartesian(self.anticipation_time)
        defender_future = defender.predict_next_cartesian(self.anticipation_time)
        dist = np.hypot(defender_future[0] - ball_future[0], defender_future[1] - ball_future[1])
        return dist < self.radius

    def adjust_trajectory(self, defender, ball, dt):
        if self.check_interception(defender, ball, dt):
            ball_future = ball.predict_next_cartesian(self.anticipation_time)
            dx = ball_future[0] - defender.x
            dy = ball_future[1] - defender.y
            norm = np.hypot(dx, dy)
            if norm > 0:
                defender.vx = dx / self.anticipation_time
                defender.vy = dy / self.anticipation_time
        return defender

class Predictor:
    def __init__(self, anticipation_time=1.0, domo_radius=3.0):
        self.domo = DomoDeFerro(anticipation_time, domo_radius)

    def predict(self, players, ball, n_frames=30, dt=1.0):
        predictions = []
        players_states = [Entity(p.x, p.y, p.vx, p.vy, p.ax, p.ay) for p in players]
        ball_state = Entity(ball.x, ball.y, ball.vx, ball.vy, ball.ax, ball.ay)

        for frame in range(n_frames):
            frame_positions = []
            for i, player in enumerate(players_states):
                if self.domo.check_interception(player, ball_state, dt):
                    players_states[i] = self.domo.adjust_trajectory(player, ball_state, dt)
            for player in players_states:
                next_x, next_y = player.predict_next_cartesian(dt, ref_x=0, ref_y=0)
                player.update_state(next_x, next_y, player.vx, player.vy, player.ax, player.ay)
                frame_positions.append((next_x, next_y))
            next_ball_x, next_ball_y = ball_state.predict_next_cartesian(dt, ref_x=0, ref_y=0)
            ball_state.update_state(next_ball_x, next_ball_y, ball_state.vx, ball_state.vy, ball_state.ax, ball_state.ay)
            frame_positions.append((next_ball_x, next_ball_y))
            predictions.append(frame_positions)
        return predictions