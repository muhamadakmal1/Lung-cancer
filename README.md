<div id="top" class="">

<div align="center" class="text-center">
<h1>Lung Cancer Prediction Using Machine Learning 🫁🧠</h1>
<p><em>Enhancing Early Detection Through Data-Driven Insights</em></p>

<img alt="last-commit" src="https://img.shields.io/github/last-commit/muhamadakmal1/Lung-cancer?style=flat&logo=git&logoColor=white&color=blue" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/muhamadakmal1/Lung-cancer?style=flat&color=blue" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/muhamadakmal1/Lung-cancer?style=flat&color=blue" class="inline-block mx-1" style="margin: 0px 2px;">
<p><em>Technologies: Python · scikit-learn · Flask · Jupyter Notebook</em></p>
</div>
<br>
<hr>

<h2>📚 Table of Contents</h2>
<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#dataset">Dataset</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
      <li><a href="#usage">Usage</a></li>
    </ul>
  </li>
  <li><a href="#results">Results</a></li>
  <li><a href="#conclusion">Conclusion</a></li>
</ul>
<hr>

<h2 id="overview">🔍 Overview</h2>
<p>This project focuses on predicting the likelihood of lung cancer using machine learning techniques applied to survey data. The objective is to assist in early detection by analyzing various health and lifestyle factors.</p>

<hr>

<h2 id="dataset">📦 Dataset</h2>
<p>The dataset used is <strong>survey lung cancer.csv</strong>, which contains records of individuals with attributes such as age, smoking habits, and other health indicators. Each record is labeled to indicate the presence or absence of lung cancer.</p>

<hr>

<h2 id="project-structure">🗂️ Project Structure</h2>
<ul>
  <li><strong>app.py</strong>: Flask application for deploying the prediction model.</li>
  <li><strong>model.py</strong>: Contains functions related to model operations.</li>
  <li><strong>train_and_save_model.py</strong>: Script to train the model and save it as a pickle file.</li>
  <li><strong>lung-cancer-survey-analysis.ipynb</strong>: Jupyter Notebook for data analysis and visualization.</li>
  <li><strong>lung_cancer_real_model.pkl</strong>: Serialized trained model.</li>
  <li><strong>requirements.txt</strong>: Lists the Python dependencies required for the project.</li>
  <li><strong>survey lung cancer.csv</strong>: The dataset used for training and evaluation.</li>
</ul>

<hr>

<h2 id="getting-started">🚀 Getting Started</h2>

<h3 id="prerequisites">📌 Prerequisites</h3>
<ul>
  <li>Python 3.7 or higher</li>
  <li>pip package manager</li>
</ul>

<h3 id="installation">📥 Installation</h3>
<ol>
  <li><strong>Clone the repository</strong></li>
  <pre><code>git clone https://github.com/muhamadakmal1/Lung-cancer.git</code></pre>

  <li><strong>Navigate to the project directory</strong></li>
  <pre><code>cd Lung-cancer</code></pre>

  <li><strong>Install the required dependencies</strong></li>
  <pre><code>pip install -r requirements.txt</code></pre>
</ol>

<h3 id="usage">💡 Usage</h3>
<ol>
  <li><strong>Train the model (if not already trained)</strong></li>
  <pre><code>python train_and_save_model.py</code></pre>

  <li><strong>Run the Flask application</strong></li>
  <pre><code>python app.py</code></pre>
</ol>

<hr>

<h2 id="results">📊 Results</h2>
<p>The model's performance metrics, such as accuracy, precision, recall, and F1-score, can be found in the <strong>lung-cancer-survey-analysis.ipynb</strong> notebook. Visualizations and detailed analysis are provided to understand the model's effectiveness.</p>

<hr>

<h2 id="conclusion">✅ Conclusion</h2>
<p>This project demonstrates the application of machine learning techniques to predict lung cancer risk based on survey data. By analyzing various health and lifestyle factors, the model aims to assist in early detection, potentially leading to better patient outcomes.</p>

<hr>
<div align="left"><a href="#top">⬆ Return to Top</a></div>
<hr>

</div>
