# GPU Usage
How to use a single GPU.

Todo:
- How to use several GPU.
- GPU parallelism.


## Tensor Initial
Tensor can be initialized directly on the GPU.
```python
X = torch.ones(2, 3, device=try_gpu())
```

## nn.Module 
Using `.to(device = )` to create module on GPU.
```python
net = nn.Sequential(nn.Linear(3, 1))
net = net.to(device=try_gpu())
```