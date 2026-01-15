
```
activate base
conda create --name csttnt_env ipykernel
deactivate

activate csttnt_env
python -m ipykernel install --user --name csttnt_env --display-name "csttnt_env"
deactivate
```