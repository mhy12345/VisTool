import torch
def torch_to_numpy(data):
    if isinstance(data, torch.Tensor):
        data = data.detach()
        if data.is_cuda:
            data = data.cpu()
        data = data.numpy()
    return data

