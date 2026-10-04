import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

OUT_DIR = "data/test_images"
os.makedirs(OUT_DIR, exist_ok=True)

def save(fig, name):
    fig.savefig(os.path.join(OUT_DIR, name), dpi=100, bbox_inches="tight")
    plt.close(fig)

def chart_redgreen():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(["A","B","C","D"], [5,7,4,6], color=["red","green","red","green"])
    ax.set_title("Red vs Green Bar Chart")
    save(fig, "chart_redgreen.png")

def chart_multiline():
    fig, ax = plt.subplots(figsize=(6,4))
    x = np.linspace(0,10,50)
    colors = ["#d62728","#ff7f0e","#8c564b","#bcbd22","#2ca02c"]
    for i,c in enumerate(colors):
        ax.plot(x, np.sin(x+i), color=c, label=f"line {i+1}")
    ax.legend()
    ax.set_title("Multi-line Similar Colors")
    save(fig, "chart_multiline.png")

def heatmaps():
    Z = np.add.outer(np.sin(np.linspace(0,6,60)), np.cos(np.linspace(0,6,60)))
    for cmap in ["jet","viridis"]:
        fig, ax = plt.subplots(figsize=(6,4))
        im = ax.imshow(Z, cmap=cmap)
        fig.colorbar(im)
        ax.set_title(f"Heatmap - {cmap}")
        save(fig, f"heatmap_{cmap}.png")

def map_regions():
    rng = np.random.default_rng(0)
    labels = rng.integers(0,4,(12,16))
    labels = np.kron(labels, np.ones((10,10)))
    fig, ax = plt.subplots(figsize=(6,4))
    cmap = ListedColormap(["red","green","orange","blue"])
    ax.imshow(labels, cmap=cmap)
    ax.axis("off")
    ax.set_title("Region Map")
    save(fig, "map_regions.png")

def ui_status():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.axis("off")
    systems = [
        ("Server A","green"),
        ("Server B","red"),
        ("Server C","green"),
        ("Server D","orange"),
    ]
    for i,(name,color) in enumerate(systems):
        ax.add_patch(plt.Circle((0.2,0.8-i*0.2),0.05,color=color))
        ax.text(0.3,0.78-i*0.2,name,fontsize=12)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_title("System Status Dashboard")
    save(fig, "ui_status.png")

if __name__ == "__main__":
    chart_redgreen()
    chart_multiline()
    heatmaps()
    map_regions()
    ui_status()
    print("Images created successfully!")