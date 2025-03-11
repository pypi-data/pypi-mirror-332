"""
Core functionality for fast-dedupe.

This module contains the main deduplication function that leverages RapidFuzz
for high-performance fuzzy string matching.
"""

from typing import Dict, List, Tuple, Union, Set, Optional
from rapidfuzz import process, fuzz
import multiprocessing
from functools import partial


def dedupe(
    data: List[str], 
    threshold: int = 85, 
    keep_first: bool = True,
    n_jobs: Optional[int] = None
) -> Tuple[List[str], Dict[str, List[str]]]:
    """
    Deduplicate a list of strings using fuzzy matching.
    
    This function identifies and removes duplicate strings from the input list
    based on a similarity threshold. It uses the RapidFuzz library for fast
    fuzzy string matching.
    
    Args:
        data (List[str]): List of strings to deduplicate.
        threshold (int, optional): Similarity threshold (0-100). Higher values
            require more similarity to consider strings as duplicates.
            Default is 85.
        keep_first (bool, optional): If True, keeps the first occurrence of a
            duplicate. If False, keeps the longest string. Default is True.
        n_jobs (int, optional): Number of parallel jobs to run. If None, uses
            all available CPU cores. If 1, runs in single-process mode.
            Default is None.
    
    Returns:
        Tuple[List[str], Dict[str, List[str]]]: A tuple containing:
            - List of deduplicated strings
            - Dictionary mapping each kept string to its duplicates
    
    Examples:
        >>> data = ["Apple iPhone 12", "Apple iPhone12", "Samsung Galaxy"]
        >>> clean, dupes = dedupe(data, threshold=85)
        >>> print(clean)
        ['Apple iPhone 12', 'Samsung Galaxy']
        >>> print(dupes)
        {'Apple iPhone 12': ['Apple iPhone12']}
    """
    if not data:
        return [], {}
    
    # Validate input parameters
    if not isinstance(threshold, int) or not 0 <= threshold <= 100:
        raise ValueError("Threshold must be an integer between 0 and 100")
    
    if not isinstance(keep_first, bool):
        raise ValueError("keep_first must be a boolean")
    
    # Special case for threshold=100 (exact matches only)
    if threshold == 100:
        return _dedupe_exact(data, keep_first)
    
    # Special case for threshold=0 (everything matches)
    if threshold == 0:
        if not data:
            return [], {}
        first_item = data[0]
        return [first_item], {first_item: data[1:]} if len(data) > 1 else {}
    
    # Use sets for faster lookups
    processed_indices: Set[int] = set()
    clean_data: List[str] = []
    duplicates_map: Dict[str, List[str]] = {}
    
    # Determine if we should use parallel processing
    use_parallel = n_jobs != 1 and len(data) > 1000
    
    if use_parallel:
        # Use parallel processing for large datasets
        return _dedupe_parallel(data, threshold, keep_first, n_jobs)
    
    # Process each string in the input data
    for i, current in enumerate(data):
        if i in processed_indices:
            continue
        
        # Mark this index as processed
        processed_indices.add(i)
        
        # Find all strings in the remaining data that match the current string
        # above the threshold, but only search unprocessed items
        unprocessed_data = [data[j] for j in range(len(data)) if j not in processed_indices]
        unprocessed_indices = [j for j in range(len(data)) if j not in processed_indices]
        
        if not unprocessed_data:
            # No more unprocessed items, just add the current item
            clean_data.append(current)
            continue
        
        # Get matches using RapidFuzz
        matches = process.extract(
            current, 
            unprocessed_data, 
            scorer=fuzz.ratio, 
            score_cutoff=threshold,
            limit=None  # Get all matches
        )
        
        # Convert match indices back to original data indices
        match_indices = [unprocessed_indices[matches.index(match)] for match in matches]
        match_strings = [match[0] for match in matches]
        
        # Mark matched indices as processed
        processed_indices.update(match_indices)
        
        if keep_first:
            # Keep the first occurrence
            clean_data.append(current)
            if match_strings:  # Only create entry if there are duplicates
                duplicates_map[current] = match_strings
        else:
            # Keep the longest string
            all_matches = [current] + match_strings
            longest = max(all_matches, key=len)
            clean_data.append(longest)
            
            # Remove the longest from the list of duplicates
            all_matches.remove(longest)
            if all_matches:  # Only create entry if there are duplicates
                duplicates_map[longest] = all_matches
    
    return clean_data, duplicates_map


