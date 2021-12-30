# Depth-Estimation-using-RCNN

## 1.0 INSTALLATION

Create a new virtual env (pip)
```
python -m venv <virtual_env>
cd Scripts\activate
```

Create a new virtual env (conda)
```
conda create -n <virtual_env> python=3.8 anaconda
conda activate <virtual_env>
```

Install dependencies

```
pip install -r requirements.txt
```

## 2.0 MODEL TRAINING

The model used to train the dataset is from U-Net architecture

![](https://miro.medium.com/max/875/1*f7YOaE4TWubwaFF7Z1fzNw.png)

Run the train.py file and tune the hyperparameters to train your own model or use the existing parameters to train the U Net model 

## 3.0 VISUALIZE DEPTH MAPS

Use the test.py file and provide the trained model as the parameter to visualize depth maps and compare with the original images
Use the visualize_single_image function to visualize single depth maps or use visulaize_depth_map to pass images in a batch 
