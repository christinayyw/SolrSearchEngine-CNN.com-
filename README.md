# SolrSearchEngine-CNN.com-
a search engine build with Solr, on all webpages on CNN.com
- Use jsoup library to generate a edgeList which is used to create a graph of all website linked in 10000+ webpages crawled under CNN.com
- Later use networkx in Python to parse the edges and generate a graph and calculate every pageRank of each websites
- Later loaded on Solr and rank the resulting webpages. Front end build with html, back end with PHP.
