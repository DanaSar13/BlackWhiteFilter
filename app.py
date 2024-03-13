import numpy as np

def black_and_white(image):
    # Grayscale conversion matrix
    bw_filter = np.array(
        [[0.2989, 0.587, 0.114],
         [0.2989, 0.587, 0.114],
         [0.2989, 0.587, 0.114]]
    )
    # Apply the grayscale conversion
    bw_img = image.dot(bw_filter.T)
    bw_img /= bw_img.max()
    return bw_img

import gradio as gr

# Create a Gradio interface for the black and white conversion
gr.Interface(fn=black_and_white, inputs="image", outputs="image").launch();
