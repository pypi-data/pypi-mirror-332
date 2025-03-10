<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:svg="http://www.w3.org/2000/svg">
    <!-- Source: https://invent.kde.org/plasma/libplasma/-/blob/master/src/tools/apply-stylesheet.sh -->
    <xsl:output omit-xml-declaration="yes" indent="yes"/>
    <xsl:strip-space elements="*"/>

    <xsl:template match="@* | node()">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="svg:defs">
        <xsl:copy>
            <xsl:apply-templates select="@*" />
            <xsl:apply-templates select="*">
                <xsl:sort select="name()" data-type="text" order="descending"/>
            </xsl:apply-templates>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>
