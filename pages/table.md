---
layout: null
title: Table
category: page
description: Welcome to BioContainers / RSEng MPI Projects!
permalink: /table/
---

<link href="https://rseng.github.io/web/assets/css/bootstrap.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">
 
    
<h1 style="padding-left:5px">Research Software / Biocontainers with MPI</h1>

<a style="padding-left:5px" href="{{ site.baseurl }}/"><< Return Home</a>
<script src='https://code.jquery.com/jquery-3.5.1.js'></script>
<link rel='stylesheet' href='https://cdn.datatables.net/1.12.1/css/dataTables.bootstrap4.min.css'>

<style>
#software_filter, #software_length, #software_info {
 color: #333;
}
td, th {
  color: #333;
}
.tag {
  margin-right: 2px !important;
}
</style>

<div class="container">
<a type="button" class="btn reset btn-theme filter-reset" onclick="$('#software').DataTable().search('').draw()" style='float:right;padding-bottom:5px' href="#">reset</a>
<table id="software"  class="table table-bordered" cellspacing="0" width="100%">
  <thead>
    <tr>
      <th>Repository</th>
      <th>Description</th>
      <th>Language</th>
      <th>Stars</th>
      <th>Forks</th>
      <th>Issues Open</th>
      <th>Issues Closed</th>
      <th>Topics</th>
    </tr>
  </thead>      
</table>
</div>

<script>
$(document).ready(function () {

$.getJSON("{{ site.baseurl }}/assets/repos.json", function(data) {
console.log(data)
$('#software').DataTable({
  data: data,
  pageLength: 50,
  columns: [
    { data: "github_url",
      render: function ( data, type, row ) { return "<a href='" + row['github_url'] + "' target='_blank'>" + data +"</a>";},
    },
    { data: "description"},
    { data: "language"},
    { data: "stars"},
    { data: "forks"},
    { data: "issues-open"},
    { data: "issues-closed"},
    { data: "topics", 
      render: function ( data, type, row ) { 
         var topics = ""
         if(data.length > 0) {
           $.each(data, function(i, e){
              topics += "<button onclick=$('#software').DataTable().search('"+ e +"').draw(); class='tag button btn btn-primary btn-xs'>" + e + "</button>";
           })
         }
         return topics
      },
    },
  ]
});
});

// Ensure search is aligned to the right!
$('#software_filter').parent().attr("class", "col-md-12")
})
</script>

<script src='https://cdn.datatables.net/1.12.1/js/jquery.dataTables.min.js'></script>
<script src='https://cdn.datatables.net/1.12.1/js/dataTables.bootstrap4.min.js'></script>

