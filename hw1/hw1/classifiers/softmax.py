import numpy as np
from random import shuffle

def softmax_loss_simple(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  # If you get stuck, don't forget about these resources:                     #
  # http://cs231n.github.io/neural-networks-case-study/#linear                #
  # http://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/#
  #############################################################################


  D,C = W.shape
  N,D = X.shape  
  
  for x in xrange(0, D):
    weights = np.dot(W.T, X[x, :])
    weights -= np.max(weights) # subtract max to prevent instability
    
    loss -= weights[y[x]]
    sum_exp = 0.0
    
    for w in weights:
        sum_exp += np.exp(w)
        
    for i in xrange(0, D):
        dW[i, :] += (1.0 / sum_exp * np.exp(weights[i]) * X[x, :])
        if i == y[x]:
            dW[i, :] -= X[:, x]
            
    loss += np.log(curr_sum)
    loss /= num_train # average loss over number of training examples
    
    dW /= num_train # average gradient over number of training examples

  # Add regularization to loss
  loss += 0.5 * reg * np.sum(W * W)

  # Add regularization to gradient
  dW += reg * W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_fast(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

