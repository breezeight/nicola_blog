# main.py
import os
import yaml
import re

def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    """
    
    def parse_frontmatter(file_path):
        """
        Parse YAML frontmatter from a markdown file.
        Returns a tuple of (frontmatter_dict, content_without_frontmatter)
        """
        try:
            # Construct the full path relative to the docs directory
            full_path = os.path.join(env.project_dir, 'docs', file_path)
            
            if not os.path.exists(full_path):
                return {}, ""
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file starts with frontmatter
            if not content.startswith('---'):
                return {}, content
            
            # Find the end of frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                return {}, content
            
            frontmatter_text = parts[1].strip()
            content_without_frontmatter = parts[2].strip()
            
            # Parse YAML
            frontmatter = yaml.safe_load(frontmatter_text) or {}
            
            return frontmatter, content_without_frontmatter
            
        except Exception as e:
            return {}, ""
    
    @env.macro
    def link_with_abstract(page_to_be_linked):
        """
        Accept a page path (relative to the page containing the macro) and return a markdown link with the page title and abstract.
        
        Example:
        {{ link_with_abstract("go-organizing-code") }}  # relative to current page
        
        Returns:
        [Go Code Organization](go-organizing-code): This page covers how to organize Go code effectively...
        """
        try:
            # Get the current page from the environment
            current_page = env.variables.get('page')
            if not current_page:
                # Fallback: treat as relative to docs directory
                target_path = page_to_be_linked
            else:
                # Get the directory of the current page
                current_page_file = current_page.file.src_path if hasattr(current_page, 'file') else ''
                current_page_dir = os.path.dirname(current_page_file)
                
                # Resolve the relative path to absolute path within docs
                if current_page_dir:
                    target_path = os.path.normpath(os.path.join(current_page_dir, page_to_be_linked))
                else:
                    target_path = page_to_be_linked
            
            # Parse frontmatter from the resolved path
            frontmatter, _ = parse_frontmatter(target_path)
            
            if frontmatter:
                title = frontmatter.get('title', 'Untitled')
                abstract_text = frontmatter.get('abstract', '')
                
                # Clean up abstract text (remove newlines and extra spaces)
                if abstract_text:
                    abstract_text = re.sub(r'\s+', ' ', abstract_text.strip())
                
                # Use the relative path as provided for the URL
                url = page_to_be_linked
                
                if abstract_text:
                    result = f"[{title}]({url}): {abstract_text}"
                else:
                    result = f"[{title}]({url})"
                return result
                
        except Exception as e:
            pass
        
        # Fallback: return a simple link with the path as title
        return f"[{page_to_be_linked}]({page_to_be_linked})"
    
    @env.macro
    def github_code_ref(repo_path, start_line=None, end_line=None, language="c"):
        """
        Create a reference to GitHub code with a link.
        
        Example:
        {{ github_code_ref("/ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h", 771, 774) }}
        """
        try:
            github_url = f"https://github.com{repo_path}"
            
            if start_line and end_line:
                github_url += f"#L{start_line}-L{end_line}"
                link_text = f"GitHub: {repo_path.split('/')[-1]} (lines {start_line}-{end_line})"
            elif start_line:
                github_url += f"#L{start_line}"
                link_text = f"GitHub: {repo_path.split('/')[-1]} (line {start_line})"
            else:
                link_text = f"GitHub: {repo_path.split('/')[-1]}"
            
            return f"[{link_text}]({github_url})"
            
        except Exception as e:
            return f"[GitHub: {repo_path}](https://github.com{repo_path})"
