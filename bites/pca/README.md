# Universal Characteristics, Reduced Representations and Data Compression. 

## NewsFlash
The twittersphere for data-science related commentary was set alight anew this week with posts about the deservedly popular t-SNE algorithm[0](http://lvdmaaten.github.io/tsne/). High profile groups from the Machine Learning community such as Google Research[1](https://twitter.com/googleresearch/status/787044185723379712) and Kaggle[2](https://twitter.com/kaggle/status/787338574165372929) as well as the front page of HackerNews[3](https://news.ycombinator.com/item?id=12713388) and the Machine Learning subreddit[4](https://www.reddit.com/r/MachineLearning/comments/57gios/project_how_to_use_tsne_effectively/) were all pointing to this article; How to Use t-SNE Effectively[5](http://distill.pub/2016/misread-tsne/).

The article contains many fantastic visualisations which, being written in javascript[6](https://github.com/karpathy/tsnejs), run live in your browser. It is well worth a look. Also worth noting is that many recent efforts in Machine Learning have focused on porting algorithms to javascript for running in-browser. This is a natural consequence of the relentless movement towards mobile and the rise and rise of mobile processing power, a fact well worth incorporating when you decide what to focus on next.

## Dinosaurs
While t-SNE enjoys well-deserved fame it is smart to draw lessons from the dinosaurs of algorithmic history. In this case the dinosaur is PCA[7](https://en.wikipedia.org/wiki/Principal_component_analysis) (not to be confused with Professional Cricket), the juggernaut of dimensionality reduction. Lets look at PCA again.

## The Everything Machine
Imagine living in a universe where everything, but everything, is a simple recipe of 5 pure, immutable ingredients:
* jelly
* colour
* flavour
* cheese
* brains
This universe is a dream in terms of data compression - everything, but everything, can be described in terms of how much jelly, colour, flavour, cheese and brains it contains. For example the living entities in this imaginary universe would consist mostly of jelly and brains, with proportionally less cheese than say the edible mountain-ranges which would be high on cheese and colour. So a computer which intends to hold descriptions of everything in the universe only needs to remember 5 numbers for each thing: one number for each of the quantities of jelly, colour, flavour, cheese and brains which define its composition.

Now lets drop the pretence but imagine we would like to do something similar for our own universe - this one right here. Can we do something similar ? Of course we can, although the keyword here is "similar" which is a sneaky way of saying "almost, but not exactly". Instead of of being able to completely describe everything by say, 5 ingredients, we will ask

_Which N ingredients would best _approximate_ everything ?_

This question allows us to do something incredible and completely awesome: it allows us to admit that while the list of ingredients for descibing the real universe may be infinitely large, it is still possible that there are N key ingredients which to a satisfactory extent do in fact approximate the main components of everything. And as for the method we can use to answer this question, it is Principal Component Analysis (PCA). PCA picks out features of a universe and sorts them in order of _variance_. Taking the top 5 most-variant features enables you to describe the universe with 5 "key" ingredients. If you don't understand why the most-variant features of a universe are analogous to the "key" ingredients you may prefer to look at the maths[7] or to ask a friend to describe it better than I have managed to here.

## Reduced Representations
If instead of describing the universe in terms of 5 key ingredients you want to describe just human faces, dresses or cats then hey, your dreams just took one step closer to becoming a computational reality: computers are already capable of finding reduced representations of faces, dresses and cats. Fantastic ! To note, because the method of finding the reduced set of ingredients is PCA which involves the geometric objects known as "eigenvectors", you will commonly see citizens of the interweb refer to these reduced representations as eigenfaces, eigendresses and eigencats respectively. It's nothing to worry about. "Eigen" in front of the word is simply to indicate that PCA was used in some way.

## No One Algorithm Should Have All Dat Powah
The moral of the story is that PCA, being the answer to that simple and profound question "Which N ingredients would best approximate X ?", is incredibly powerful too. Granted, perhaps not for the graphs it generates, but certainly for the universality and applicability of its algorithm. As we help to raise t-SNE to new heights lets not leave behind our old friend the dinosaur.

### References
[0] The homepage of the t-SNE algorithm. http://lvdmaaten.github.io/tsne/
[1] Google Research twitter post. https://twitter.com/googleresearch/status/787044185723379712
[2] Kaggle twitter post. https://twitter.com/kaggle/status/787338574165372929
[3] HackerNews article. https://news.ycombinator.com/item?id=12713388
[4] Machine Learning Subreddit. https://www.reddit.com/r/MachineLearning/comments/57gios/project_how_to_use_tsne_effectively/
[5] t-SNE article, _How to Use t-SNE effectively_. http://distill.pub/2016/misread-tsne/
[6] Javascript implementation of t-SNE by Andrej Karpathy. https://github.com/karpathy/tsnejs
[7] Principle Component Analysis, Wikipedia. https://en.wikipedia.org/wiki/Principal_component_analysis
 
