# Simple GPU Queue
> Simple GPU Queue: For running lots of smaller experiments on your handful of GPUs
> 


## For Development
```
conda env create -f environment.yml
conda activate simple-gpu-queue
pip install -r requirements.txt
# pip install -r requirements-dev.txt
```

Start the server

```
python simple_gpu_queue.py 4 # Machine with 4 GPUs
```

Check the server is running, navigate to `http://localhost:5034/docs`, test the routes

