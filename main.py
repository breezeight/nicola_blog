# main.py

def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    """
    
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
