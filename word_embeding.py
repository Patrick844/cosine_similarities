#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import math


# In[70]:


def similarities(s1,s2):
    
    s1=s1.lower()
    s2=s2.lower()

    #split the string into an array of words
    s1_list=s1.split()
    s2_list=s2.split()
    
    for ss in s1_list:
        if not ss.isalnum():
            s1_list.remove(ss)
            
    for ss in s2_list:
        if not ss.isalnum():
            s2_list.remove(ss)
            
        
    
    #remove duplicates and co;bine them
    s1_set=set(s1_list)
    s2_set=set(s2_list)
    
    s_set=s1_set.union(s2_set)
    
    
    #Count the occurence of a word
    dict1={}
    dict2={}
    
    #initialize the word to 0
    for s in s_set:
        dict1[s]=0
        dict2[s]=0
        
        #add the occurence of the word to a dictionary
        for word in s1_list:
            if s == word:
                dict1[s]=dict1[s]+1
                
        for word2 in s2_list:
            if s == word2:
                dict2[s]=dict2[s]+1
                
    #get the list of value and convert to numpy --> vector            
    v1=np.array(list(dict1.values()))
    v2=np.array(list(dict2.values()))
    
   
    #Dot product of two vector
    dot_product=v1.dot(v2)
    
    #manual calcul of norm
    norm_v1=calculate_norm(v1)
    norm_v2=calculate_norm(v2)
    
    #norm_v1=np.linalg.norm(v1)  norm with numpy
    #norm_v2=np.linalg.norm(v2)  norm with numpy
    
    cosine_sim=dot_product/(norm_v1*norm_v2)
    
    
    return cosine_sim
    
    
        
def calculate_norm(v):
    total=0
    
    for vs in v:
        total+=vs**2

        
        
    return math.sqrt(total)
        
        

        

            
    
    


# In[71]:


sentence1="Mammals (from Latin mamma, 'breast') are a group of vertebrate animals constituting the class Mammalia (/məˈmeɪliə/), and characterized by the presence of mammary glands which in females produce milk for feeding (nursing) their young, a neocortex (a region of the brain), fur or hair, and three middle ear bones. These characteristics distinguish them from reptiles and birds, from which they diverged in the Carboniferous, over 300 million years ago. Around 6,400 extant species of mammals have been described. The largest orders are the rodents, bats and Eulipotyphla (hedgehogs, moles, shrews, and others). The next three are the Primates (including humans, apes, monkeys, and others), the Artiodactyla (cetaceans and even-toed ungulates), and the Carnivora (cats, dogs, seals, and others)."
sentence2 = "mammal, (class Mammalia), any member of the group of vertebrate animals in which the young are nourished with milk from special mammary glands of the mother. In addition to these characteristic milk glands, mammals are distinguished by several other unique features. Hair is a typical mammalian feature, although in many whales it has disappeared except in the fetal stage. The mammalian lower jaw is hinged directly to the skull, instead of through a separate bone (the quadrate) as in all other vertebrates. A chain of three tiny bones transmits sound waves across the middle ear. A muscular diaphragm separates the heart and the lungs from the abdominal cavity. Only the left aortic arch persists. (In birds the right aortic arch persists; in reptiles, amphibians, and fishes both arches are retained.) Mature red blood cells (erythrocytes) in all mammals lack a nucleus; all other vertebrates have nucleated red blood cells."

similarities(sentence1,sentence2)

