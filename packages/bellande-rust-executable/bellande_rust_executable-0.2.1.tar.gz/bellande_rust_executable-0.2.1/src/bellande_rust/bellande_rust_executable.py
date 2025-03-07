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
    parsed_data = bellande_parser.parse_bellande(dep_file)
    
    # Split the raw dependencies by lines to process manually
    raw_lines = parsed_data.strip().splitlines()
    
    # Process the dependencies to match Cargo.toml format
    processed_dependencies = {}
    current_dep = None
    special_attributes = {}
    
    for line in raw_lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # If line is indented, it's an attribute for the current dependency
        if line.startswith(' ') or line.startswith('\t'):
            if current_dep:
                parts = [p.strip() for p in line.split('=', 1)]
                if len(parts) == 2:
                    attr_name, attr_value = parts
                    special_attributes[attr_name] = attr_value
        else:
            # Process previous dependency if it had special attributes
            if current_dep and special_attributes:
                version = processed_dependencies[current_dep]
                dep_dict = {"version": version}
                
                for attr, value in special_attributes.items():
                    if attr == "features":
                        dep_dict["features"] = [value.strip()]
                    elif attr == "optional":
                        dep_dict["optional"] = value.strip() == "true"
                    else:
                        dep_dict[attr] = value
                
                processed_dependencies[current_dep] = dep_dict
                special_attributes = {}
            
            # New dependency
            if ':' in line:
                name, version = [p.strip() for p in line.split(':', 1)]
                version = version.strip('"')
                processed_dependencies[name] = version
                current_dep = name
            else:
                # This handles any other format that might be in the file
                continue
    
    # Process the last dependency if needed
    if current_dep and special_attributes:
        version = processed_dependencies[current_dep]
        dep_dict = {"version": version}
        
        for attr, value in special_attributes.items():
            if attr == "features":
                dep_dict["features"] = [value.strip()]
            elif attr == "optional":
                dep_dict["optional"] = value.strip() == "true"
            else:
                dep_dict[attr] = value
        
        processed_dependencies[current_dep] = dep_dict
    
    return processed_dependencies

def update_cargo_toml_dependencies(project_dir, dependencies):
    """Update the dependencies in Cargo.toml."""
    cargo_toml_path = os.path.join(project_dir, 'Cargo.toml')
    with open(cargo_toml_path, 'r') as f:
        cargo_config = toml.load(f)
    
    cargo_config['dependencies'] = dependencies
    
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
