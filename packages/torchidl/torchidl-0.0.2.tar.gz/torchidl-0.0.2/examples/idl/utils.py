import torch
import datetime
import os
import random
import numpy as np

def transpose(X):
    """
    Convenient function to transpose a matrix.
    """
    assert len(X.size()) == 2, "data must be 2D"
    return X.T

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

def get_test_accuracy(model, loss_fn, test_loader, device):
    """
    Run the model with the test dataset and compute the loss and accuracy.
    """
    model.eval() # eval mode
    total_loss = 0.0
    correct_predictions = 0
    total_samples = 0

    with torch.no_grad(): 
        for inputs, targets in test_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            predictions = model(inputs)
            if not isinstance(predictions, torch.Tensor):
                predictions = torch.from_numpy(predictions).to(device)

            # Compute loss
            loss = loss_fn(predictions, targets)
            total_loss += loss.item()

            # Compute accuracy
            predicted_labels = torch.argmax(predictions, dim=-1)
            correct_predictions += (predicted_labels == targets).sum().item()
            total_samples += targets.size(0)

    avg_loss = total_loss / len(test_loader)
    accuracy = correct_predictions / total_samples
    model.train() # train mode
    return avg_loss, accuracy


def train(args, model, train_loader, test_loader, optimizer, loss_fn, num_epochs, log_dir, device):
    """
    Trains the model for a specified number of epochs and logs the results.

    Args:
        model (torch.nn.Module): The model to train.
        train_loader (torch.utils.data.DataLoader): The training data loader.
        test_loader (torch.utils.data.DataLoader): The test data loader.
        optimizer (torch.optim.Optimizer): The optimizer used for training.
        loss_fn (torch.nn.Module): The loss function to minimize.
        num_epochs (int): The number of epochs to train the model.
        log_dir (str): The base directory to save log files.
        device (torch.device, optional): The device (CPU or GPU) to perform training on.

    Returns:
        tuple: The trained model and the log file path.
    """

    model.to(device)

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
    log_file.write("Epoch,Train Loss,Train Accuracy,Test Loss,Test Accuracy\n")

    # Training loop
    for epoch in range(num_epochs):
        model.train()  # train mode
        train_loss = 0.0
        correct_train = 0
        total_train = 0

        batch_idx = 0
        total_batches = len(train_loader) 

        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)

            # Forward pass
            predictions = model(inputs)
            loss = loss_fn(predictions, targets)

            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            predicted_labels = torch.argmax(predictions, dim=-1)
            correct_train += (predicted_labels == targets).sum().item()
            total_train += targets.size(0)
            train_loss += loss.item()

            if batch_idx % 100 == 0:
                test_loss, test_accuracy = get_test_accuracy(model, loss_fn, test_loader, device)

                print(f"Epoch {epoch + 1}/{num_epochs} - "
                      f"Batch {batch_idx + 1}/{total_batches}: "
                      f"Train Loss: {loss.item():.4f}, Train Accuracy: {100 * correct_train / total_train:.2f}%, "
                      f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy * 100:.2f}%")

            
                log_file.write(f"Epoch {epoch + 1}/{num_epochs} - "
                        f"Batch {batch_idx + 1}/{total_batches}: "
                        f"Train Loss: {loss.item():.4f}, Train Accuracy: {100 * correct_train / total_train:.2f}%, "
                        f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy * 100:.2f}%\n")

            batch_idx += 1

        avg_train_loss = train_loss / len(train_loader)
        train_accuracy = (correct_train / total_train) * 100
        test_loss, test_accuracy = get_test_accuracy(model, loss_fn, test_loader, device)

        print(f"Epoch {epoch + 1}/{num_epochs}: "
              f"Train Loss: {avg_train_loss:.4f} | Train Accuracy: {train_accuracy:.2f}% | "
              f"Test Loss: {test_loss:.4f} | Test Accuracy: {test_accuracy * 100:.2f}%")
        log_file.write(f"Epoch {epoch + 1}/{num_epochs}: "
                f"Train Loss: {avg_train_loss:.4f} | Train Accuracy: {train_accuracy:.2f}% | "
                f"Test Loss: {test_loss:.4f} | Test Accuracy: {test_accuracy * 100:.2f}%\n")

        log_file.write("-" * 100 + "\n")
        print("-" * 100)

    return model, log_file