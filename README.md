# proj-jaly m6A Modification Detection Model

This repository contains the source code for our ML model to identify RNA modifications from direct RNA-Seq data (Task 1), as well our prediction of m6A sites in all SG-NEx direct RNA-Seq samples (Task 2).

## Definitions of folders
1. `proj_jaly_student_evaluation`: files needed to reproduce our model to make predictions on a test dataset
2. `predictions` : examples of predictions run with our model
    * `jaly_test_results.csv` - predictions for `test-dataset.json`
    * `jaly_dataset1.csv` - predictions for `dataset1.json`
    * `jaly_dataset2.csv` - predictions for `dataset2.json`
    * `jaly_dataset3.csv` - predictions for `dataset3.json`
3. `project_code`: python code for project
    * `FinalDataParsing.ipynb` - data parsing of the 3 json file datasets
    * `FinalProjectModelCode.ipynb` - XGBoost model on the 3 datasets
    * `SGNexDataVisualization.ipynb` - visualisations on full SG-NEx data
    * `A549_replicate5.py` - sample python script to run our model on a single SG-NEx direct RNA-Seq sample (task 2)

## Files needed for student evaluation
The files needed for other teams' student evaluation are located in the `proj_jaly_student_evaluation` folder. <br/>
Follow Installation and Method Guide to clone this Github repo (do not have to manually download these files) <br/>
This folder contains: 
1. `test-dataset.json` : a small sample subset of `dataset1.json` for the other team to test our model on
2. `XGboostModel.json` : our saved XGBoost model
3. `packages.sh` : shell script to install Python packages
4. `python_script_test.py` : python script to run our model on test dataset and obtain csv output file with predictions

## Installation and Method Guide (Student evaluation)
1. Log onto AWS Research Gateway and start a `t3.2xlarge` instance on Ubuntu 20 04 Large.

2. Connect to SSH/RDP

3. Check python version
```
python3 --version
```

4. Update your local system's repository list by entering the following command
```
sudo apt update
```

5. Download Python3
```
sudo apt install python3
```

6. Install pip for the packages. Type 'Y' to continue installing.
```
sudo apt install python3-pip
```

7. Go to your AWS ProjectStorage directory
```
cd studies/ProjectStorage
```

8. Make environment to clone github
```
mkdir git_env
cd git_env
git clone https://github.com/jialin-low/dsa4262-jaly.git
```

9. Go to directory with test dataset, model, and python script
```
cd dsa4262-jaly/proj_jaly_student_evaluation 
```

10. Run shell script to install python packages
```
sh packages.sh
```

11. Run python script. There will be a csv output file named `jaly_test_results.csv` in your ProjectStorage.
```
python3 python_script_test.py
```

## User Guide to access csv output file
1. After completing the above guide, head to your ProjectStorage under `My Products` in AWS Research Gateway
<img width="385" alt="image" src="https://user-images.githubusercontent.com/73953587/199913114-451a51fc-fbe9-4670-9214-c572e5007997.png">

2. Click on the `Explore` button
<img width="1224" alt="Screenshot 2022-11-04 at 4 02 37 PM (2)" src="https://user-images.githubusercontent.com/73953587/199931575-4efc6cc6-fc12-4f7b-ba7e-84bd94e50b16.png">

3. Go into the `Shared` folder
<img width="1263" alt="Screenshot 2022-11-04 at 4 53 28 PM (2)" src="https://user-images.githubusercontent.com/73953587/199932333-7d102d24-c568-4b3f-a399-690f7b571388.png">

4. Find and click onto folder named `git_env`, followed by the folder named `dsa4262-proj-jaly`, and lastly the folder named `proj_jaly_student_evaluation`. You should see the PATH as `Shared/git_env/dsa4262-proj-jaly/proj_jaly_student_evaluation`.
<img width="1265" alt="image" src="https://user-images.githubusercontent.com/73953587/199932981-e0d13176-fee6-40bb-8fbd-32c20877d33f.png">

5. Download `jaly_test_results.csv` by clicking on the three dots to view the output file with the predictions. 
<img width="1226" alt="image" src="https://user-images.githubusercontent.com/73953587/199933773-72ec3f03-0bb7-4e28-9209-8e2cafc02805.png">
