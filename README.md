# End to End Machine Learning Project

## Structure 
### 📁 Project Structure
- 📁 artifacts
- 📁 logs
- 📁 notebook
- 📁 src  
  - 📁 components  
    - 📄 __init__.py  
    - 📄 data_ingestion.py  
    - 📄 data_transformation.py  
    - 📄 model_trainer.py
    - 📄 model_evaluation.py
  - 📁 pipeline  
    - 📄 __init__.py  
    - 📄 train_pipeline.py  
    - 📄 predict_pipeline.py
  - 📄 __init__.py   
  - 📄 exception.py  
  - 📄 logger.py  
  - 📄 utils.py 
- venv
- templates
  - home.html
  - index.html
- 📄 app.py 
- Dockerfile 
- Readme.md
- 📄 requirements.txt 
- 📄 setup.py 


---
## Environment Setup
```
conda create -p venv python==3.12.12 -y

$ conda activate directory/Projects/ETEML/ml-projects/venv
$ conda deactivate
$ conda env list 

pip install -r requirements.txt
```
---
Source : [End to End Machine Learning Project](https://github.com/krishnaik06/mlproject)