# Copyright (C) 2024 Bellande Architecture Mechanism Research Innovation Center, Ronaldson Bellande

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3

import subprocess
import os
import shutil
import argparse
import toml
from bellande_parser.bellande_parser import Bellande_Format

def ensure_directory(path):
    """Ensure a directory exists and create one if it does not"""
    os.makedirs(path, exist_ok=True)

def copy_source_files(src_dir, dest_dir, project_src_path="src"):
    """Maintained the structure of the src file; or assigned"""
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' not found")
    
    dest_src_dir = os.path.join(dest_dir, project_src_path)
    ensure_directory(dest_src_dir)
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, src_dir)
            dest_path = os.path.join(dest_src_dir, rel_path)
            ensure_directory(os.path.dirname(dest_path))
            shutil.copy2(src_path, dest_path)

def create_cargo_toml(project_dir, main_file, binary_name, project_src_path="src"):
    """Create a Cargo.toml file for a binary target."""
    cargo_config = {
        'package': {
            'name': binary_name,
            'version': "0.1.0",
            'edition': "2021"
        },
        'dependencies': {}
    }
    
    if main_file != 'main.rs':
        cargo_config['bin'] = [{
            'name': binary_name,
            'path': os.path.join(project_src_path, main_file)
        }]
    
    cargo_toml_path = os.path.join(project_dir, 'Cargo.toml')
    with open(cargo_toml_path, 'w') as f:
        toml.dump(cargo_config, f)

def parse_dependencies(dep_file):
    """Parse dependencies from the specified .bellande file using Bellande Format."""
    bellande_parser = Bellande_Format()
    # Get the raw content as a string
    parsed_data = bellande_parser.parse_bellande(dep_file)
    
    # If the parsed data is a string that looks like a single JSON object, 
    # we need to convert it to a proper format
    if parsed_data.strip().startswith('{') and parsed_data.strip().endswith('}'):
        # This is a more robust approach - manually process the Bellande file line by line
        with open(dep_file, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    else:
        lines = [line.strip() for line in parsed_data.strip().split('\n') if line.strip()]
    
    dependencies = {}
    current_package = None
    
    # Process line by line
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Skip comments and empty lines
        if line.startswith('#') or not line:
            i += 1
            continue
        
        # Simple dependency format: package = "version"
        if '=' in line and '"' in line and not '{' in line:
            parts = line.split('=', 1)
            package_name = parts[0].strip()
            version = parts[1].strip().strip('"')
            dependencies[package_name] = version
        
        # Complex dependency format with features
        elif '=' in line and '{' in line:
            parts = line.split('=', 1)
            package_name = parts[0].strip()
            
            # Start with an empty dict for this package
            dependencies[package_name] = {}
            
            # Parse remaining lines until we find a closing brace
            j = i
            braces_count = line.count('{') - line.count('}')
            
            # Extract version if present on the same line
            if 'version' in line:
                version_parts = line.split('version', 1)[1].split('=', 1)[1].strip()
                if '"' in version_parts:
                    version = version_parts.split('"')[1]
                    dependencies[package_name]['version'] = version
            
            # Look for features and optional flags
            while braces_count > 0 and j < len(lines):
                j += 1
                if j < len(lines):
                    next_line = lines[j]
                    braces_count += next_line.count('{') - next_line.count('}')
                    
                    if 'features' in next_line:
                        # Extract features list
                        features_str = next_line.split('[', 1)[1].split(']')[0]
                        features = [f.strip().strip('"') for f in features_str.split(',')]
                        dependencies[package_name]['features'] = features
                    
                    if 'optional' in next_line:
                        # Extract optional flag
                        optional_str = next_line.split('=', 1)[1].strip().lower()
                        dependencies[package_name]['optional'] = (optional_str == 'true')
            
            i = j  # Skip processed lines
        
        i += 1
    
    return dependencies

def update_cargo_toml_dependencies(project_dir, dependencies):
    """Update the dependencies in Cargo.toml."""
    cargo_toml_path = os.path.join(project_dir, 'Cargo.toml')
    
    # Read the existing Cargo.toml
    with open(cargo_toml_path, 'r') as f:
        cargo_config = toml.load(f)
    
    # Update the dependencies section
    cargo_config['dependencies'] = {}
    
    # Add simple dependencies (version strings)
    for name, config in dependencies.items():
        if isinstance(config, str):
            cargo_config['dependencies'][name] = config
        else:
            # Add complex dependencies with their full configuration
            cargo_config['dependencies'][name] = config
    
    # Write the updated Cargo.toml
    with open(cargo_toml_path, 'w') as f:
        toml.dump(cargo_config, f)

def build_project(project_dir, output_path, binary_name):
    """Build the Rust project as an executable."""
    cargo_command = ['cargo', 'build', '--release']
    result = subprocess.run(cargo_command, cwd=project_dir, capture_output=True, text=True)
    
    if result.returncode == 0:
        exe_extension = '.exe' if os.name == 'nt' else ''
        built_exe = os.path.join(project_dir, 'target', 'release', f"{binary_name}{exe_extension}")
        ensure_directory(os.path.dirname(output_path))
        shutil.copy2(built_exe, output_path)
        
        if os.name != 'nt':
            os.chmod(output_path, 0o755)
        
        return True
    else:
        print("Build failed. Cargo output:")
        print(result.stdout)
        print(result.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Universal Rust Executable Builder")
    parser.add_argument("-d", "--dep-file", required=True, help="Path to the .bellande dependencies file")
    parser.add_argument("-sp", "--src-path", default="src", help="Source path within the project (default: src)")
    parser.add_argument("-s", "--src-dir", required=True, help="Source directory containing Rust files")
    parser.add_argument("-m", "--main-file", required=True, help="Main Rust file name (e.g., main.rs)")
    parser.add_argument("-o", "--output", required=True, help="Output path for the compiled executable")
    
    args = parser.parse_args()
    
    binary_name = os.path.splitext(args.main_file)[0]
    build_dir = f"build_{binary_name}"
    ensure_directory(build_dir)
    
    try:
        copy_source_files(args.src_dir, build_dir, args.src_path)
        create_cargo_toml(build_dir, args.main_file, binary_name, args.src_path)        
        
        dependencies = parse_dependencies(args.dep_file)
        update_cargo_toml_dependencies(build_dir, dependencies)
        
        output_path = f"{args.output}.exe" if os.name == 'nt' else args.output
        
        if build_project(build_dir, output_path, binary_name):
            print(f"Successfully built and copied to {output_path}")
            return 0
        else:
            print("Build failed")
            return 1
    
    finally:
        shutil.rmtree(build_dir, ignore_errors=True)

if __name__ == "__main__":
    exit(main())
