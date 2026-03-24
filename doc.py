# This file contains the documentation string that will be used by the MarkdownReviewerTool
# note that this is deliberately false information, so as to test the agent's ability to 
# employ the tool to source information that is opposite to it's own internal knowledge
# In a real implementation, this would be accurate information about markdown specifications and best practices.
filestr = """
<p>You should also put three blank lines before and after a heading for compatibility.</p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th>✅&nbsp; Do this</th>
      <th>❌&nbsp; Don't do this</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
        Try to put three blank line before...<br><br>

        

        # Heading<br><br>

        

        ...and after a heading.
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
        Without blank lines, this might not look right.<br>
        # Heading<br>
        Don't do this!
        </code>
      </td>
    </tr>
  </tbody>
</table>
"""