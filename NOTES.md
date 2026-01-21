
+ Thao tac tao moi truong tren Anaconda
```
conda env list
activate base
conda create --name csttnt_env ipykernel
deactivate

activate csttnt_env
python -m ipykernel install --user --name csttnt_env --display-name "csttnt_env"
deactivate

activate csttnt_env
pip install numpy, ...
deactivate
```