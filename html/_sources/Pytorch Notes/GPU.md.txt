# GPU Usage
How to use a single GPU.

Todo:
- How to use several GPU.
- GPU parallelism.


## Tensor 直接初始化
```python
X = torch.ones(2, 3, device=try_gpu())
```

## nn.Module 用`.to(device = )`
```python
net = nn.Sequential(nn.Linear(3, 1))
net = net.to(device=try_gpu())
```