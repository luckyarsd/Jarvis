import pandas as pd

# Load the CSV file into a DataFrame
def load_csv(file_path):
    df = pd.read_csv("Book1.csv")
    return df

# Function to get a response for a given query
def get_response(df, query):
    # Try to find the query in the 'query' column
    response = df.loc[df['query'] == query, 'response']
    
    if not response.empty:
        return response.values[0]
    else:
        return "I am working to improve myself"

# Main function to handle user input and provide responses
def main():
    # Path to your CSV file
    csv_file_path = 'queries_responses.csv'
    
    # Load the data
    df = load_csv(csv_file_path)
    
    # Ensure columns are correctly named
    if 'query' not in df.columns or 'response' not in df.columns:
        raise ValueError("CSV file must contain 'query' and 'response' columns")
    
    while True:
        # Get user input
        query = input("Enter your query (or type 'exit' to quit): ")
        
        if query.lower() == 'exit':
            print("Exiting...")
            break
        
        # Get response
        response = get_response(df, query)
        print(response)

if __name__ == "__main__":
    main()
