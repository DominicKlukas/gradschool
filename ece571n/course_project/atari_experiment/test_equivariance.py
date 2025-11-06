import torch
import numpy as np

import matplotlib.pyplot as plt

from escnn import gspaces
from escnn import nn

obs_np = np.load("np_obs.npy")
obs_stacked = np.load("obs.npy")
obs_stacked = torch.from_numpy(obs_stacked)

obs_one = torch.from_numpy(obs_np)
obs_one = obs_one.unsqueeze(0).unsqueeze(0)


r2_act = gspaces.flip2dOnR2(np.pi/2)

feat_type_stacked = nn.FieldType(r2_act, 4*[r2_act.trivial_repr])

feat_type_in = nn.FieldType(r2_act, [r2_act.trivial_repr])

feat_type_out = nn.FieldType(r2_act, [r2_act.trivial_repr, r2_act.trivial_repr, r2_act.regular_repr])

obs_one = feat_type_in(obs_one)

images = []

for g in r2_act.testing_elements:
    images += [obs_one.transform(g).tensor.squeeze().numpy()]

fig, ax = plt.subplots()
idx = 0
# Create the first image
im = ax.imshow(images[idx], cmap='gray')
ax.set_title(f"Image {idx}")

def on_key(event):
    global idx
    if event.key == 'right':
        idx = (idx + 1) % len(images)
    elif event.key == 'left':
        idx = (idx - 1) % len(images)
    else:
        return  # ignore other keys

    im.set_data(images[idx])
    ax.set_title(f"Image {idx}")
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()


