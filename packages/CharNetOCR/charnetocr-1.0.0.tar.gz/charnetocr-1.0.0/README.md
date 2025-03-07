# CharNet OCR


> 💡 Being the very first version, CharNet's performance is currently a baseline, __and it only accepts images having solid `#FFF` background and solid `#000` text.__
> 
> ❓ It is being planned to improve the model's performance and make it more robust in the upcoming versions.


--- 


An Optical Character Recognition library for Python. It recognizes character-by-character and produces text of words present in the image. An ensemble of 3 YOLOv8-nano models that determines the character-level bounding boxes and labels. 


## About the models

| Model | Description |
|---|---|
| CharNetLC | Character-level detection model for lower-case alphabets |
| CharNetUC | Character-level detection model for upper-case alphabets |
| CharNetDC | Character-level detection model for digits and special characters |


The models were trained on custom dataset of of ~2,000 fonts collected from Dafont's ["Script > Handwritten"](https://www.dafont.com/theme.php?cat=603&l[]=10&l[]=1) section (under "100% free" filter).


## Getting Started

### Installation 

```bash
pip install CharNetOCR
```

### Usage 

```py
from CharNetOCR import recognize 

my_img = './test.png'

data = recognize(
    img_path=my_img,

    # Additional parameters (optional):
    verbose=False, # True by default
    word_configs={
        'kernel': (5, 5), # kernel size for morphological operations
        'iterations': 2, # number of iterations for morphological operations
    },
    char_weights={
        'lowercase': 1.0,
        'uppercase': 0.95, 
        'digits_and_special_chars': 0.85
    }
)

# data = (word_str, bbox_coords, confidence)[]
```

For the `recognize` function, you can pass the following parameters:

| Parameter | Default | Description |
| --- | --- | --- |
| `img_path` | None | Path to the image file |
| `verbose` | True | Whether to print the progress or not |
| `word_configs` | `{ 'kernel': (5, 5), 'iterations': 2 }` | Morphological operations configurations |
| `char_weights` | `{ 'lowercase': 1.0, 'uppercase': 0.95, 'digits_and_special_chars': 0.85 }` | Weights for the CharNet models |


## How it works?

### 1. Image segmentation 

![Image Segmentation](./assets/working-segmentation.png)

1. First, all words are segmented in the image through word-level bounding boxes determination using OpenCV. 

2. Then, we iterate through each "bbox" in the list of word's bounding boxes. On each iteration, 

    - The segment of the image is cropped using the bounding box coordinates.
    - The segmented image is padded to remove dramatic enlargement of the word.
    - The processed image is saved temporarily and passed into the ensemble of CharNet models.
    - We receive a combined character-level prediction. We delete the temporary image
    - And append the predicted text to the final list of words.


### 2. CharNet Ensembling 

![Image Segmentation](./assets/working-ensembling.png)


1. The cropped image is passed through the ensemble of CharNet models.
2. Each model predicts the character-level bounding boxes and labels.
3. The highest-confidence bounding box is selected from the 3 models for each character.

> 🎯 And the best part? You can control the weights of the models to get the best results!


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feat/awesome-feature`)
3. Commit the changes (`git commit -am 'Add awesome feature'`)
4. Push to the branch (`git push origin feat/awesome-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.


## Credits 

This project was developed by [Aakash](https://www.aakash.engineer/) and [Vikas Jha](https://github.com/Saizuo) for the Open Source Community.