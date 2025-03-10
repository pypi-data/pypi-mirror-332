# Charm: The Missing Piece in ViT fine-tuning for Image Aesthetic Assessment

> [**Accepted at CVPR 2025**](https://cvpr.thecvf.com/virtual/2025/poster/34423)<br>

We introduce **Charm** , a novel tokenization approach that preserves **C**omposition, **H**igh-resolution,
**A**spect **R**atio, and **M**ulti-scale information simultaneously. By preserving critical aesthetic information, <em> Charm </em> achieves significant performance improvement across different image aesthetic assessment datasets.


### Quick Inference

* Step 1) Check our [GitHub Page](https://github.com/FBehrad/Charm/) and install the requirements. 

```setup
pip install -r requirements.txt
```
* Step 2) Install Charm tokenizer.
```setup
pip install Charm_tokenizer
```

* Step 3) Tokenization + Position embedding preparation

[//]: # (![Charm tokenizer]&#40;charm.gif&#41;)
```python
from Charm_tokenizer.ImageProcessor import Charm_Tokenizer

img_path = r"img.png"

charm_tokenizer = Charm_Tokenizer(patch_selection='frequency', training_dataset='tad66k', without_pad_or_dropping=True)
tokens, pos_embed, mask_token = charm_tokenizer.preprocess(img_path)
```
The mask_token indicates which patches are in high resolution and which are in low resolution.


* Step 4) Predicting aesthetic score

```python
from Charm_tokenizer.Backbone import backbone

model = backbone(training_dataset='tad66k', device='cpu')
prediction = model.predict(tokens, pos_embed, mask_token)
```

**Note:**
1. While random patch selection during training helps avoid overfitting,for consistent results during inference, fully deterministic patch selection approaches should be used. 
2. For the training code, check our [GitHub Page](https://github.com/FBehrad/Charm/).