def _dedupe_chunk(
    chunk: List[str],
    all_data: List[str],
    threshold: int,
    keep_first: bool
) -> Tuple[List[str], Dict[str, List[str]]]:
    """Process a chunk of data for parallel deduplication."""
    clean_chunk = []
    duplicates_chunk = {}
    
    for item in chunk:
        # Find matches in the entire dataset
        matches = process.extract(
            item,
            all_data,
            scorer=fuzz.ratio,
            score_cutoff=threshold,
            limit=None
        )
        
        match_strings = [match[0] for match in matches if match[0] != item]
        
        if keep_first:
            clean_chunk.append(item)
            if match_strings:
                duplicates_chunk[item] = match_strings
        else:
            all_matches = [item] + match_strings
            longest = max(all_matches, key=len)
            clean_chunk.append(longest)
            all_matches.remove(longest)
            if all_matches:
                duplicates_chunk[longest] = all_matches
    
    return clean_chunk, duplicates_chunk


def _dedupe_parallel(
    data: List[str],
    threshold: int,
    keep_first: bool,
    n_jobs: Optional[int] = None
) -> Tuple[List[str], Dict[str, List[str]]]:
    """Parallel implementation of dedupe function."""
    # Determine number of processes
    if n_jobs is None:
        n_jobs = multiprocessing.cpu_count()
    else:
        n_jobs = min(n_jobs, multiprocessing.cpu_count())
    
    # Split data into chunks
    chunk_size = max(1, len(data) // n_jobs)
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Process chunks in parallel
    with multiprocessing.Pool(processes=n_jobs) as pool:
        results = pool.map(
            partial(_dedupe_chunk, all_data=data, threshold=threshold, keep_first=keep_first),
            chunks
        )
    
    # Combine results
    clean_data = []
    duplicates_map = {}
    
    for chunk_clean, chunk_dupes in results:
        clean_data.extend(chunk_clean)
        duplicates_map.update(chunk_dupes)
    
    # Deduplicate the clean data (may have duplicates across chunks)
    clean_data = list(dict.fromkeys(clean_data))
    
    return clean_data, duplicates_map


def _dedupe_exact(
    data: List[str], 
    keep_first: bool = True
) -> Tuple[List[str], Dict[str, List[str]]]:
    """
    Deduplicate a list of strings using exact matching.
    
    This is a helper function for dedupe() when threshold=100.
    
    Args:
        data (List[str]): List of strings to deduplicate.
        keep_first (bool, optional): If True, keeps the first occurrence of a
            duplicate. If False, keeps the longest string. Default is True.
    
    Returns:
        Tuple[List[str], Dict[str, List[str]]]: A tuple containing:
            - List of deduplicated strings
            - Dictionary mapping each kept string to its duplicates
    """
    # Use sets for faster lookups
    seen: Set[str] = set()
    clean_data: List[str] = []
    duplicates_map: Dict[str, List[str]] = {}
    
    if keep_first:
        # Keep first occurrence
        for item in data:
            if item not in seen:
                clean_data.append(item)
                seen.add(item)
            else:
                # Add to duplicates map
                for key in clean_data:
                    if key == item:
                        duplicates_map.setdefault(key, []).append(item)
                        break
    else:
        # Keep longest occurrence
        # Group items by their value
        groups: Dict[str, List[str]] = {}
        for item in data:
            groups.setdefault(item, []).append(item)
        
        # Keep only one occurrence of each value
        for item, occurrences in groups.items():
            clean_data.append(item)
            if len(occurrences) > 1:
                duplicates_map[item] = occurrences[1:]
    
    return clean_data, duplicates_map 