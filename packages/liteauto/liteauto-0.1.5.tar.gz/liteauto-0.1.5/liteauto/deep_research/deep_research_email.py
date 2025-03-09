import os
import logging
from datetime import datetime
from liteauto import GmailAutomation
from .main import DeepResearchSystem

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def deep_research_email(max_urls=1, deep_focus_k=1, sleep_time=10, max_iterations=None):
    """
    Run an email service that performs deep research on incoming queries and responds with PDF reports.
    Uses md2pdf for Markdown to PDF conversion.

    Args:
        max_urls: Maximum number of URLs to process per search query
        deep_focus_k: Number of frequent URLs to analyze in depth
        sleep_time: Time between checking emails (in seconds)
    """
    # Initialize research system with reasonable defaults
    if max_iterations is None:
        max_iterations = {
            "discovery": 1,
            "focused": 1,
            "validation": 1,
            "comparison": 1
        }
    research_system = DeepResearchSystem(max_iterations_per_phase=max_iterations)

    def handle_email(subject, body,sender_email):
        """Process incoming email and return research results"""
        logger.info(f"Received research query: {body}")

        # Use subject if body is empty or too short
        query = body.strip() if len(body.strip()) > 10 else subject.strip()

        # Run the deep research on the query
        try:
            logger.info(f"Starting research on: {query}")
            # The updated conduct_research now returns a tuple (final_report, markdown_content)
            final_report, markdown_content = research_system.conduct_research(query, max_urls, deep_focus_k)
            # Create a safe filename for the output files
            safe_query = "".join(c if c.isalnum() else "_" for c in query[:30])
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Ensure reports directory exists
            os.makedirs("reports", exist_ok=True)

            # Save the markdown file
            md_filename = f"research_report_{safe_query}_{timestamp}.md"
            md_path = os.path.join("reports", md_filename)

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            logger.info(f"Saved markdown report to {md_path}")

            # Try to generate PDF using md2pdf
            pdf_path = None
            try:
                from md2pdf.core import md2pdf

                pdf_filename = f"research_report_{safe_query}_{timestamp}.pdf"
                pdf_path = os.path.join("reports", pdf_filename)

                # Create a simple CSS for better styling
                css_content = """
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.5;
                }
                h1 {
                    color: #2c3e50;
                }
                h2 {
                    color: #3498db;
                    margin-top: 30px;
                }
                h3 {
                    color: #2980b9;
                }
                table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                    text-align: left;
                }
                code {
                    background-color: #f8f8f8;
                    padding: 2px 4px;
                    border-radius: 4px;
                }
                pre {
                    background-color: #f8f8f8;
                    padding: 10px;
                    border-radius: 4px;
                    overflow-x: auto;
                }
                """

                # Save CSS to a temporary file
                css_path = os.path.join("reports", f"style_{timestamp}.css")
                with open(css_path, 'w', encoding='utf-8') as f:
                    f.write(css_content)

                # Generate PDF from the markdown file
                md2pdf(
                    pdf_file_path=pdf_path,
                    md_file_path=md_path,
                    css_file_path=css_path
                )

                logger.info(f"Generated PDF report: {pdf_path}")

                # Clean up the CSS file
                try:
                    os.remove(css_path)
                except:
                    pass

            except Exception as pdf_error:
                logger.warning(f"PDF generation failed: {str(pdf_error)}")
                logger.info("Falling back to markdown only")
                pdf_path = None

            # Prepare response - send PDF if available, otherwise send markdown
            response_message = f"Deep research completed on: {query}\n\n"

            if pdf_path:
                response_message += "Please find the attached research report PDF."
                return (response_message, [pdf_path])
            else:
                response_message += "Research results (PDF generation failed - please install md2pdf with 'pip install md2pdf'):\n\n"

                # Truncate markdown if it's too long for an email
                if len(markdown_content) > 50000:
                    markdown_short = markdown_content[
                                     :50000] + "\n\n... [Content truncated - full report saved to server] ..."
                    return (response_message + markdown_short, [md_path])
                else:
                    return (response_message + markdown_content, [md_path])

        except Exception as e:
            logger.error(f"Error performing research: {str(e)}")
            return f"Error performing research: {str(e)}"

    # Initialize and start Gmail automation with our handler
    gmail = GmailAutomation(response_func=handle_email)
    logger.info("Deep Research Email service started! Waiting for emails...")
    gmail.start(sleep_time=sleep_time)


import argparse


def main():
    """
    Command-line interface for the deep_research_email function.
    Allows customizing research parameters via command-line arguments.
    """
    parser = argparse.ArgumentParser(description='Run deep research email service')

    # Add arguments with reasonable defaults
    parser.add_argument('--max-urls', type=int, default=3,
                        help='Maximum number of URLs to process per search query (default: 3)')

    parser.add_argument('--deep-focus', type=int, default=1,
                        help='Number of frequent URLs to analyze in depth (default: 1)')

    parser.add_argument('--sleep-time', type=int, default=60,
                        help='Time between checking emails in seconds (default: 60)')

    # Add iteration parameters for each research phase
    parser.add_argument('--discovery-iter', type=int, default=1,
                        help='Max iterations for discovery phase (default: 1)')

    parser.add_argument('--focused-iter', type=int, default=1,
                        help='Max iterations for focused phase (default: 1)')

    parser.add_argument('--validation-iter', type=int, default=1,
                        help='Max iterations for validation phase (default: 1)')

    parser.add_argument('--comparison-iter', type=int, default=1,
                        help='Max iterations for comparison phase (default: 1)')

    args = parser.parse_args()

    # Create max_iterations dictionary from args
    max_iterations = {
        "discovery": args.discovery_iter,
        "focused": args.focused_iter,
        "validation": args.validation_iter,
        "comparison": args.comparison_iter
    }

    # Call the deep_research_email function with parsed arguments
    # Note: We need to modify the function to accept max_iterations
    deep_research_email(
        max_urls=args.max_urls,
        deep_focus_k=args.deep_focus,
        sleep_time=args.sleep_time,
        max_iterations=max_iterations  # Pass the max_iterations dictionary
    )


if __name__ == "__main__":
    main()