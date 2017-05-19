import numpy as np
from random import shuffle

def structured_loss_simple(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops)
  Inputs:
  - W: C x D array of weights
  - X: D x N array of data. Data are D-dimensional columns
  - y: 1-dimensional array of length N with labels 0...K-1, for K classes
  - reg: (float) regularization strength
  Returns:
  a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  dW = np.zeros(W.shape) # initialize the gradient as zero

  # compute the loss and the gradient
  num_classes = W.shape[0]
  num_train = X.shape[1]
  loss = 0.0
  for i in xrange(num_train):
    scores = W.dot(X[:,i])
    correct_class_score = scores[y[i]]
    for j in xrange(num_classes):
      if j == y[i]: # If correct class
        continue
      margin = scores[j] - correct_class_score + 1 # note delta = 1
      if margin > 0:
        loss += margin
        dW[j, :] += X[:, i].T
        dW[y[i], :] -= X[:, i].T
  
  #############################################################################
  # TODO:                                                                     #
  # Compute the gradient of the loss function and store it dW.                #
  # Rather that first computing the loss and then computing the derivative,   #
  # it may be simpler to compute the derivative at the same time that the     #
  # loss is being computed. As a result you may need to modify some of the    #
  # code above to compute the gradient.                                       #
  #############################################################################

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train

  # Average gradients as well
  dW /= num_train

  # Add regularization to the loss.
  loss += 0.5 * reg * np.sum(W * W)

  # Add regularization to the gradient
  regularization = reg * W
  dW += regulartization

  return loss, dW


def structured_loss_fast(W, X, y, reg):
  """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as structured_loss_simple.
  """
  loss = 0.0
  dW = np.zeros(W.shape) # initialize the gradient as zero

  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the structured SVM loss, storing the    #
  # result in loss.                                                           #
  #############################################################################

  # compute the loss and the gradient

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.

  # Add regularization to the loss.

  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################
  
  scores = np.dot(W, X) # also known as f(x_i, W)

  correct_scores = np.ones(scores.shape) * scores[y, np.arange(0, scores.shape[1])]
  deltas = np.ones(scores.shape)
  L = scores - correct_scores + deltas

  L[L < 0] = 0
  L[y, np.arange(0, scores.shape[1])] = 0 # Don't count y_i
  loss = np.sum(L)

  # Average over number of training examples
  num_train = X.shape[1]
  loss /= num_train

  # Add regularization
  loss += 0.5 * reg * np.sum(W * W)

  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the gradient for the structured SVM     #
  # loss, storing the result in dW.                                           #
  #                                                                           #
  # Hint: Instead of computing the gradient from scratch, it may be easier    #
  # to reuse some of the intermediate values that you used to compute the     #
  # loss.                                                                     #
  #############################################################################

  grad = np.zeros(scores.shape)

  L = scores - correct_scores + deltas

  L[L < 0] = 0
  L[L > 0] = 1
  L[y, np.arange(0, scores.shape[1])] = 0 # Don't count y_i
  L[y, np.arange(0, scores.shape[1])] = -1 * np.sum(L, axis=0)
  dW = np.dot(L, X.T)

  # Average over number of training examples
  num_train = X.shape[1]
  dW /= num_train

  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

  return loss, dW
