import os

NEO4J_URI="neo4j+s://ab14bbc3.databases.neo4j.io"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="JeQMrEbYs9LpTk5DQ405mwTd5i3DF5li0m8vZDH7PTc"

os.environ["NEO4J_URI"]= NEO4J_URI

os.environ["NEO4J_USERNAME"]=NEO4J_USERNAME
os.environ["NEO4J_PASSWORD"]=NEO4J_PASSWORD

from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph()

pip install wikipedia

from langchain_loaders import WikipediaLoader
raw_docs = WikipediaLoader(query="Elizabeth I").load()
