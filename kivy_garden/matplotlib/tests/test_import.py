import pytest


def test_flower():
    import matplotlib
    matplotlib.use('module://kivy_garden.matplotlib.backend_kivy')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
