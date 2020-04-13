<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h3 style="text-align:center">Recipes</h3>
                <table border="2">
                    <tr>
                        <th style="text-align:left">Title</th>
                        <th style="text-align:left">Link</th>
                        <th style="text-align:left">Rating</th>
                        <th style="text-align:left">Description</th>
                        <th style="text-align:left">Author</th>
                        <th style="text-align:left">AuthorLink</th>
                    </tr>
                    <xsl:for-each select="Recipes/Recipe">
                        <tr>
                            <td>
                                <xsl:value-of select="Title" />
                            </td>
                            <td>
                                <xsl:value-of select="Link" />
                            </td>
                            <td>
                                <xsl:value-of select="Rating" />
                            </td>
                            <td>
                                <xsl:value-of select="Description" />
                            </td>
	                        <td>
                                <xsl:value-of select="Author" />
                            </td>
							<td>
                                <xsl:value-of select="AuthorLink" />
                            </td>
                        </tr>
                         </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
