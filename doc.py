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