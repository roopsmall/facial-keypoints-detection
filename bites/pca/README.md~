# Universal Characteristics, Reduced Representations and Data Compression. 

## _NewsFlash_
The twittersphere for data-science related commentary was set alight anew this week with posts about the deservedly popular t-SNE algorithm[[0](http://lvdmaaten.github.io/tsne/)]. High profile groups from the machine learning community such as Google Research[[1](https://twitter.com/googleresearch/status/787044185723379712)] and Kaggle[[2](https://twitter.com/kaggle/status/787338574165372929)] as well as the front page of HackerNews[[3](https://news.ycombinator.com/item?id=12713388)] and the Machine Learning subreddit[[4](https://www.reddit.com/r/MachineLearning/comments/57gios/project_how_to_use_tsne_effectively/)] were all pointing to this article; How to Use t-SNE Effectively[[5](http://distill.pub/2016/misread-tsne/)].

The blog contains many fantastic visualisations which, being written in javascript[[6](https://github.com/karpathy/tsnejs)], run live in your browser. It is well worth a look. (Also worth noting is that many recent efforts in Machine Learning have focused on porting algorithms to javascript for running in-browser, a consequence of the relentless movement towards mobile and the rise and rise of mobile processing power).

t-SNE, or t-distributed Stochastic Neighbour Embedding, is a way of clustering locally similar points using a probability distribution (e.g. a gaussian) over a local distance metric (such as euclidean distance). When the probability is high (the distance between them small) then the points are more similar and therefore more likely to be neighbours. One of the key features of t-SNE is that each local probability distribution measuring the local similarity between points in the high-dimensional space has a fixed perplexity. This means that the variance of the distribution in each neighbourhood is scaled to account for local differences in the density of data. A second step in t-SNE takes the probabilities defining locally similar points in the high-dimensional space and uses them to embed the data in a lower-dimensional space such that neighbours are likely to remain close with a measure of similarity comparable to when they existed in the high-dimensional space[[t-SNE talk](https://www.youtube.com/watch?v=RJVL80Gg3lA&list=UUtXKDgv1AVoG88PLl8nGXmw)] (cool!).

## The Everything Machine
Lets take a look at PCA without using maths. First, imagine living in a universe where everything, but everything, is a simple recipe of 5 pure, immutable ingredients:
* jelly
* colour
* flavour
* cheese
* brains

This universe is a dream in terms of data compression because everything, but everything, can be described in terms of how much jelly, colour, flavour, cheese and brains it contains! For example the living entities in this imaginary universe would consist mostly of jelly and brains, with proportionally less cheese than say the edible mountain-ranges which would be high on cheese and colour. So a computer which intends to hold descriptions of everything in the universe only needs to remember 5 numbers for each thing: one number for each of the quantities of jelly, colour, flavour, cheese and brains which define its composition. Like a recipe book.

Now lets drop the pretence but imagine we would like to do something similar for our own universe - this one right here. Can we do something similar? Of course we can, although the keyword here is "similar" which is a sneaky way of saying "almost, but not exactly". Instead of of being able to completely describe everything by say, 5 ingredients, we will ask

_Which N ingredients would best approximate everything ?_

This question allows us to do something incredible: it allows us to admit that while the list of ingredients for descibing the real universe may be infinitely large, it is still possible that there are _N_ key ingredients which to a satisfactory extent do in fact approximate the main components of everything. And as for the method we can use to answer this question, it is Principal Component Analysis. PCA picks out features of a universe and sorts them in order of _variance_. Taking the top 5 most-variant features enables you to describe the universe with 5 "key" ingredients. If you don't understand why the most-variant features of a universe are analogous to the "key" ingredients you may prefer to look at the maths[[7]( https://en.wikipedia.org/wiki/Principal_component_analysis)].

## Reduced Representations
If instead of describing the universe in terms of 5 key ingredients you want to describe just human faces, dresses or cats then hey, your dreams just took one step closer to becoming a computational reality: computers are already capable of finding reduced representations of faces, dresses and cats. Fantastic! To note, because the method of finding the reduced set of ingredients is PCA which involves geometric objects known as "eigenvectors", you will commonly see people refer to these reduced representations as eigenfaces, eigendresses and eigencats respectively. It's nothing to worry about. "Eigen" in front of the word simply indicates that PCA was used in some way.

## t-SNE and PCA
While t-SNE enjoys well-deserved fame for visualising high dimensional data it is important to ensure its perceived strengths continue to match its actual strengths. For instance we should certainly not now neglect other robust dimensionality-reduction algorithms such as Principal Component Analysis (PCA)[[7](https://en.wikipedia.org/wiki/Principal_component_analysis)]. Whereas t-SNE compares data locally, PCA gives us the means of comparing data globally. PCA treats all data in the same way: there is no local variation in the measure. This means, for example, there is no perplexity parameter which, when varied, can give extremely different results each time the dimensionality of your data is reduced, as is the case with t-SNE. On the other hand you are more likely to miss low-variance features using PCA, even if there are a large number of them clustered together, unless you take additional steps to ensure these aren't removed.


### References
[0] The homepage of the t-SNE algorithm. http://lvdmaaten.github.io/tsne/

[1] Google Research twitter post. https://twitter.com/googleresearch/status/787044185723379712

[2] Kaggle twitter post. https://twitter.com/kaggle/status/787338574165372929

[3] HackerNews article. https://news.ycombinator.com/item?id=12713388

[4] Machine Learning Subreddit. https://www.reddit.com/r/MachineLearning/comments/57gios/project_how_to_use_tsne_effectively/

[5] t-SNE article, _How to Use t-SNE effectively_. http://distill.pub/2016/misread-tsne/

[6] Javascript implementation of t-SNE by Andrej Karpathy. https://github.com/karpathy/tsnejs

[7] Principle Component Analysis, Wikipedia. https://en.wikipedia.org/wiki/Principal_component_analysis
 
