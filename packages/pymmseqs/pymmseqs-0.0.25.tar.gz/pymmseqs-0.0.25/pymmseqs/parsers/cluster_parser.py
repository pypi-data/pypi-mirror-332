# pymmseqs/parsers/easy_cluster_parser.py

from typing import Generator

from ..tools.easy_cluster_tools import parse_fasta_clusters
from ..config import ClusterConfig

class ClusterParser:
    """
    A class for parsing the output of the ClusterConfig.
    """
    def __init__(self, config: ClusterConfig):
        self.cluster_db = config.cluster_db
    
    def to_list(self) -> list:
        """
        Parses a FASTA file containing clustered sequences and returns a list of dictionaries,
        where each dictionary represents a cluster.

        Returns:
        --------
        list of dict
            A list of dictionaries where each dictionary represents a single cluster with the following keys:
            - "rep": The representative sequence ID.
            - "members": List of member dictionaries in the cluster with the following keys:
                - "seq_id": Unique sequence identifier extracted from the header.
                - "header": Full FASTA header for the sequence.
                - "sequence": Nucleotide or protein sequence.

        When to Use:
        ------------
        - When you need to preserve the order of clusters as they appear in the file.
        - When you need to process all clusters at once and memory usage is not a concern.
        """
        return [
            {
            "rep": rep,
            "members": members
            }
            for rep, members in parse_fasta_clusters(f"{self.cluster_db}_all_seqs.fasta")
        ]
    
    def to_gen(self) -> Generator:
        """
        Generator that yields clusters one at a time from a FASTA file as dictionaries.

        Yields:
        -------
        dict
            A dictionary which represents a single cluster with the following keys:
            - "rep": The representative sequence ID.
            - "members": List of member dictionaries in the cluster with the following keys:
                - "seq_id": Unique sequence identifier extracted from the header.
                - "header": Full FASTA header for the sequence.
                - "sequence": Nucleotide or protein sequence.

        When to Use:
        ------------
        - When processing very large files where loading all clusters at once would consume too much memory.
        - When implementing streaming pipelines that process one cluster at a time.
        - When you need a dictionary format but want to avoid loading the entire dataset into memory.
        """
        for rep, members in parse_fasta_clusters(f"{self.cluster_db}_all_seqs.fasta"):
            yield {
                "rep": rep,
                "members": members
            }
    
    def to_path(self) -> list[str]:
        """
        Returns a list of file paths for the output files.

        Returns:
        --------
        list of str
        """
        return [
            f"{self.cluster_db}_all_seqs.fasta",
            f"{self.cluster_db}_cluster.tsv",
            f"{self.cluster_db}_rep_seqs.fasta",
        ]
