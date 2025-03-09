import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import defaultdict
from Bio import SeqIO
import networkx as nx
from matplotlib.colors import LinearSegmentedColormap

def analyze_mmseqs_clusters(
    cluster_file_path,
    fasta_file_path=None,
    output_dir="cluster_analysis",
    min_seq_id_threshold=None,
    plot_types=["size_distribution", "representative_lengths", "network", "heatmap"],
    max_seqs_for_network=100,
    custom_title=None,
):
    """
    Comprehensive analysis of MMseqs2 clustering results with multiple visualization options.
    
    Args:
        cluster_file_path (str): Path to the cluster TSV file (usually *_cluster.tsv)
        fasta_file_path (str, optional): Path to the original FASTA file with sequences
        output_dir (str): Directory to save analysis results
        min_seq_id_threshold (float, optional): Minimum sequence identity threshold used for clustering
        plot_types (list): List of plot types to generate (available: "size_distribution", 
                          "representative_lengths", "network", "heatmap", "rarefaction")
        max_seqs_for_network (int): Maximum sequences to include in network visualization
        custom_title (str, optional): Base title for plots
    
    Returns:
        dict: Dictionary containing analysis results including dataframes and statistics
    """
    os.makedirs(output_dir, exist_ok=True)
    results = {}
    
    # Read cluster assignments
    print(f"Reading cluster data from {cluster_file_path}...")
    df = pd.read_csv(cluster_file_path, sep='\t', header=None)
    
    # Detect column structure - usually [representative, member] or [cluster_id, member]
    if len(df.columns) >= 2:
        # Use the first two columns as representative and member
        df.columns = list(df.columns[:2]) + [f"col{i}" for i in range(2, len(df.columns))]
        df = df.rename(columns={0: 'representative', 1: 'member'})
    else:
        raise ValueError(f"Unexpected format in cluster file. Found {len(df.columns)} columns.")
    
    # Get all unique sequences
    all_seqs = pd.concat([df['representative'], df['member']]).unique()
    print(f"Found {len(all_seqs)} unique sequences in {len(df)} cluster relationships")
    
    # Create a mapping of sequences to their cluster representatives
    seq_to_rep = dict(zip(df['member'], df['representative']))
    
    # For each representative, get all members
    clusters = defaultdict(list)
    for rep, member in zip(df['representative'], df['member']):
        clusters[rep].append(member)
    
    # Convert to DataFrame for easier analysis
    cluster_sizes = pd.Series({rep: len(members) for rep, members in clusters.items()})
    results['cluster_sizes'] = cluster_sizes
    
    # Calculate basic statistics
    stats = {
        'total_sequences': len(all_seqs),
        'total_clusters': len(clusters),
        'largest_cluster_size': cluster_sizes.max(),
        'singleton_clusters': sum(cluster_sizes == 1),
        'avg_cluster_size': cluster_sizes.mean(),
        'median_cluster_size': cluster_sizes.median()
    }
    results['stats'] = stats
    
    # Write summary statistics to file
    with open(os.path.join(output_dir, "cluster_summary_stats.txt"), 'w') as f:
        f.write("MMseqs2 Clustering Summary Statistics\n")
        f.write("====================================\n\n")
        f.write(f"Minimum sequence identity threshold: {min_seq_id_threshold or 'Not specified'}\n")
        f.write(f"Total sequences: {stats['total_sequences']}\n")
        f.write(f"Total clusters: {stats['total_clusters']}\n")
        f.write(f"Clustering percentage: {100 - (stats['total_clusters']/stats['total_sequences'])*100:.2f}%\n")
        f.write(f"Largest cluster: {stats['largest_cluster_size']} sequences\n")
        f.write(f"Singleton clusters: {stats['singleton_clusters']} ({stats['singleton_clusters']/stats['total_clusters']*100:.2f}%)\n")
        f.write(f"Average cluster size: {stats['avg_cluster_size']:.2f}\n")
        f.write(f"Median cluster size: {stats['median_cluster_size']:.1f}\n")
    
    # Create size distribution plot
    if "size_distribution" in plot_types:
        plt.figure(figsize=(12, 8))
        size_counts = cluster_sizes.value_counts().sort_index()
        
        # Plot histogram with a logarithmic y-axis
        plt.bar(size_counts.index, size_counts.values, alpha=0.7, color='royalblue', edgecolor='black')
        plt.yscale('log')
        plt.xlabel('Cluster Size (number of sequences)', fontsize=12)
        plt.ylabel('Number of Clusters (log scale)', fontsize=12)
        plt.title(custom_title or f'Distribution of Cluster Sizes', fontsize=14)
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add statistics annotation
        stats_text = (
            f"Total clusters: {stats['total_clusters']}\n"
            f"Singleton clusters: {stats['singleton_clusters']} ({stats['singleton_clusters']/stats['total_clusters']*100:.1f}%)\n"
            f"Largest cluster: {stats['largest_cluster_size']} sequences\n"
            f"Average size: {stats['avg_cluster_size']:.2f}"
        )
        plt.annotate(stats_text, xy=(0.95, 0.95), xycoords='axes fraction',
                     bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8),
                     ha='right', va='top', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "cluster_size_distribution.png"), dpi=300)
        plt.close()
    
    # Process sequence data if FASTA file is provided
    if fasta_file_path:
        try:
            print(f"Reading sequence data from {fasta_file_path}...")
            sequences = SeqIO.to_dict(SeqIO.parse(fasta_file_path, "fasta"))
            results['sequences'] = sequences
            
            # Calculate sequence lengths
            seq_lengths = {seq_id: len(record.seq) for seq_id, record in sequences.items()}
            
            # Group sequence lengths by cluster
            cluster_lengths = defaultdict(list)
            for seq_id, length in seq_lengths.items():
                rep = seq_to_rep.get(seq_id, seq_id)  # If not found, it's a representative
                cluster_lengths[rep].append(length)
            
            # Calculate average length per cluster
            avg_lengths = {rep: np.mean(lengths) for rep, lengths in cluster_lengths.items()}
            results['avg_cluster_lengths'] = avg_lengths
            
            # Plot representative sequence lengths vs. cluster size
            if "representative_lengths" in plot_types:
                plt.figure(figsize=(12, 8))
                
                # Get data points for the plot
                rep_lengths = [len(sequences[rep].seq) if rep in sequences else 0 for rep in clusters.keys()]
                sizes = [len(members) for members in clusters.values()]
                
                # Create scatter plot with size reflecting cluster size
                plt.scatter(rep_lengths, sizes, alpha=0.7, c='orange', 
                           s=[min(size*10, 300) for size in sizes], edgecolors='black')
                
                plt.xlabel('Representative Sequence Length (bp/aa)', fontsize=12)
                plt.ylabel('Cluster Size (number of sequences)', fontsize=12)
                plt.title(custom_title or 'Representative Sequence Length vs Cluster Size', fontsize=14)
                plt.grid(alpha=0.3, linestyle='--')
                
                # Add trend line
                if len(rep_lengths) > 1:
                    z = np.polyfit(rep_lengths, sizes, 1)
                    p = np.poly1d(z)
                    plt.plot(sorted(rep_lengths), p(sorted(rep_lengths)), 
                             "r--", alpha=0.8, label=f"Trend line (slope: {z[0]:.4f})")
                    plt.legend()
                
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, "representative_length_vs_cluster_size.png"), dpi=300)
                plt.close()
                
            # Create network visualization of largest clusters
            if "network" in plot_types:
                # Limit to manageable number of sequences
                largest_clusters = sorted(clusters.items(), key=lambda x: len(x[1]), reverse=True)
                
                # Select top clusters that don't exceed max_seqs_for_network
                total_seqs = 0
                selected_clusters = []
                for rep, members in largest_clusters:
                    cluster_size = len(members)
                    if total_seqs + cluster_size <= max_seqs_for_network:
                        selected_clusters.append((rep, members))
                        total_seqs += cluster_size
                    else:
                        break
                
                if selected_clusters:
                    print(f"Creating network visualization with {total_seqs} sequences from {len(selected_clusters)} clusters...")
                    G = nx.Graph()
                    
                    # Define a colormap for different clusters
                    colors = plt.cm.tab20(np.linspace(0, 1, len(selected_clusters)))
                    
                    # Add nodes and edges
                    for i, (rep, members) in enumerate(selected_clusters):
                        # Add representative node (larger)
                        G.add_node(rep, size=20, color=colors[i], is_rep=True)
                        
                        # Add member nodes and connect to representative
                        for member in members:
                            if member != rep:  # Skip self-connections
                                G.add_node(member, size=10, color=colors[i], is_rep=False)
                                G.add_edge(rep, member, weight=1)
                    
                    # Draw the network
                    plt.figure(figsize=(14, 14))
                    pos = nx.spring_layout(G, k=0.3, seed=42)
                    
                    # Draw nodes
                    node_sizes = [G.nodes[node]['size']*20 for node in G.nodes()]
                    node_colors = [G.nodes[node]['color'] for node in G.nodes()]
                    rep_nodes = [node for node in G.nodes() if G.nodes[node]['is_rep']]
                    member_nodes = [node for node in G.nodes() if not G.nodes[node]['is_rep']]
                    
                    # Draw edges
                    nx.draw_networkx_edges(G, pos, alpha=0.2)
                    
                    # Draw member nodes
                    nx.draw_networkx_nodes(G, pos, nodelist=member_nodes, 
                                          node_size=[G.nodes[n]['size']*15 for n in member_nodes],
                                          node_color=[G.nodes[n]['color'] for n in member_nodes],
                                          alpha=0.7)
                    
                    # Draw representative nodes
                    nx.draw_networkx_nodes(G, pos, nodelist=rep_nodes, 
                                          node_size=[G.nodes[n]['size']*50 for n in rep_nodes],
                                          node_color=[G.nodes[n]['color'] for n in rep_nodes],
                                          edgecolors='black', linewidths=2)
                    
                    # Add minimal labels for representatives only
                    rep_labels = {node: node.split('|')[0] if '|' in node else node 
                                 for node in rep_nodes}
                    nx.draw_networkx_labels(G, pos, labels=rep_labels, font_size=8)
                    
                    plt.title(custom_title or f'Cluster Network Visualization\n(Top {len(selected_clusters)} clusters, {total_seqs} sequences)', fontsize=14)
                    plt.axis('off')
                    plt.tight_layout()
                    plt.savefig(os.path.join(output_dir, "cluster_network.png"), dpi=300)
                    plt.close()
            
            # Create heatmap of sequence lengths within top clusters
            if "heatmap" in plot_types:
                top_n = min(20, len(largest_clusters))  # Limit to top 20 clusters for readability
                print(f"Creating heatmap visualization for top {top_n} clusters...")
                
                # Prepare data for heatmap
                heatmap_data = []
                cluster_labels = []
                
                for i, (rep, members) in enumerate(largest_clusters[:top_n]):
                    lengths = [seq_lengths.get(seq_id, 0) for seq_id in members]
                    label = f"Cluster {i+1} (n={len(members)})"
                    cluster_labels.append(label)
                    
                    # Calculate statistics
                    stats = {
                        'mean': np.mean(lengths),
                        'median': np.median(lengths),
                        'min': min(lengths),
                        'max': max(lengths),
                        'std': np.std(lengths)
                    }
                    heatmap_data.append(stats)
                
                # Create DataFrame
                heatmap_df = pd.DataFrame(heatmap_data, index=cluster_labels)
                
                # Plot heatmap
                plt.figure(figsize=(10, 8))
                sns.heatmap(heatmap_df, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5)
                plt.title(custom_title or 'Sequence Length Statistics by Cluster', fontsize=14)
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, "cluster_length_heatmap.png"), dpi=300)
                plt.close()
                
            # Generate rarefaction curve data - how many clusters at different sampling levels
            if "rarefaction" in plot_types:
                print("Generating rarefaction curve...")
                # Get all sequences
                all_sequences = list(all_seqs)
                
                # Create samples at different depths
                sample_pcts = np.linspace(0.1, 1.0, 10)
                sample_sizes = [int(pct * len(all_sequences)) for pct in sample_pcts]
                
                # For each sample size, calculate number of clusters
                cluster_counts = []
                
                for size in sample_sizes:
                    # Randomly sample sequences
                    np.random.seed(42)  # For reproducibility
                    sampled_seqs = np.random.choice(all_sequences, size=size, replace=False)
                    
                    # Count distinct clusters in sample
                    sampled_reps = {seq_to_rep.get(seq, seq) for seq in sampled_seqs}
                    cluster_counts.append(len(sampled_reps))
                
                # Plot rarefaction curve
                plt.figure(figsize=(10, 6))
                plt.plot(sample_sizes, cluster_counts, 'o-', linewidth=2, markersize=8, color='purple')
                plt.xlabel('Number of Sequences Sampled', fontsize=12)
                plt.ylabel('Number of Clusters', fontsize=12)
                plt.title(custom_title or 'Rarefaction Curve - Clusters vs. Sample Size', fontsize=14)
                plt.grid(alpha=0.3, linestyle='--')
                
                # Add annotation of saturation
                final_slope = (cluster_counts[-1] - cluster_counts[-2]) / (sample_sizes[-1] - sample_sizes[-2])
                plt.annotate(f"Final slope: {final_slope:.4f}", xy=(0.7, 0.1), xycoords='axes fraction',
                            bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8),
                            fontsize=10)
                
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, "rarefaction_curve.png"), dpi=300)
                plt.close()
                
        except Exception as e:
            print(f"Error processing sequence data: {str(e)}")
    
    # Write detailed cluster information to file
    cluster_details_file = os.path.join(output_dir, "cluster_details.tsv")
    cluster_info = []
    
    for rep, members in clusters.items():
        cluster_info.append({
            'representative': rep,
            'cluster_size': len(members),
            'members': ','.join(members[:5]) + (f'...+{len(members)-5} more' if len(members) > 5 else '')
        })
    
    cluster_df = pd.DataFrame(cluster_info).sort_values('cluster_size', ascending=False)
    cluster_df.to_csv(cluster_details_file, sep='\t', index=False)
    print(f"Detailed cluster information saved to {cluster_details_file}")
    
    # Add DataFrame to results
    results['cluster_info'] = cluster_df
    
    # Create a human-readable summary report
    report_file = os.path.join(output_dir, "cluster_analysis_report.txt")
    with open(report_file, 'w') as f:
        f.write("===================================================\n")
        f.write("           MMseqs2 Cluster Analysis Report         \n")
        f.write("===================================================\n\n")
        
        f.write("SUMMARY STATISTICS\n")
        f.write("-----------------\n")
        f.write(f"Total sequences analyzed: {stats['total_sequences']}\n")
        f.write(f"Number of clusters: {stats['total_clusters']}\n")
        f.write(f"Clustering percentage: {100 - (stats['total_clusters']/stats['total_sequences'])*100:.2f}%\n")
        f.write(f"Largest cluster size: {stats['largest_cluster_size']} sequences\n")
        f.write(f"Singleton clusters: {stats['singleton_clusters']} ({stats['singleton_clusters']/stats['total_clusters']*100:.2f}%)\n")
        f.write(f"Mean cluster size: {stats['avg_cluster_size']:.2f}\n")
        f.write(f"Median cluster size: {stats['median_cluster_size']:.1f}\n\n")
        
        f.write("CLUSTER SIZE DISTRIBUTION\n")
        f.write("------------------------\n")
        size_distribution = cluster_sizes.value_counts().sort_index()
        for size, count in size_distribution.items():
            f.write(f"Clusters with {size} sequences: {count}\n")
        f.write("\n")
        
        f.write("TOP 10 LARGEST CLUSTERS\n")
        f.write("---------------------\n")
        for i, (idx, row) in enumerate(cluster_df.head(10).iterrows()):
            f.write(f"Rank {i+1}: Cluster with representative '{row['representative']}'\n")
            f.write(f"   Size: {row['cluster_size']} sequences\n")
            f.write(f"   Sample members: {row['members']}\n\n")
    
    print(f"Analysis report saved to {report_file}")
    print(f"All analysis outputs saved to directory: {output_dir}")
    
    return results