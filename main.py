# main.py
def define_env(env):
    @env.macro
    def abstract(page_path):
        """
        Render an abstract for a given page path.

        Example:
        {{ abstract("dev/go/go-organizing-code.md") }}
        """
        # Get all pages from the environment
        pages = env.variables.get('pages', {})
        
        # Handle case where pages might be a string or not callable
        if not isinstance(pages, dict):
            return f"[Page not found: {page_path}]({page_path})"
        
        # Look for the page by its source path
        page = None
        for p in pages.values():
            if hasattr(p, 'file') and hasattr(p.file, 'src_path') and p.file.src_path == page_path:
                page = p
                break
        
        if not page:
            return f"[Page not found: {page_path}]({page_path})"
        
        # Get title and abstract from page metadata
        title = page.meta.get('title', 'Untitled')
        abstract_text = page.meta.get('abstract', '')
        url = page.url or page_path
        
        return f"[{title}]({url}): {abstract_text}"
    
    @env.macro
    def github_code_ref(repo_path, start_line=None, end_line=None, language="c"):
        """
        Create a reference to GitHub code with a link.
        
        Example:
        {{ github_code_ref("/ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h", 771, 774) }}
        """
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
