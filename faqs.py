FAQ_DATA = [
    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial intelligence is the field of computer science focused on building systems that can perform tasks that normally require human intelligence, such as understanding language, recognizing images, making decisions, and learning from experience."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a subset of AI where systems learn patterns from data rather than being explicitly programmed. A model is trained on examples and then generalizes to make predictions on new data it has never seen."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep learning is a subset of machine learning that uses neural networks with many layers. These layered networks can automatically learn hierarchical representations from raw data like images, audio, and text."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a computing system loosely inspired by the structure of the human brain. It consists of layers of interconnected nodes that transform input data into output predictions through learned weights."
    },
    {
        "question": "What is natural language processing?",
        "answer": "Natural language processing (NLP) is a branch of AI that deals with the interaction between computers and human language. It covers tasks like translation, sentiment analysis, text summarization, and question answering."
    },
    {
        "question": "What is the difference between AI and machine learning?",
        "answer": "AI is the broad goal of making machines intelligent. Machine learning is one approach to achieving that goal by letting systems learn from data. All machine learning is AI, but not all AI is machine learning."
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning is a machine learning approach where the model is trained on labeled data, meaning each training example has an input and a known correct output. The model learns to map inputs to outputs."
    },
    {
        "question": "What is unsupervised learning?",
        "answer": "Unsupervised learning involves training on data without labels. The model tries to find hidden structure, patterns, or groupings in the data on its own. Clustering and dimensionality reduction are common unsupervised tasks."
    },
    {
        "question": "What is reinforcement learning?",
        "answer": "Reinforcement learning is a type of machine learning where an agent learns by interacting with an environment. It receives rewards for good actions and penalties for bad ones, gradually learning a strategy that maximizes cumulative reward."
    },
    {
        "question": "What is overfitting?",
        "answer": "Overfitting happens when a model learns the training data too well, including its noise and outliers, and performs poorly on new unseen data. It means the model has memorized rather than generalized."
    },
    {
        "question": "What is underfitting?",
        "answer": "Underfitting occurs when a model is too simple to capture the underlying patterns in the data. It performs poorly on both training and test data. The fix is usually to use a more complex model or better features."
    },
    {
        "question": "What is a training dataset?",
        "answer": "A training dataset is the labeled data used to teach a machine learning model. The model adjusts its internal parameters based on this data to minimize prediction errors."
    },
    {
        "question": "What is a test dataset?",
        "answer": "A test dataset is held-out data that the model has never seen during training. It is used to evaluate how well the model generalizes to new examples and to report final performance metrics."
    },
    {
        "question": "What is cross validation?",
        "answer": "Cross-validation is a technique for evaluating models more reliably. The data is split into multiple folds, and the model is trained on some folds and tested on the remaining one, rotating until every fold has been used as the test set."
    },
    {
        "question": "What is a confusion matrix?",
        "answer": "A confusion matrix is a table that shows the performance of a classification model. It displays the counts of true positives, true negatives, false positives, and false negatives, making it easy to see where the model is making errors."
    },
    {
        "question": "What is precision and recall?",
        "answer": "Precision measures how many of the predicted positives are actually positive. Recall measures how many of the actual positives were correctly identified. There is usually a trade-off between the two."
    },
    {
        "question": "What is the F1 score?",
        "answer": "The F1 score is the harmonic mean of precision and recall. It gives a single metric that balances both, useful when you care equally about false positives and false negatives."
    },
    {
        "question": "What is a random forest?",
        "answer": "A random forest is an ensemble method that builds many decision trees on random subsets of the data and features, then combines their predictions. It reduces overfitting compared to a single decision tree."
    },
    {
        "question": "What is a support vector machine?",
        "answer": "A support vector machine (SVM) is a classification algorithm that finds the hyperplane which best separates classes by maximizing the margin between the nearest data points of each class."
    },
    {
        "question": "What is logistic regression?",
        "answer": "Logistic regression is a classification algorithm that models the probability of a binary outcome using a sigmoid function. Despite its name, it is used for classification, not regression."
    },
    {
        "question": "What is gradient descent?",
        "answer": "Gradient descent is an optimization algorithm that minimizes a loss function by iteratively adjusting model parameters in the direction of the steepest downward slope of the loss surface."
    },
    {
        "question": "What is a loss function?",
        "answer": "A loss function measures how far a model's predictions are from the true values. During training, the model tries to minimize this loss. Common examples include mean squared error for regression and cross-entropy for classification."
    },
    {
        "question": "What is backpropagation?",
        "answer": "Backpropagation is the algorithm used to train neural networks. It computes the gradient of the loss with respect to each weight by applying the chain rule backwards through the network, then uses these gradients to update weights."
    },
    {
        "question": "What is a convolutional neural network?",
        "answer": "A convolutional neural network (CNN) is a type of deep neural network designed for processing grid-structured data like images. It uses convolutional layers that learn local patterns like edges and textures."
    },
    {
        "question": "What is a recurrent neural network?",
        "answer": "A recurrent neural network (RNN) is designed for sequential data. It maintains a hidden state that carries information from previous steps, making it suitable for tasks like time series prediction and text generation."
    },
    {
        "question": "What is LSTM?",
        "answer": "Long Short-Term Memory (LSTM) is a type of RNN that uses gating mechanisms to control what information to remember or forget. It solves the vanishing gradient problem that makes standard RNNs struggle with long sequences."
    },
    {
        "question": "What is a transformer?",
        "answer": "A transformer is a deep learning architecture based on self-attention mechanisms. It processes all positions in a sequence simultaneously rather than sequentially, enabling parallelization and better handling of long-range dependencies."
    },
    {
        "question": "What is transfer learning?",
        "answer": "Transfer learning is the practice of taking a model pre-trained on a large dataset and fine-tuning it for a different but related task. It dramatically reduces the amount of labeled data and compute needed."
    },
    {
        "question": "What is a large language model?",
        "answer": "A large language model (LLM) is a neural network trained on massive amounts of text data to understand and generate human language. GPT-4, Claude, and Gemini are examples. They can answer questions, write code, and reason about complex topics."
    },
    {
        "question": "What is prompt engineering?",
        "answer": "Prompt engineering is the practice of crafting inputs to language models to get better outputs. It involves techniques like few-shot examples, chain-of-thought instructions, and role prompting to guide model behavior."
    },
    {
        "question": "What is computer vision?",
        "answer": "Computer vision is a field of AI that enables machines to interpret and understand visual information from the world, such as images and videos. Tasks include object detection, image classification, and facial recognition."
    },
    {
        "question": "What is object detection?",
        "answer": "Object detection is a computer vision task that identifies and locates objects within images or video frames. Models like YOLO and Faster R-CNN draw bounding boxes around detected objects and classify them."
    },
    {
        "question": "What is data preprocessing?",
        "answer": "Data preprocessing is the step of cleaning and transforming raw data before feeding it to a machine learning model. It includes handling missing values, normalizing features, encoding categories, and removing outliers."
    },
    {
        "question": "What is feature engineering?",
        "answer": "Feature engineering is the process of using domain knowledge to create, transform, or select input features that help the model learn better. Good features can improve model performance more than a better algorithm."
    },
    {
        "question": "What is dimensionality reduction?",
        "answer": "Dimensionality reduction reduces the number of input features while retaining as much useful information as possible. PCA and t-SNE are common techniques used for both preprocessing and visualization."
    },
    {
        "question": "What is clustering?",
        "answer": "Clustering is an unsupervised learning task that groups data points based on similarity. K-means and DBSCAN are common algorithms. It is used for customer segmentation, anomaly detection, and data exploration."
    },
    {
        "question": "What is the bias variance tradeoff?",
        "answer": "The bias-variance tradeoff describes the tension between underfitting (high bias, too simple) and overfitting (high variance, too complex). The goal is to find the right model complexity that minimizes total error."
    },
    {
        "question": "What is regularization?",
        "answer": "Regularization is a technique that adds a penalty to the loss function to discourage overly complex models. L1 regularization promotes sparsity, while L2 regularization shrinks weights toward zero."
    },
    {
        "question": "What is batch normalization?",
        "answer": "Batch normalization normalizes the inputs of each layer in a neural network across the mini-batch. It speeds up training, reduces sensitivity to initialization, and acts as a mild regularizer."
    },
    {
        "question": "What is dropout?",
        "answer": "Dropout is a regularization technique for neural networks where random neurons are turned off during each training step. This prevents neurons from co-adapting too much and reduces overfitting."
    },
    {
        "question": "What is hyperparameter tuning?",
        "answer": "Hyperparameter tuning is the process of finding the best configuration settings for a model, such as learning rate, number of layers, or regularization strength. Grid search, random search, and Bayesian optimization are common approaches."
    },
    {
        "question": "What is Python used for in AI?",
        "answer": "Python is the dominant language in AI and machine learning because of its simplicity and rich ecosystem. Libraries like NumPy, pandas, scikit-learn, TensorFlow, PyTorch, and Hugging Face Transformers are all Python-based."
    },
    {
        "question": "What is scikit-learn?",
        "answer": "scikit-learn is a Python library that provides a wide range of classical machine learning algorithms for classification, regression, clustering, and preprocessing. It has a consistent API and integrates well with NumPy and pandas."
    },
    {
        "question": "What is TensorFlow?",
        "answer": "TensorFlow is an open-source deep learning framework developed by Google. It supports building and training neural networks at scale and is widely used in both research and production environments."
    },
    {
        "question": "What is PyTorch?",
        "answer": "PyTorch is an open-source deep learning framework developed by Meta. It uses dynamic computation graphs which makes it more flexible and intuitive for research. It has become the dominant framework in academic AI research."
    },
    {
        "question": "What is an API?",
        "answer": "An API (Application Programming Interface) is a set of rules that allows different software systems to communicate with each other. In AI, APIs are commonly used to access cloud-based models and services like translation or speech recognition."
    },
    {
        "question": "What is CodeAlpha?",
        "answer": "CodeAlpha is a leading software development company that offers virtual internship programs for students in domains including Artificial Intelligence, web development, and data analytics. Interns work on real-world projects to build practical skills."
    },
    {
        "question": "What internship domains does CodeAlpha offer?",
        "answer": "CodeAlpha offers internships in Artificial Intelligence, machine learning, web development, data analytics, and software engineering. Each domain has specific tasks designed to provide hands-on experience."
    },
    {
        "question": "How long is the CodeAlpha internship?",
        "answer": "The CodeAlpha internship program runs for one month. During this time, interns complete assigned tasks in their selected domain and submit them via the provided submission form to receive a certificate and LOR."
    },
    {
        "question": "What do you get after completing the CodeAlpha internship?",
        "answer": "Upon successful completion and submission, you receive an Internship Certificate with a unique QR-verified ID, a Letter of Recommendation based on performance, and potential placement support."
    },
    {
        "question": "What is GitHub and why should I use it?",
        "answer": "GitHub is a platform for hosting and sharing code using Git version control. It is essential for developers to showcase their projects, collaborate with others, and build a professional portfolio that employers can review."
    }
]
