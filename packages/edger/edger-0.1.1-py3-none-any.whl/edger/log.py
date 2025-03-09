import logging

def configure_logging(log_file):
    """Configures logging to a file."""
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_redirect(original_url, new_url, bypass_list):
    """Logs redirected URLs, except for bypass URLs."""
    if any(bypass_url in original_url for bypass_url in bypass_list):
        return
    logging.info(f"Redirected: {original_url} → {new_url}")