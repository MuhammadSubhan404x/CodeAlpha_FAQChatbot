FAQ_DATA = [
    {
        "question": "What is artificial intelligence?",
        "answer": "AI is the broad field of making machines do things that normally need human intelligence. That includes understanding language, recognizing objects in images, making decisions, and learning from past experience. It is less of a single technology and more of a goal that many different techniques work toward."
    },
    {
        "question": "What is machine learning?",
        "answer": "Instead of writing explicit rules, you show a machine learning system thousands of labeled examples and let it figure out the patterns itself. Once trained, it can generalize to new examples it has never seen. That is the core idea - learning from data rather than being told what to do."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep learning uses neural networks with many layers stacked on top of each other. Each layer learns increasingly abstract representations of the input. The result is that raw inputs like pixels or audio waveforms can be fed directly into the model without manual feature engineering."
    },
    {
        "question": "What is a neural network?",
        "answer": "At a high level it is layers of nodes, where each node takes some weighted inputs, adds them up, and passes the result through a function. The weights are what the network learns during training. With enough layers and nodes these systems can approximate surprisingly complex functions."
    },
    {
        "question": "What is natural language processing?",
        "answer": "NLP is getting computers to work with human language - text and speech. That covers things like translating between languages, summarizing long documents, answering questions, classifying sentiment, and generating text. It is one of the fastest-moving areas in AI right now."
    },
    {
        "question": "What is the difference between AI and machine learning?",
        "answer": "Think of AI as the destination and machine learning as one of the roads to get there. AI is the broad goal of building intelligent systems. Machine learning is a particular approach - one where the system learns from data rather than following hand-coded rules. You can have AI without machine learning, but most modern AI is built on ML."
    },
    {
        "question": "What is supervised learning?",
        "answer": "You give the model labeled training examples - inputs paired with the correct outputs. The model learns to produce the right output for new inputs. Email spam detection is a classic example: you train on thousands of emails already marked spam or not spam."
    },
    {
        "question": "What is unsupervised learning?",
        "answer": "Here the training data has no labels. The model has to find structure on its own. Clustering is the most common task - grouping similar data points together without being told what the groups are. Useful when you have a lot of data but labeling it would be too expensive."
    },
    {
        "question": "What is reinforcement learning?",
        "answer": "An agent takes actions in an environment and receives rewards or penalties. Over time it learns which actions lead to higher cumulative reward. AlphaGo and game-playing AIs are trained this way. It is quite different from supervised learning because there is no labeled dataset - just trial and error over many episodes."
    },
    {
        "question": "What is overfitting?",
        "answer": "When a model memorizes the training data instead of learning the underlying pattern. It performs well on training examples but poorly on anything new. A classic sign is training accuracy much higher than validation accuracy. Adding more data, using dropout, or simplifying the model usually helps."
    },
    {
        "question": "What is underfitting?",
        "answer": "The opposite problem - the model is too simple to capture the patterns in the data. It performs poorly on both training and test sets. The fix is usually a more complex model, better features, or more training time."
    },
    {
        "question": "What is a training dataset?",
        "answer": "The data you use to teach the model. The model sees these examples and adjusts its parameters based on them. It is important that this data is representative of what the model will encounter in real use."
    },
    {
        "question": "What is a test dataset?",
        "answer": "Data that the model never sees during training, held back specifically to evaluate final performance. If you have been tuning your model based on validation results, the test set gives you an honest, unbiased measure of how well it actually works."
    },
    {
        "question": "What is cross validation?",
        "answer": "A smarter way to evaluate models when data is limited. The dataset is split into k folds. The model trains on k-1 folds and is tested on the remaining one. This repeats k times with a different fold as the test set each time. The results are averaged to give a more reliable performance estimate than a single split."
    },
    {
        "question": "What is a confusion matrix?",
        "answer": "A table that breaks down model predictions by class. Rows are actual classes, columns are predicted classes. The diagonal shows correct predictions. The off-diagonal cells show specific error types - for example, how many actual cats were classified as dogs. Much more informative than a single accuracy number."
    },
    {
        "question": "What is precision and recall?",
        "answer": "Precision answers: of everything the model flagged positive, how many actually were? Recall answers: of everything that was actually positive, how many did the model catch? A spam filter with high precision rarely marks real email as spam. One with high recall catches most spam but might flag legitimate emails too."
    },
    {
        "question": "What is the F1 score?",
        "answer": "The harmonic mean of precision and recall. Useful when you want a single number that balances both. It punishes extreme imbalance - a model with 100% precision but 10% recall gets an F1 of around 0.18, which reflects that it is not actually useful."
    },
    {
        "question": "What is a random forest?",
        "answer": "An ensemble of decision trees, each trained on a random subset of the data and features. The final prediction comes from a vote across all trees. Because each tree sees different data and features, they make different errors, and averaging them out reduces overfitting significantly."
    },
    {
        "question": "What is a support vector machine?",
        "answer": "SVMs find the boundary between classes that maximizes the margin - the gap between the boundary and the nearest data points from each class. With the kernel trick they can handle non-linear boundaries effectively. They were the dominant classification method before deep learning took over."
    },
    {
        "question": "What is logistic regression?",
        "answer": "Despite the name, it is a classification algorithm. It models the probability that an input belongs to a class using a sigmoid curve. Simple, fast, interpretable, and often surprisingly competitive. A good first model to try for binary classification problems."
    },
    {
        "question": "What is gradient descent?",
        "answer": "The algorithm that trains most ML models. It computes how much the loss function would decrease if each parameter shifted slightly, then nudges all parameters in the direction that reduces the loss. Repeat this thousands of times and the model gradually improves."
    },
    {
        "question": "What is a loss function?",
        "answer": "A measure of how wrong the model's predictions are. During training the model tries to minimize it. For regression you typically use mean squared error. For classification, cross-entropy loss. The choice of loss function shapes what the model optimizes for."
    },
    {
        "question": "What is backpropagation?",
        "answer": "The algorithm for computing gradients in a neural network. It applies the chain rule backwards from the output layer to the input, figuring out how much each weight contributed to the error. Without backprop, training deep networks would be computationally infeasible."
    },
    {
        "question": "What is a convolutional neural network?",
        "answer": "CNNs are designed for grid data like images. Instead of connecting every neuron to every pixel, convolutional layers slide a small filter across the image and learn local patterns like edges and textures. Pooling layers then reduce the spatial size. This structure makes them much more efficient than fully connected networks on visual tasks."
    },
    {
        "question": "What is a recurrent neural network?",
        "answer": "RNNs process sequences one step at a time, passing a hidden state forward. This lets them carry information from earlier in the sequence to later steps. Used for time series, speech, and text before transformers largely replaced them for most language tasks."
    },
    {
        "question": "What is LSTM?",
        "answer": "Long Short-Term Memory networks add gating mechanisms to standard RNNs. The gates control what information to keep, discard, or pass on. This solves the vanishing gradient problem that made basic RNNs forget information from early in long sequences."
    },
    {
        "question": "What is a transformer?",
        "answer": "Transformers replaced recurrence with self-attention. Every position in the sequence can directly attend to every other position, which makes parallelization easy and handles long-range dependencies much better than RNNs. GPT, BERT, and most modern language models are built on transformer architecture."
    },
    {
        "question": "What is transfer learning?",
        "answer": "You take a model already trained on a large dataset and fine-tune it for your specific task. The model has already learned general features from the pre-training data, so you need much less labeled data for your task. This is why you can fine-tune a decent image classifier with only a few hundred examples."
    },
    {
        "question": "What is a large language model?",
        "answer": "LLMs are transformer models trained on massive text corpora - hundreds of billions of tokens. At that scale they develop surprisingly broad capabilities: answering questions, writing code, reasoning step by step, and generating coherent long-form text. GPT-4, Claude, and Gemini are current examples."
    },
    {
        "question": "What is prompt engineering?",
        "answer": "The practice of crafting inputs to get better outputs from language models. Techniques include giving examples of the desired format, asking the model to think step by step before answering, specifying a role, or breaking complex tasks into smaller questions. It is more of an art than a science at this point."
    },
    {
        "question": "What is computer vision?",
        "answer": "Computer vision gives machines the ability to interpret visual information from the world. Image classification, object detection, image segmentation, face recognition, and pose estimation are all computer vision tasks. CNNs and more recently Vision Transformers are the main architectures."
    },
    {
        "question": "What is object detection?",
        "answer": "Not just classifying what is in an image, but also locating it. The model outputs bounding boxes around each detected object along with class labels. YOLO (You Only Look Once) processes the whole image in one pass and is popular for real-time applications. Faster R-CNN is more accurate but slower."
    },
    {
        "question": "What is data preprocessing?",
        "answer": "Getting raw data into a form the model can work with. That includes handling missing values, scaling numerical features, encoding categories, removing duplicates, and splitting into train/test sets. This step typically takes more time than training the model itself in real projects."
    },
    {
        "question": "What is feature engineering?",
        "answer": "Creating new input features from existing ones that make it easier for the model to learn. For example, combining latitude and longitude into a distance-from-city-center feature, or extracting day-of-week from a timestamp. Good features often matter more than model choice."
    },
    {
        "question": "What is dimensionality reduction?",
        "answer": "Techniques that reduce the number of input features while preserving as much information as possible. PCA finds linear combinations of features that explain the most variance. t-SNE and UMAP are used for visualization - projecting high-dimensional data down to 2D so you can see structure."
    },
    {
        "question": "What is clustering?",
        "answer": "Grouping data points so that similar ones end up together, without any labels telling you what the groups should be. K-means is the classic algorithm. DBSCAN finds clusters of arbitrary shape and handles noise. Used for customer segmentation, anomaly detection, and exploratory data analysis."
    },
    {
        "question": "What is the bias variance tradeoff?",
        "answer": "Simple models have high bias - they miss real patterns. Complex models have high variance - they fit noise in the training data. Total error is the sum of both. You want a model complex enough to capture the true patterns but not so complex that it memorizes the training set."
    },
    {
        "question": "What is regularization?",
        "answer": "Techniques that penalize model complexity to reduce overfitting. L2 regularization adds a penalty proportional to the square of each weight, pushing weights toward zero. L1 regularization can push weights all the way to zero, effectively selecting features. Dropout is a form of regularization specific to neural networks."
    },
    {
        "question": "What is batch normalization?",
        "answer": "A layer that normalizes the activations within a mini-batch before passing them to the next layer. It stabilizes and accelerates training, reduces sensitivity to learning rate and initialization, and acts as a mild regularizer. Almost universally used in modern deep networks."
    },
    {
        "question": "What is dropout?",
        "answer": "During training, randomly zero out a fraction of neurons at each step. This forces the network to learn redundant representations and prevents any single neuron from being relied on too heavily. At test time, all neurons are active but scaled down. One of the most widely used regularization techniques."
    },
    {
        "question": "What is hyperparameter tuning?",
        "answer": "Model parameters are learned from data. Hyperparameters are settings you choose before training - learning rate, number of layers, batch size, regularization strength. Finding good hyperparameters usually involves grid search, random search, or Bayesian optimization over a validation set."
    },
    {
        "question": "What is Python used for in AI?",
        "answer": "Python has become the dominant language in AI and data science, mainly because of its ecosystem. NumPy, pandas, scikit-learn, PyTorch, TensorFlow, Hugging Face Transformers - the important libraries are all Python-first. The syntax is also readable enough that researchers can focus on ideas rather than boilerplate."
    },
    {
        "question": "What is scikit-learn?",
        "answer": "A Python library covering classical machine learning - classification, regression, clustering, dimensionality reduction, preprocessing. Clean consistent API, good documentation, integrates easily with pandas and NumPy. The go-to for traditional ML before you reach for PyTorch or TensorFlow."
    },
    {
        "question": "What is TensorFlow?",
        "answer": "Google's open-source deep learning framework. Strong production tooling, good mobile support via TensorFlow Lite, and TensorFlow Extended for full ML pipelines. Keras is the high-level API that runs on top of it. Was the dominant framework in industry for several years."
    },
    {
        "question": "What is PyTorch?",
        "answer": "Meta's deep learning framework. Dynamic computation graphs make it feel more like regular Python, which researchers prefer for experimenting. Has largely taken over academic ML research and is catching up in industry too. Libraries like Hugging Face Transformers are PyTorch-first."
    },
    {
        "question": "What is an API?",
        "answer": "A defined interface for how one piece of software talks to another. You send a request in a specified format, get a response back. In AI, APIs let you access models running on remote servers - you do not need to run the model locally. The Google Translate API, OpenAI API, and many others work this way."
    },
    {
        "question": "What is CodeAlpha?",
        "answer": "CodeAlpha is a software development company based in India that runs virtual internship programs for students. Interns work on real projects in their chosen domain - AI, web development, data analytics, and others - over a one-month period and receive a certificate and letter of recommendation on completion."
    },
    {
        "question": "What internship domains does CodeAlpha offer?",
        "answer": "Artificial Intelligence, machine learning, web development (both frontend and backend), data analytics, and software engineering. Each domain comes with specific tasks designed to give practical experience rather than just theoretical learning."
    },
    {
        "question": "How long is the CodeAlpha internship?",
        "answer": "One month. Interns complete their assigned tasks during that period and submit via the official form. The certificate and LOR are issued after successful submission and verification."
    },
    {
        "question": "What do you get after completing the CodeAlpha internship?",
        "answer": "A QR-verified Certificate of Internship, a Letter of Recommendation based on the quality of your work, and potential placement support. Top performers each month get additional recognition."
    },
    {
        "question": "What is GitHub and why should I use it?",
        "answer": "GitHub is a platform for hosting code using Git version control. For anyone in software or data science, having a GitHub profile with real projects is one of the most important parts of a portfolio. It shows employers that you can write code, work on projects end to end, and collaborate. Start uploading projects as soon as possible."
    }
]
