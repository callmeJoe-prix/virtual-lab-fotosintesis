import matplotlib.pyplot as plt

def plot_light_curve(df):
    fig, ax = plt.subplots()
    ax.plot(df["light"], df["rate"])
    ax.set_xlabel("Intensitas Cahaya")
    ax.set_ylabel("Laju Fotosintesis")
    ax.set_title("Kurva Respon Cahaya")
    return fig

def plot_o2_output(light, o2):
    fig, ax = plt.subplots()
    ax.bar([light], [o2])
    ax.set_xlabel("Intensitas Cahaya")
    ax.set_ylabel("Produksi O₂")
    ax.set_title("Output Oksigen")
    return fig
