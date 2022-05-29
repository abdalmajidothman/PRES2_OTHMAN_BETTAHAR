#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np 
# importing pandas package
import pandas as pandasForSortingCSV
  
# assign dataset 
csvData = pandasForSortingCSV.read_csv("sample.csv")
                                         

  
# sort data frame
csvData.sort_values(["probe_dst_addr","probe_ttl"], 
                    axis=0,
                    ascending=[False, False], 
                    inplace=True)
  


dataList =  list(csvData["probe_dst_addr"])
dataList2 =  list(csvData["reply_src_addr"])
rtt= list(csvData["rtt"])
mpls=list(csvData["reply_mpls_labels"])
replysize=list(csvData["reply_size"])
replyttl=list(csvData["reply_ttl"])
probe_ttl=list(csvData["probe_ttl"])


# max nb of nodes
nombredenoeuds=1000



noeud = []
noeuds = []
arretelist= []
listeNoeuds = []
lenght = len(dataList)
G = nx.Graph()


for i in range(lenght):
    #stops if max nb nodes is reached
    if i == lenght - 1 or G.number_of_nodes()==nombredenoeuds : 
        break

    if dataList[ i ] == dataList[i + 1]  and dataList[ i ] != "::"  :
       
       if dataList2[i] not in noeud :
         noeud.append(dataList2[i])
         G.add_node(dataList2[i],label = "" + dataList2[i] ,destination=dataList[i] , adresse=dataList2[i], rtt=rtt[i], replysize=replysize[i], replyttl=replyttl[i], probe_ttl=probe_ttl[i], mplsreplys=mpls[i], ifmpls=(mpls[i]!="[]"), col = 'red')
         print(dataList2[i])
         print(G.number_of_nodes())
         if probe_ttl[i] == probe_ttl[i+1]+1 and [dataList2[i],dataList2[i+1]] not in arretelist and [dataList2[i+1],dataList2[i]] not in arretelist and  dataList2[i] !=dataList2[i+1]  :
          arretelist.append([dataList2[i],dataList2[i+1]])
    else : 
        if dataList[ i ] == dataList[i - 1] and dataList[ i ] != "::"   : 
            if dataList2[i] not in noeud:
                noeud.append(dataList2[i])
                G.add_node(dataList2[i],label = "" + dataList2[i] ,destination=dataList[i] , adresse=dataList2[i], rtt=rtt[i], replysize=replysize[i], replyttl=replyttl[i], probe_ttl=probe_ttl[i], mplsreplys=mpls[i], ifmpls=(mpls[i]!="[]") ,col = 'red')
                print(dataList2[i])
                if probe_ttl[i]-1 == probe_ttl[i-1] and [dataList2[i],dataList2[i-1]] not in arretelist and [dataList2[i-1],dataList2[i]] not in arretelist and dataList2[i] !=dataList2[i-1] :
                 arretelist.append([dataList2[i],dataList2[i-1]])
            lengthchemin= len(noeud)-1
            noeud = []
            


for arrete in arretelist :

                if arrete not in noeuds :
                    print(arrete)
                    noeuds.append(arrete)
                    G.add_edge(arrete[0],arrete[1],weight=1,styl='solid')

print("\n") 


  
      
print(G)

#exporting to gexf
nx.write_gexf(G, "test.gexf")
