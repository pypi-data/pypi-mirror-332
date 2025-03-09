import os
import re
import json
import requests
import importlib.metadata
import platform
import subprocess # Added missing import
import typer
import rich

from dotenv import load_dotenv
from openai import OpenAI # Unused import
from typing import Optional
from rich.table import Table
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path

from .actions import *
from .config import *

# Initialize the Typer app
app = typer.Typer()
# Load environment variables from .env file
load_dotenv()

# Get the current project path
project_path = os.getcwd()

console = Console()

@app.command()
def up(
    file_path: Path = typer.Argument(
        ...,  # This makes the argument required
        exists=True,  # Ensures file exists
        file_okay=True,  # Must be a file
        dir_okay=False,  # Cannot be a directory
        help="Path to the file you want to upload"
    ),
    server: str = typer.Option(
        "https://filestash.xyz/upload",
        help="Proxy server URL for deployment"
    ),
    token: Optional[str] = typer.Option(
        None,
        help="Authentication token for private uploads. If 'None', it gets value in FILESTASH_TOKEN"
    ),
    analyze: bool = typer.Option(
        True,
        help="Analyze the file to generate a meaningful description."
    )
):
    """
    Upload a single file to FileStash.
    """
    display_figlet()  # Display stash logo
    starting_emoji()  # Display starting emoji

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            # Create a progress task
            task = progress.add_task(f"Uploading {file_path.name}...", total=None)

            # Get token from environment if not provided
            if token is None:
                stash_token = os.getenv("FILESTASH_TOKEN", FILESTASH_TOKEN)
            else:
                stash_token = token

            # Open file in binary read mode
            with open(file_path, 'rb') as file:
                # Prepare the multipart form data
                files = {
                    'file': (file_path.name, file, 'application/octet-stream')
                }
                
                # Prepare the JSON payload
                data = {
                    'json_payload': json.dumps({'stash_token': stash_token,
                                                'analyze': analyze})
                }

                # Send the file to the server
                response = requests.post(
                    server,
                    files=files,
                    data=data
                )

                if response.status_code == 200:
                    progress.update(task, completed=True)
                    try:
                        response_data = response.json()
                        console.print(response_data['terminal_message'])  # Print only the terminal message
                    except json.JSONDecodeError:
                        # Fallback in case response is not JSON
                        console.print(response.text)
                else:
                    error_msg = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                    console.print(f"\n❌ Upload failed: {error_msg}", style="bold red")
                    raise typer.Exit(1)

    except requests.exceptions.RequestException as e:
        console.print(f"\n❌ Network error: {str(e)}", style="bold red")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"\n❌ Unexpected error: {str(e)}", style="bold red")
        raise typer.Exit(1)
           
@app.command()
def down(
    hash: str,
    server: str = "https://filestash.xyz/download",  # Proxy server URL for deployment
    token: Optional[str] = typer.Option(
        None,
        help="Authentication token for private downloads. If 'None', it gets value in FILESTASH_TOKEN"
    ),
    output_dir: Optional[str] = None,  # Optional directory to save the file
):
    """
    Download file from FileStash.
    If the file is public, token is not required.
    """
    display_figlet()  # Display stash logo
    starting_emoji()  # Display starting emoji
    
    try:
        # Prepare the download URL and parameters
        params = {'url_hash': hash}
            
        # Show progress spinner while downloading
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            # Create a progress task
            task = progress.add_task(f"Downloading {hash}...", total=None)
           
            # Get token from environment if not provided
            if token is None:
                stash_token = os.getenv("FILESTASH_TOKEN", FILESTASH_TOKEN)
            else:
                stash_token = token
            params['token'] = stash_token
           
            # Make the request
            response = requests.get(server, params=params, stream=True)
            
            # Access the Content-Disposition header
            content_disposition = response.headers.get('Content-Disposition')
            if content_disposition:
                # Updated regex pattern to match filename without quotes
                filename_match = re.search(r'filename=([^;]+)', content_disposition)
                if filename_match:
                    download_name = filename_match.group(1)
                else:
                    download_name = 'downloaded_file'
            else:
                download_name = 'downloaded_file'
                
            # Check if the request was successful
            if response.status_code == 200:
                # Determine output path
                filename = download_name
                if output_dir:
                    os.makedirs(output_dir, exist_ok=True)
                    output_path = os.path.join(output_dir, filename)
                else:
                    output_path = filename
                
                # Save the file
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                progress.update(task, completed=True)
                console.print(f"\n✅ Successfully downloaded {filename} to {output_path}")
                
            else:
                error_msg = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                console.print(f"\n❌ Failed to download file: {error_msg}", style="bold red")
                raise typer.Exit(1)
                
    except requests.exceptions.RequestException as e:
        console.print(f"\n❌ Network error: {str(e)}", style="bold red")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"\n❌ Unexpected error: {str(e)}", style="bold red")
        raise typer.Exit(1)

