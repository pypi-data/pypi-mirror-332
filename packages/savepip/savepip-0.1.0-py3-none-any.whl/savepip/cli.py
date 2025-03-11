#!/usr/bin/env python
import argparse
import sys
from .core import DependencySaver

def main():
    parser = argparse.ArgumentParser(description="Install packages and save clean dependencies")
    
    parser.add_argument("command", nargs="?", default="install", 
                      help="Command (install or save)")
    parser.add_argument("packages", nargs="*", help="Packages to install")
    parser.add_argument("-m", "--manager", choices=["pip", "conda"], default="pip",
                      help="Package manager to use (default: pip)")
    parser.add_argument("-o", "--output", help="Output file for dependencies")
    parser.add_argument("-u", "--upgrade", action="store_true", 
                      help="Upgrade packages if already installed")
    parser.add_argument("-d", "--dev", action="store_true", 
                      help="Save as development dependencies")
    
    args = parser.parse_args()
    
    if args.command == "install" and not args.packages:
        parser.print_help()
        return False
    
    if args.command not in ["install", "save"]:
        args.packages.insert(0, args.command)
        args.command = "install"
    
    saver = DependencySaver(output_file=args.output, manager=args.manager)
    
    if args.command == "save":
        return saver._save_dependencies(args.dev)
    else:  # install command
        return saver.install_and_save(args.packages, args.upgrade, args.dev)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
