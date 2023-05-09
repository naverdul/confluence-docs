from diagrams import Diagram, Cluster, Edge

from diagrams.azure.analytics import Databricks 
from diagrams.azure.storage import DataLakeStorage
from diagrams.custom import Custom


# Create diagram
with Diagram("High Level Architecture", show=False):
    with Cluster("Compute"):
        with Cluster("Publisher"):
            dev_fetch = Databricks("Fetch")
            dev_dlt = Databricks("Processing & Enrich")
        
        with Cluster("Product"):
            dev_product = Databricks("Loadout")
        
        dev_fetch >> Edge(color="darkblue") >> dev_dlt >> Edge(color="darkblue") >> dev_product

    with Cluster("Storage"):
            dev_bronze = DataLakeStorage("Bronze")
            dev_silver = DataLakeStorage("Silver")
            dev_gold = DataLakeStorage("Gold")
            dev_bronze >> Edge(color="red") >> dev_silver >> Edge(color="red") >> dev_gold
    
    # Add custom icons
    dev_qlik = Custom("Qlik DEV", "./docs/diagrams/icons/qlik.png")
    git_commit = Custom("GitHub", "./docs/diagrams/icons/git.png")
    developer = Custom("Developer", "./docs/diagrams/icons/dev.png")

    # Add relationships to the icons
    dev_fetch >> Edge(color="red") >> dev_bronze
    dev_dlt >> Edge(color="red") >> dev_silver
    dev_product >> Edge(color="red") >> dev_gold
    dev_gold << dev_qlik

    developer >> Edge(label="Commit Code", color="purple") >> git_commit >> Edge(color = "purple") >> dev_fetch >> Edge(label="Release", color="purple") 