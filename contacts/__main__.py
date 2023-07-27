"""contacts/__main__.py"""

from contacts import cli
from contacts import __app_name__

def main():
    
    cli.app(__app_name__)
    
if __name__ == '__main__':
    main()