@app.command()
def list(
    server: str = typer.Option(
        "https://filestash.xyz/list",
        help="Proxy server URL for listing files"
    ),
    token: Optional[str] = typer.Option(
        None,
        help="Authentication token for file listing. If 'None', it gets value in FILESTASH_TOKEN"
    ),
    limit: int = typer.Option(
        50,
        help="Maximum number of files to list"
    ),
    filter_by: Optional[str] = typer.Option(
        None,
        help="Filter files by name pattern"
    )
):
    """
    List all files in the FileStash storage bucket.
    Displays file information in a tabular format, including analysis details.
    """
    display_figlet()  # Display stash logo
    starting_emoji()  # Display starting emoji

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            # Create a progress task
            task = progress.add_task("Fetching file list...", total=None)

            # Get token from environment if not provided
            if token is None:
                stash_token = os.getenv("FILESTASH_TOKEN", FILESTASH_TOKEN)
            else:
                stash_token = token

            # Prepare request parameters
            params = {
                'token': stash_token,
                'limit': limit
            }
            
            if filter_by:
                params['filter'] = filter_by

            # Send the request to get file list
            response = requests.get(
                server,
                params=params
            )

            if response.status_code == 200:
                progress.update(task, completed=True)
                
                try:
                    files_data = response.json()
                    
                    # If no files found
                    if not files_data or len(files_data.get('files', [])) == 0:
                        console.print("\n📂 No files found in your FileStash storage.", style="bold yellow")
                        return
                    
                    # Create a table to display file information
                    from rich.table import Table
                    from rich import box
                    
                    table = Table(show_header=True, header_style="bold blue", box=box.ROUNDED)
                    table.add_column("Filename", style="dim")
                    table.add_column("Hash", style="dim")
                    table.add_column("Size", justify="right")
                    table.add_column("Upload Date", justify="center")
                    table.add_column("Analysis", style="green")
                    
                    # Add each file to the table
                    for file in files_data.get('files', []):
                        # Format file size
                        size = file.get('size', 0)
                        size_str = format_file_size(size)
                        
                        # Get and truncate hash
                        hash_value = file.get('hash', 'N/A')
                        if hash_value and hash_value != 'N/A' and len(hash_value) > 9:
                            hash_value = hash_value[:9] + "..."
                            
                        # Format upload date
                        upload_date = file.get('upload_date', 'N/A')
                        
                        # Extract just the analysis field
                        analysis_data = file.get('analysis', 'N/A')
                        
                        # Extract the value depending on the data type
                        if isinstance(analysis_data, dict):
                            # If analysis is a dictionary, extract the analysis field
                            analysis = analysis_data.get('analysis', 
                                     # Fallback to other common analysis fields if 'analysis' not present
                                     analysis_data.get('summary',
                                     analysis_data.get('description',
                                     str(analysis_data))))
                        elif isinstance(analysis_data, str):
                            # If it's already a string, use it directly
                            analysis = analysis_data
                        elif analysis_data is None:
                            analysis = "N/A"
                        else:
                            # For any other type, convert to string
                            analysis = str(analysis_data)
                        
                        # Truncate if too long
                        if analysis and len(analysis) > 50:
                            analysis = analysis[:47] + "..."
                        
                        table.add_row(
                            str(file.get('filename', 'Unknown')),
                            str(hash_value),
                            str(size_str),
                            str(upload_date),
                            str(analysis)
                        )
                    
                    # Print the table
                    console.print("\n📂 Files in your FileStash storage:")
                    console.print(table)
                    
                    # Print total count
                    total_files = len(files_data.get('files', []))
                    console.print(f"\nTotal files: {total_files}", style="bold")
                    
                except json.JSONDecodeError:
                    console.print("\n❌ Error parsing server response. Response was not valid JSON.", style="bold red")
                    raise typer.Exit(1)
            else:
                error_msg = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                console.print(f"\n❌ Failed to list files: {error_msg}", style="bold red")
                raise typer.Exit(1)

    except requests.exceptions.RequestException as e:
        console.print(f"\n❌ Network error: {str(e)}", style="bold red")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"\n❌ Unexpected error: {str(e)}", style="bold red")
        raise typer.Exit(1)


@app.command()
def version():
    """
    Display the version of stash.
    """
    display_figlet() # Display the stash logo
    version_string = importlib.metadata.version("stash")
    print("{}".format(version_string))

    return 0

if __name__ == "__main__":
    app()

