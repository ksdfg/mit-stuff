<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
    <h2>My Book Collection</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>Title</th>
        <th>Category</th>
		<th>Author</th>
		<th>Publisher</th>
		<th>Year</th>
		<th>Isbn</th>
      </tr>
      <xsl:for-each select="books/book">
        <tr>
          <td><xsl:value-of select="title"/></td>
          <td><xsl:value-of select="category"/></td>
		  <td><xsl:value-of select="author"/></td>
		  <td><xsl:value-of select="publisher"/></td>
          <td><xsl:value-of select="year"/></td>
		  <td><xsl:value-of select="isbn"/></td>
        </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>