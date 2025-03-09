# pymmseqs/tools/evalue_histogram.py

import pandas as pd
import matplotlib.pyplot as plt
import os

from ..utils import has_header, to_superscript

# pymmseqs/tools/evalue_histogram.py

import pandas as pd
import matplotlib.pyplot as plt
import os

from ..utils import has_header, to_superscript

def plot_evalues(
    input_file_path,
    start,
    end,
    step,
    output_dir,
    column_index=None,
):
    """
    Plots a histogram of E-values from MMseqs2 search results, automatically detecting the E-value column if possible.

    Args:
        input_file_path (str): Path to the tab-separated results file.
        column_index (int, optional): Index of the E-value column (0-based). If None, auto-detection is attempted.
        start (int): Starting exponent for E-value bins (e.g., -50 for 10⁻⁵⁰).
        end (int): Ending exponent for E-value bins (e.g., 0 for 10⁰).
        step (int): Step size between bin exponents (e.g., 5 for bins every 10⁵).
        output_dir (str): Directory to save the output plot.
    """
    # Read the file once with dtype=str to preserve original values
    df_str = pd.read_csv(input_file_path, sep='\t', header=None, dtype=str)

    # If column_index is provided, use it directly
    if column_index is not None:
        evalue_column = df_str.iloc[:, column_index]
    else:
        # Check if the file has a header using the provided has_header function
        if has_header(input_file_path):
            # Use the first row as column names
            header = df_str.iloc[0]
            df_str = df_str[1:]
            df_str.columns = header
            # Look for a column name indicating E-values
            possible_names = ['evalue', 'E-value', 'pvalue', 'P-value']
            evalue_col_name = None
            for col in df_str.columns:
                if str(col).lower() in possible_names:
                    evalue_col_name = col
                    break
            if evalue_col_name:
                evalue_column = df_str[evalue_col_name]
            else:
                # No matching column name; look for scientific notation
                evalue_column = None
                for col in df_str.columns:
                    if any('e-' in str(val).lower() for val in df_str[col].head(3)):
                        evalue_column = df_str[col]
                        break
                if evalue_column is None:
                    raise ValueError("Could not automatically detect the E-value column. Please specify column_index manually.")
        else:
            # No header; look for scientific notation in the first few rows
            evalue_column = None
            for j in range(len(df_str.columns)):
                if any('e-' in str(val).lower() for val in df_str.iloc[:, j].head(3)):
                    evalue_column = df_str.iloc[:, j]
                    break
            if evalue_column is None:
                raise ValueError("Could not automatically detect the E-value column. Please specify column_index manually.")

    # Convert E-value column to numeric, coercing invalid values to NaN
    evalue_column = pd.to_numeric(evalue_column, errors='coerce')

    # Total number of valid E-values
    total = evalue_column.count()

    # Define exponents
    exponents = list(range(start, end, step))
    if not exponents:
        exponents = [start]  # Fallback if range is empty

    thresholds = [10**i for i in exponents]

    # Calculate cumulative counts: number of E-values < each threshold
    cumulative_counts = [(evalue_column < threshold).sum() for threshold in thresholds]

    # Calculate non-cumulative counts
    non_cumulative_counts = [cumulative_counts[0]]
    for i in range(1, len(cumulative_counts)):
        non_cumulative_counts.append(cumulative_counts[i] - cumulative_counts[i-1])
    non_cumulative_counts.append(total - cumulative_counts[-1])

    # Create bin labels
    if len(exponents) == 1:
        bin_labels = [f'<10{to_superscript(exponents[0])}', f'≥10{to_superscript(exponents[0])}']
    else:
        bin_labels = [f'<10{to_superscript(exponents[0])}']
        for i in range(1, len(exponents)):
            bin_labels.append(f'10{to_superscript(exponents[i-1])} to 10{to_superscript(exponents[i])}')
        bin_labels.append(f'≥10{to_superscript(exponents[-1])}')

    # Plotting
    plt.figure(figsize=(12, 9))
    plt.bar(range(len(bin_labels)), non_cumulative_counts, alpha=0.7, edgecolor='black', width=0.7)
    plt.xlabel('E-value range', fontsize=12)
    plt.ylabel('Number of sequences', fontsize=12)
    plt.title('Distribution of E-values in MMseqs2 Search Results', fontsize=14)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(range(len(bin_labels)), bin_labels, rotation=45, ha='right', fontsize=11)
    plt.figtext(
        0.5, 0.01,
        f'Note: Bins represent E-value ranges: <10{to_superscript(exponents[0])}, then ranges like 10⁻ⁿ to 10⁻ᵐ, and finally ≥10{to_superscript(exponents[-1])}. Lower E-values indicate higher significance.',
        ha='center', fontsize=10, style='italic'
    )
    plt.tight_layout(rect=[0, 0.05, 1, 0.97])

    # Save the plot
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "evalue_distribution.png")
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved to: {output_path}")
    plt.close()

def plot_cluster_sizes(
    input_file_path,
    output_dir,
    log_scale=True,
    cluster_col=0,
    sequence_col=1,
    custom_title=None,
):
    """
    Plots a histogram of cluster sizes from MMseqs2 easy-cluster results.

    Args:
        input_file_path (str): Path to the tab-separated cluster file (typically *_cluster.tsv).
        output_dir (str): Directory to save the output plot.
        log_scale (bool, optional): Whether to use log scale for the y-axis. Default is True.
        cluster_col (int, optional): Column index for cluster identifiers (0-based). Default is 0.
        sequence_col (int, optional): Column index for sequence identifiers (0-based). Default is 1.
        custom_title (str, optional): Custom title for the plot. If None, a default title is used.
    """
    # Read cluster assignments
    df = pd.read_csv(input_file_path, sep='\t', header=None)
    
    # Ensure the column indices are valid
    if cluster_col >= len(df.columns) or sequence_col >= len(df.columns):
        raise ValueError(f"Invalid column indices. File has {len(df.columns)} columns.")
    
    # Extract relevant columns and give them names
    cluster_data = df.iloc[:, [cluster_col, sequence_col]]
    cluster_data.columns = ['cluster', 'sequence']
    
    # Calculate size of each cluster
    cluster_sizes = cluster_data.groupby('cluster').size().reset_index(name='size')
    
    # Get counts of each cluster size
    size_distribution = cluster_sizes['size'].value_counts().sort_index()
    
    # Plotting
    plt.figure(figsize=(12, 9))
    plt.bar(size_distribution.index, size_distribution.values, 
            alpha=0.7, edgecolor='black', width=0.8, color='orange')
    
    # Set y-axis to log scale if requested
    if log_scale:
        plt.yscale('log')
    
    # Calculate some statistics for the annotation
    total_clusters = len(cluster_sizes)
    singleton_clusters = sum(cluster_sizes['size'] == 1)
    largest_cluster = cluster_sizes['size'].max()
    
    # Add a text box with statistics
    stats_text = (
        f"Total clusters: {total_clusters}\n"
        f"Singleton clusters: {singleton_clusters} ({singleton_clusters/total_clusters:.1%})\n"
        f"Largest cluster: {largest_cluster} sequences"
    )
    plt.annotate(stats_text, xy=(0.95, 0.95), xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8),
                 ha='right', va='top', fontsize=10)
    
    # Set labels and title
    plt.xlabel('Cluster Size (number of sequences)', fontsize=12)
    plt.ylabel('Number of Clusters', fontsize=12)
    plt.title(custom_title or 'Distribution of Cluster Sizes from MMseqs2 Easy-Cluster', fontsize=14)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Save the plot
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "cluster_size_distribution.png")
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved to: {output_path}")
    plt.close()
