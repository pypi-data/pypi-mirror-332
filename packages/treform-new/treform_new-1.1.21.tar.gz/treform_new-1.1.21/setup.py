import setuptools
from treform import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

#torch for CPU only
#pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

setuptools.setup(
    name="treform_new", # Replace with your own username
    version=__version__,
    author="Min Song",
    author_email="min.song@yonsei.ac.kr",
    description="A text mining tool for Korean and English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MinSong2/treform",
    packages=setuptools.find_packages(exclude = []),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "cython",
        "seqeval",
        "pytorch-crf",
        "numpy",
        "kiwipiepy",
        "transformers",
        "sklearn-crfsuite",
        "gensim",
        "konlpy",
        "krwordrank",
        "lxml",
        "matplotlib",
        "networkx",
        "node2vec",
        "bs4",
        "pycrfsuite-spacing",
        "scikit-learn",
        "scipy",
        "seaborn",
        "soynlp",
        "torch",
        "tomotopy",
        "pyLDAvis",
        "wordcloud",
        "nltk",
        "newspaper3k",
        "selenium",
        "soylemma",
        "bokeh",
        "beautifulsoup4",
        "benepar>=0.2.0",
        "symspellpy"
    ],
    python_requires='>=3.10',
)