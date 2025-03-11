
# Simple-lama-inpainting

Simple pip package originally from [LeftRefill](https://github.com/ewrfcas/LeftRefill)[1] inpainting with reference. Edited from the [wrapper](https://github.com/DavidXu-JJ/StreetUnveiler/blob/main/utils/left_refill_utils.py) from StreetUnveiler[2]

The API design is similar to [simple-lama-inpainting](https://github.com/enesmsahin/simple-lama-inpainting).

## Installation

```bash
pip install simple-leftrefill-inpainting
```

# CLI

```bash
simple_leftrefill <path_to_inpainted_image> <path_to_mask_image> <path_to_reference_image> <path_to_output_image>
```

# How to use in your code

```python
from diffusers.utils import load_image
from simple_leftrefill_inpainting import LeftRefillGuidance

model = LeftRefillGuidance()

result = model.predict(
    load_image("./assets/inpainted.png"),
    load_image("./assets/mask.png"),
    load_image("./assets/reference.png"),
)

result.save("./assets/result.png")
```

# Illustration

Inpainted Input:

![](./assets/inpainted.png)

Inpainting Mask:

![](./assets/mask.png)

Reference Mask:

![](./assets/reference.png)

Result:

![](./assets/result.png)

# License

Please follow both LeftRefill license and the license in this repo.

# Reference

[1] Cao et al. LeftRefill: Filling Right Canvas based on Left Reference through Generalized Text-to-Image Diffusion Model. CVPR 2024

```
@inproceedings{cao2024leftrefill,
      title={LeftRefill: Filling Right Canvas based on Left Reference through Generalized Text-to-Image Diffusion Model}, 
      author={Chenjie Cao and Yunuo Cai and Qiaole Dong and Yikai Wang and Yanwei Fu},
      booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
      year={2024},
}
```

[2] Xu et al. 3D StreetUnveiler with Semantic-aware 2DGS - a simple baseline. ICLR 2025

```
@inproceedings{xu2025streetunveiler,
  author       = {Jingwei Xu and Yikai Wang and Yiqun Zhao and Yanwei Fu and Shenghua Gao},
  title        = {3D StreetUnveiler with Semantic-aware 2DGS - a simple baseline},
  booktitle    = {The International Conference on Learning Representations (ICLR)},
  year         = {2025},
}
```
