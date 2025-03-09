import torch
from torch import nn
from sklearn.model_selection import train_test_split
import numpy as np
from gamma.optim import _optimizer
from gamma.loss import _loss_fn

def is_same_device(t, device):
    if isinstance(t, torch.Tensor):
        return t.device == device
    elif isinstance(t, np.ndarray):
        return device == torch.device('cpu') or device == 'cpu' or device is None
    elif isinstance(t, list):
        return all(is_same_device(item, device) for item in t)
    elif isinstance(t, nn.Module):
        params = list(t.parameters())
        return len(params) == 0 or params[0].device == device
    
    raise ValueError(f"Invalid type: {type(t)}")

def get_device(t):
    if isinstance(t, torch.Tensor):
        return t.device
    elif isinstance(t, np.ndarray):
        return torch.device('cpu')
    elif isinstance(t, list):
        return get_device(t[0])
    elif isinstance(t, nn.Module):
        params = list(t.parameters())
        return params[0].device if len(params) > 0 else torch.device('cpu')
    
    return torch.device('cpu')

def to_tensor(x):
    if isinstance(x, torch.Tensor):
        return x
    return torch.tensor(x)
class Trainer:
    def __init__(self, model, optimizer, loss_fn, after_train=None, lr=0.01, device=None):
        self.model = model
        self.optimizer = _optimizer(model, optimizer, lr)
        self.loss_fn   = _loss_fn(loss_fn)
        self.after_train = after_train
        self.device = device
        if self.device is None: # if device is not specified, use the device of the model
            self.device = get_device(self.model)

    def train(self, X, y, val_data=None, split_val=False, epochs=10, batch_size=32):
        if not is_same_device(self.model, self.device):
            self.model = self.model.to(self.device)
        
        X, y = to_tensor(X), to_tensor(y)

        has_val = True
        if split_val:
            X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        else:
            X_train, y_train = X, y
            if val_data is None:
                has_val = False
            else:
                X_val, y_val = val_data

        optimizer = self.optimizer

        history = {'train_loss': [], 'val_loss': []}

        for epoch in range(epochs):
            self.model.train()
            running_loss = 0.0

            for i in range(0, len(X_train), batch_size):
                X_batch = X_train[i:i+batch_size]
                y_batch = y_train[i:i+batch_size]
                
                if not is_same_device(X_batch, self.device):
                    X_batch = X_batch.to(self.device)
                if not is_same_device(y_batch, self.device):
                    y_batch = y_batch.to(self.device)

                optimizer.zero_grad()

                y_hat = self.model(X_batch)
                loss = self.loss_fn(y_hat, y_batch)

                loss.backward()
                optimizer.step()

                running_loss += loss.item() * len(X_batch)

            train_loss = running_loss / len(X_train)
            history['train_loss'].append(train_loss)

            if has_val:
                self.model.eval()
                val_loss = 0.0

                with torch.no_grad():
                    for i in range(0, len(X_val), batch_size):
                        X_batch = X_val[i:i+batch_size]
                        y_batch = y_val[i:i+batch_size]

                        outputs = self.model(X_batch)
                        loss = self.loss_fn(outputs, y_batch)

                        val_loss += loss.item() * len(X_batch)

                val_loss = val_loss / len(X_val)
                history['val_loss'].append(val_loss)

            print(f'Epoch {epoch+1}/{epochs} - train_loss: {train_loss:.4f} - val_loss: {val_loss:.4f}')

        return history
    
    def evaluate(self, X, y, batch_size=32):
        running_loss = 0.0
        self.model.eval()
        with torch.no_grad():
            for i in range(0, len(X), batch_size):
                X_batch = X[i:i+batch_size]
                y_batch = y[i:i+batch_size]
                loss = self.loss_fn(self.model(X_batch), y_batch)
                running_loss += loss.item() * len(X_batch)
        return running_loss / len(X)
