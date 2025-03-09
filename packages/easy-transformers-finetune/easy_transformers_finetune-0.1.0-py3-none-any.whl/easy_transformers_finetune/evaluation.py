from sklearn.metrics import accuracy_score, f1_score

def evaluate_model(predictions, labels):
    # Assume predictions and labels are numpy arrays
    accuracy = accuracy_score(labels, predictions)
    f1 = f1_score(labels, predictions, average='weighted')
    return accuracy, f1
