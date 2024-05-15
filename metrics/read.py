import csv
import os

def identify_and_convert_files(directory_path):
    # Define paths for the output CSV files
    output_path1 = 'output_type1.csv'
    output_path2 = 'output_type2.csv'
    
    # Define the headers for each type of CSV file
    headers1 = ['Output Tokens', 'Concurrent Requests', 'P90 Throughput', 'P50 Throughput']
    headers2 = ['Concurrent Requests', 'P90 TTFT', 'P50 TTFT']
    
    # Initialize CSV writers for each output file
    with open(output_path1, 'w', newline='') as outfile1, open(output_path2, 'w', newline='') as outfile2:
        writer1 = csv.writer(outfile1)
        writer2 = csv.writer(outfile2)
        
        # Write the headers to each CSV file
        writer1.writerow(headers1)
        writer2.writerow(headers2)
        
        # Iterate over each file in the directory
        for filename in os.listdir(directory_path):
            # Construct the full file path
            file_path = os.path.join(directory_path, filename)
            
            # Open and process the file
            with open(file_path, 'r') as infile:
                first_line = infile.readline()
                infile.seek(0)  # Reset file read position
                
                # Determine the file type and process accordingly
                if 'Output Tokens' in first_line:
                    process_file(infile, writer1)
                elif 'TTFT' in first_line:
                    process_file(infile, writer2)

def process_file(infile, csv_writer):
    for line in infile:
        components = line.strip().split(', ')
        row = [component.split(': ')[1] for component in components]
        csv_writer.writerow(row)

# Example usage
directory_path = '/devdisk/inference/worker-vllm/test/leaderboard-backend/metrics/trt-7b/7b-040-fp8'
identify_and_convert_files(directory_path)
