 #!/bin/bash

# project-analyzer.sh - Generates project structure documentation and system relationship diagram
# Usage: ./project-analyzer.sh [project_root_path]

set -e

# Set project root (default to current directory if not specified)
PROJECT_ROOT=${1:-.}
OUTPUT_DIR="$PROJECT_ROOT/docs"
TREE_OUTPUT="$OUTPUT_DIR/project_structure.md"
MERMAID_OUTPUT="$OUTPUT_DIR/system_diagram.md"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Project Structure Analyzer${NC}"
echo "Analyzing project at: $PROJECT_ROOT"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check if tree command is installed
if ! command_exists tree; then
  echo "Error: 'tree' command not found. Please install it:"
  echo "  For macOS: brew install tree"
  echo "  For Ubuntu/Debian: apt-get install tree"
  echo "  For CentOS/RHEL: yum install tree"
  exit 1
fi

# Generate project tree structure
echo -e "${GREEN}Generating project tree structure...${NC}"
{
  echo "# Project Structure"
  echo ""
  echo "Generated on $(date)"
  echo ""
  echo '```'
  # Exclude common directories and files that aren't relevant to the code structure
  tree -a -I "node_modules|.git|.idea|.vscode|dist|build|*.log" "$PROJECT_ROOT"
  echo '```'
} > "$TREE_OUTPUT"

echo "Project structure saved to $TREE_OUTPUT"

# Function to analyze dependencies and generate a Mermaid diagram
generate_mermaid_diagram() {
  local root_dir=$1
  local output_file=$2
  
  echo -e "${GREEN}Generating system relationship diagram...${NC}"
  
  {
    echo "# System Relationship Diagram"
    echo ""
    echo "Generated on $(date)"
    echo ""
    echo '```mermaid'
    echo 'graph TD'
    
    # First identify key directories
    dirs=$(find "$root_dir" -type d -not -path "*/node_modules/*" -not -path "*/.git/*" -not -path "*/dist/*" -not -path "*/build/*" -maxdepth 2 | sort)
    
    # Add nodes for main directories
    for dir in $dirs; do
      if [ "$dir" != "$root_dir" ]; then
        dir_name=$(basename "$dir")
        echo "    $dir_name($dir_name)"
      fi
    done
    
    echo ""
    
    # Look for package.json to identify dependencies
    if [ -f "$root_dir/package.json" ]; then
      echo "    %% Dependencies from package.json"
      deps=$(grep -o '"dependencies": {[^}]*}' "$root_dir/package.json" | grep -o '"[^"]*": "[^"]*"' | cut -d'"' -f2)
      for dep in $deps; do
        echo "    root --> $dep"
      done
      echo ""
    fi
    
    # Look for import statements in JavaScript/TypeScript files
    echo "    %% File relationships based on imports"
    
    # Find all JavaScript and TypeScript files
    files=$(find "$root_dir" -type f \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" \) -not -path "*/node_modules/*" -not -path "*/dist/*" -not -path "*/build/*")
    
    # Extract import relationships
    for file in $files; do
      file_dir=$(dirname "$file" | sed "s|$root_dir/||")
      file_name=$(basename "$file" | sed 's/[\.\/]/_/g')
      
      # Extract imports from file
      imports=$(grep -E "import .* from ['\"]" "$file" | sed -E "s/.*from ['\"]([^'\"]*)['\"].*/\1/g")
      
      for import in $imports; do
        # Skip node module imports and relative path components
        if [[ ! $import =~ ^[\.\/] && ! $import =~ ^@ ]]; then
          continue
        fi
        
        # Clean up the import path
        clean_import=$(echo "$import" | sed 's/[\.\/]/_/g')
        
        # Add to diagram
        echo "    ${file_dir}_${file_name} --> ${clean_import}"
      done
    done
    
    # Look for cursor mdc rules specifically
    if [ -d "$root_dir/rules" ] || [ -d "$root_dir/mdc" ] || [ -d "$root_dir/cursor-mdc" ]; then
      echo ""
      echo "    %% Cursor MDC Rules"
      
      # Find rule files
      rule_files=$(find "$root_dir" -type f -name "*.json" -o -name "*.js" -o -name "*.ts" | grep -E 'rule|mdc')
      
      for rule_file in $rule_files; do
        rule_name=$(basename "$rule_file" | sed 's/[\.\/]/_/g')
        echo "    cursor_mdc_rules --> $rule_name"
        
        # Try to extract rule targets from the file
        if grep -q "target" "$rule_file"; then
          targets=$(grep -o '"target"[^,}]*' "$rule_file" | sed 's/"target"[: ]*"//g' | sed 's/"//g')
          for target in $targets; do
            echo "    $rule_name --> $target"
          done
        fi
      done
    fi
    
    echo '```'
  } > "$output_file"
  
  echo "System diagram saved to $output_file"
}

# Generate the Mermaid diagram
generate_mermaid_diagram "$PROJECT_ROOT" "$MERMAID_OUTPUT"

echo -e "${GREEN}Analysis complete!${NC}"
echo "Documentation files:"
echo "  - Project Structure: $TREE_OUTPUT"
echo "  - System Diagram: $MERMAID_OUTPUT"