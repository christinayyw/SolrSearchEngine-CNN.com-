import networkx as nx
G=nx.read_edgelist("edgelist3.txt",create_using=nx.DiGraph())
pr = nx.pagerank(G,alpha=0.85, personalization=None, max_iter=30, tol=1e-06,nstart=None,weight='weight',dangling=None)
with open("pagerank2.txt","w")as fout:
    for doc in pr:
        fout.write(doc + "="+str(pr[doc]) + "\n")
        
fout.close()
