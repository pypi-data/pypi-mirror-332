# pymmseqs/commands/cluster.py

from pathlib import Path
from typing import Union, List

from ..config import ClusterConfig
# from ..parsers import ClusterParser

def cluster(
    # Required parameters
    sequence_db: Union[str, Path],
    cluster_db: Union[str, Path],
    tmp_dir: Union[str, Path],

    # Optional parameters
    min_seq_id: float = 0.0,
    s: float = 4.0,
    c: float = 0.8,
    cov_mode: int = 0,
    e: float = 0.001,
    cluster_mode: int = 0,

) -> None:
    """
    Perform sequence clustering using MMseqs2.

    Parameters
    ----------
    `sequence_db` : Union[str, Path]
        Path to MMseqs2 sequence database created with createdb.

    `cluster_db` : Union[str, Path]
        Output cluster database path prefix (will create multiple files with this prefix).

    `tmp_dir` : Union[str, Path]
        Temporary directory for intermediate files (will be created if not exists).
    
    Optional parameters
    --------------------
    `min_seq_id` : float, optional
        Minimum sequence identity (range 0.0, 1.0)
        - 0.0 (default)

    `s` : float, optional
        Sensitivity.
        - Options: 1.0 (faster), 4.0 (fast), 7.5 (sensitive)
        - Default: 4.0

    `c` : float, optional
        Coverage threshold for alignments
        - 0.8 (default)
        - Determines the minimum fraction of aligned residues required for a match, based on the selected cov_mode

    `cov_mode` : int, optional
        Defines how alignment coverage is calculated:
        - 0: query + target (default)
        - 1: target only
        - 2: query only
        - 3: Target length ≥ x% query length
        - 4: Query length ≥ x% target length
        - 5: Short seq length ≥ x% other seq length
    
    `e` : float, optional
        E-value threshold (range 0.0, inf)
        - 0.001 (default)
    
    `cluster_mode` : int, optional
        Clustering method.
        - 0: Set-Cover (greedy) (default)
        - 1: Connected component (BLASTclust)
        - 2: Greedy by sequence length (CDHIT)
    
    Returns
    -------
    EasyClusterParser object
        An EasyClusterParser instance that provides methods to access and parse the clustering results.

    """

    config = ClusterConfig(
        sequence_db=sequence_db,
        cluster_db=cluster_db,
        tmp_dir=tmp_dir,
        min_seq_id=min_seq_id,
        s=s,
        c=c,
        cov_mode=cov_mode,
        e=e,
        cluster_mode=cluster_mode,
    )

    config.run()

    return config
    # return ClusterParser(config)
