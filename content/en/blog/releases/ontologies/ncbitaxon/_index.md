---
title: "NCBI organismal classification (NCBITaxon)"
linkTitle: "NCBI organismal classification"
tags: [ontologies,annotation,NCBITaxon]
categories: [ontologies,annotations]
weight: 100
date: 2022-01-05
Description: >
  An ontology representation of the NCBI organismal taxonomy.
ontology: "ncbitaxon"
cascade:
- type: "docs"
  _target:
    path: "/**"
---

<a href="https://www.ebi.ac.uk/ols/ontologies/{{< param "ontology" >}}" target="_blank"><img src="https://www.ebi.ac.uk/ols/img/OLS_logo_2017.png" style="max-width: 20%; background: #000000; padding: 5px;" alt="Open in the Ontology Lookup Service (OLS)" ></a>

<div id="result">
<script>  $( "#result" ).load( "https://www.ebi.ac.uk/ols/ontologies/{{< param "ontology" >}}  #ontology_info_box", function(){$("a[href^='../']").each(function(){$(this).attr('target','_blank');$(this).attr('href',$(this).attr('href').replace('../','https://www.ebi.ac.uk/ols/'));})})</script>


</script>
</div>