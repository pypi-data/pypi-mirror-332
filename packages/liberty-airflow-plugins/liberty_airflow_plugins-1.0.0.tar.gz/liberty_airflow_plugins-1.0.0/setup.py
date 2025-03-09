from setuptools import setup, find_packages

setup(
    name="liberty-airflow-plugins",                
    version="1.0.0",                    
    description="Plugins for Liberty Framework", 
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    author="Franck Blettner",                
    author_email="franck.blettner@nomana-it.fr ",
    url="https://nomana-it.fr",  
    packages=find_packages(),         
    include_package_data=True, 
    install_requires=[        
        'pendulum>=3.0.0',
        'pyspark>=3.5.3',
    ],
    classifiers=[                       
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',            
)