# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:53:26 2016

@author: cristinamenghini
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import pickle
from collections import defaultdict

script , stem, scor, ct = argv

class create_query_dict(object):
    """This class returns a dictionary whose keys are the query id and the values the list of documents related to the
    query."""
    
    def __init__(self, q_array):
        
        """ An instance created by that class is characterized by the following attribute:
        - q_array : is the n-dimentional array thhat contains the information that are goint to bu put into the
          dictionary"""
        
        self.q_array = q_array
    
    def dic_query_result(self):
        """This method returns dictionary whose keys are the query id and the values the list of documents related to the
        query."""
    
    # Zip two columns of the multidimensional array
        query_doc_id = zip(self.q_array[:,0], self.q_array[:,1])
    # Create an empry dictionary
        dic = {}
    # For each tuple of the zipped variable
        for q in query_doc_id:
        # whether doesn't exist create a key with a list as value and append to the list the sencond element of the tuple
            dic.setdefault(q[0],[]).append(q[1])
    # Return the filled dictionary
        return(dic)

def precision_at_k(k_list):
    """This function returns the precision of each query respect to a fixed K. Precisely it gives back a dictionary
    {key = k : value = precision}.
    - k_list : is the list of k's for which I want to compute the precision."""
    precision = {}
    # For each level of precision k = {1,3,5,10}
    for K in k:
        precision[K] = {}
        # For each query
        for q in queries:
            try:
                # Pick the set of the retrieved documents(k)
                set_retrieved = set(query_dic[q][:K])
                # Get the set of the relevant document for the q query
                set_relevant = set(relevant_query[q])
                # Intersect the two sets to obtain the number of relevant retrieved documents
                num_relevant_retrieved = len(set_retrieved.intersection(set_relevant))
                # Compute the precision of the
                precision[K][q] = num_relevant_retrieved*1.0/min(K,len(set_relevant))
            except:
                # Whether some query has no a grouf truth repeat the previous procedure but with an empty relevant document set
                set_relevant = []
                num_relevant_retrieved = len(set_retrieved.intersection(set_relevant))
                precision[K][q] = 0
    
    return(precision)

# Load data
query_result = np.array(pd.read_csv(str(ct)+'_DATASET/'+str(ct)+'_'+str(stem)+'/'+str(stem)+'_'+str(scor)+"/output_"+str(stem)+"_"+str(scor)+'.tsv', sep = '\t'))
ground_truth = np.array(pd.read_csv(str(ct)+'_DATASET/'+str(ct)+'_Ground_Truth.tsv', sep = '\t'))

# Define the list of K's
k = [1,3,5,10]

query_dic = create_query_dict(query_result).dic_query_result()
relevant_query = create_query_dict(ground_truth).dic_query_result()
# Define the list of queries
queries = query_dic.keys()
# Compute the precision of each query
precision_k = precision_at_k(k)
# COmpute the averege precision of the queries
average_precision = {K : np.array((precision_k[K].values())).mean() for K in k}
# Store the variable average_precision in a file.
pickle.dump( average_precision, open(str(ct)+'_DATASET/'+str(ct)+'_'+str(stem)+'/'+str(ct)+'_'+str(scor)+'avg_'+str(stem)+'_'+str(scor)+'.p', 'wb')) # Store the variable average_precision in a file.

print 'Done'