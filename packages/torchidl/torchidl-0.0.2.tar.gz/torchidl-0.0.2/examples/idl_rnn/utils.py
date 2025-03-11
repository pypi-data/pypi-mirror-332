import os
import datetime
import torch
import random
import numpy as np
from typing import Any, Dict
from argparse import Namespace
from torch import nn, Tensor
from torch.optim import Optimizer
from sklearn.metrics import mean_absolute_percentage_error, r2_score


def set_seed(seed: int) -> None:
    """
    Set seed for reproducibility.
    """
    random.seed(seed) 
    np.random.seed(seed) 
    torch.manual_seed(seed) 
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


def train_time_series(
    args: Namespace,
    model: nn.Module,
    x_train: Tensor,
    y_train: Tensor,
    x_test: Tensor,
    y_test: Tensor,
    optimizer: Optimizer,
    loss_fn: nn.Module,
    log_dir: str,
    device: torch.device
) -> Dict[str, float]:
    """
    Trains a model on time series data, logs the training process, and evaluates the model.

    Args:
        args (Namespace): Contains configuration such as the number of epochs.
        model (torch.nn.Module): The model to train.
        x_train (torch.Tensor): Training features.
        y_train (torch.Tensor): Training targets.
        x_test (torch.Tensor): Test features.
        y_test (torch.Tensor): Test targets.
        optimizer (torch.optim.Optimizer): The optimizer used for training.
        loss_fn (torch.nn.Module): The loss function to minimize.
        log_dir (str): The directory to save log files.
        device (torch.device): The device (CPU or GPU) for training.

    Returns:
        Dict[str, float]: A dictionary containing model evaluation metrics.
            - 'r2': R-squared score on the test dataset.
            - 'mape': Mean Absolute Percentage Error on the test dataset.
    """
    
    model.to(device)
    x_train, y_train = x_train.to(device), y_train.to(device)
    x_test = x_test.to(device)

    # Prepare logging
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file_path = os.path.join(log_dir, f"{timestamp}.log")
    log_file = open(log_file_path, 'w')

    log_file.write("Arguments:\n")
    for arg, value in vars(args).items():
        log_file.write(f"{arg}: {value}\n")
    log_file.write("\n")
    log_file.write(f'Model size: {sum(p.numel() for p in model.parameters())} parameters\n')
    log_file.write("\n")

    # Training loop
    for epoch in range(1, args.epochs + 1):
        model.train()
        y_train_pred = model(x_train)
        loss = loss_fn(y_train_pred, y_train)

        if epoch % 10 == 0:
            log_file.write(f"Epoch {epoch}/{args.epochs}, MSE Loss: {loss.item():.4f}")
            print(f"Epoch {epoch}/{args.epochs}, MSE Loss: {loss.item():.4f}")

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Evaluation
    model.eval()
    with torch.no_grad():
        y_test_pred = model(x_test).cpu().detach().numpy()
        y_test = y_test.cpu().detach().numpy()

    mape = mean_absolute_percentage_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    log_file.write(f'Test R-square: {r2:.2f}\n')
    log_file.write(f'Test MAPE: {mape:.2f}\n')
    log_file.close()
    print(f'Test R square: {r2:.2f}')
    print(f'Test MAPE: {mape:.2f}')