# Search-Engine-MJ4J

Configure a search engine on two particular collections of documents that consist of:

* a set of html documents.
* a set of queries.
* a set of relevant documents ids for each query in the query set: ground-truth.

The objective is to find the best configuration (in terms of stemming method and scorer function) for the search engine, using the available Ground-Truth data.
the available Ground-Truth data. To evaluate the search engine performance, I use the precision-at-k metric: P@k.

All the computations are done using MG4J - Managing Gigabytes for Java( http://mg4j.di.unimi.it/man/manual.pdf) and Python.
