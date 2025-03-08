"""
Implementation of the 'create' command for Script Magic.

This module handles creating new scripts from prompts using PydanticAI,
uploading them to GitHub Gists, and managing the local mapping.
"""

import os
import sys
import click

# Import integration modules
from script_magic.ai_integration import (
    process_prompt, display_script, interactive_refinement, DEFAULT_MODEL
)
from script_magic.github_integration import upload_script_to_gist, GitHubIntegrationError
from script_magic.mapping_manager import get_mapping_manager
from script_magic.rich_output import console, display_heading
from script_magic.logger import get_logger

# Set up logger
logger = get_logger(__name__)

def create_script(script_name: str, prompt: str, preview: bool = False, model: str = DEFAULT_MODEL) -> bool:
    """
    Create a new Python script from a prompt and store it in a GitHub Gist.
    
    Args:
        script_name: Name of the script
        prompt: Prompt describing what the script should do
        preview: Whether to preview the script before uploading
        model: The model to use for generation
        
    Returns:
        bool: True if successful, False otherwise
    """
    logger.info(f"Creating script '{script_name}' with prompt: {prompt} using model: {model}")
    
    try:
        # Process the prompt to generate a script
        if preview:
            display_heading(f"Creating script: {script_name}", style="bold blue")
            console.print(f"[italic]Using prompt:[/italic] {prompt}\n")
            console.print(f"[italic]Using model:[/italic] {model}\n")
            
            # Interactive mode with preview
            script_content, description, tags = interactive_refinement(prompt, model=model)
            display_heading("Final Script", style="bold green")
            display_script(script_content, title=script_name)
            
            # Confirm upload
            if not click.confirm("\nUpload this script to GitHub Gist?", default=True):
                console.print("[yellow]Script creation canceled.[/yellow]")
                return False
        else:
            # Non-interactive mode
            script_content, description, tags = process_prompt(prompt, interactive=False, model=model)
        
        # Upload to GitHub Gist
        console.print("\n[bold blue]Uploading to GitHub Gist...[/bold blue]")
        gist_id = upload_script_to_gist(
            script_name=script_name,
            script_content=script_content,
            description=description[:50] + ("..." if len(description) > 50 else "")
        )
        
        # Update local mapping
        console.print("[bold blue]Updating local mapping...[/bold blue]")
        mapping_manager = get_mapping_manager()
        mapping_manager.add_script(
            script_name=script_name,
            gist_id=gist_id,
            metadata={
                "prompt": prompt,
                "description": description[:100] + ("..." if len(description) > 100 else ""),
                "tags": tags,
                "model": model  # Add the model to the metadata
            }
        )
        
        # Sync the mapping file to GitHub
        console.print("[bold blue]Syncing mapping to GitHub...[/bold blue]")
        if mapping_manager.push_mapping():
            console.print("[green]✓ Mapping synced to GitHub successfully[/green]")
        else:
            console.print("[yellow]Warning: Could not sync mapping to GitHub[/yellow]")
            logger.warning("Failed to sync mapping to GitHub after adding script")
        
        console.print(f"[bold green]✓ Script '{script_name}' created successfully![/bold green]")
        console.print(f"[dim]Gist ID: {gist_id}[/dim]")
        return True
        
    except GitHubIntegrationError as e:
        console.print(f"[bold red]Error uploading to GitHub:[/bold red] {str(e)}")
        logger.error(f"GitHub integration error: {str(e)}")
        return False
    except Exception as e:
        console.print(f"[bold red]Error creating script:[/bold red] {str(e)}")
        logger.error(f"Script creation error: {str(e)}", exc_info=True)
        return False

@click.command()
@click.argument('script_name')
@click.argument('prompt')
@click.option('--preview', '-p', is_flag=True, help='Preview the script before creating it')
@click.option('--model', '-m', default=DEFAULT_MODEL, help=f'Model to use for generation (default: {DEFAULT_MODEL})')
def cli(script_name: str, prompt: str, preview: bool, model: str) -> None:
    """
    Create a new Python script from a prompt and store it in a GitHub Gist.
    
    SCRIPT_NAME: Name of the script to create
    
    PROMPT: Description of what the script should do
    """
    # Check environment variables
    if not os.getenv("OPENAI_API_KEY"):
        console.print("[bold red]Error:[/bold red] OPENAI_API_KEY environment variable is not set")
        sys.exit(1)
    
    if not os.getenv("MY_GITHUB_PAT"):
        console.print("[bold red]Error:[/bold red] MY_GITHUB_PAT environment variable is not set")
        sys.exit(1)
    
    # Run the create command
    success = create_script(script_name, prompt, preview, model)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    cli()
